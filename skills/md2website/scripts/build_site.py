#!/usr/bin/env python3
"""Build a multi-page website from a bundle of Markdown files.

Reads a JSON config and produces a static site in `out_dir/`:
- index.html with hero + cards (no topbar)
- one HTML per page with shared left sidebar + mobile hamburger topbar
- assets/style.css and assets/copy.js (shared)
- images/ directory containing any locally-referenced images

Pandoc is required. Optional preprocessors are detected and applied if present:
- chinese-quote-converter: ~/.claude/skills/chinese-quote-converter/scripts/convert_quotes.py
- markdown list fix:      ~/.claude/skills/publish-page/scripts/fix_md_lists.py

Usage:
    python build_site.py --config config.json --out /tmp/my-site

Config schema: see references/config_example.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html import escape
from pathlib import Path
from typing import Optional

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = SKILL_DIR / "assets"

DEFAULT_QUOTE_CONVERTER = Path.home() / ".claude/skills/chinese-quote-converter/scripts/convert_quotes.py"
DEFAULT_LIST_FIX = Path.home() / ".claude/skills/publish-page/scripts/fix_md_lists.py"


# ----------------------- helpers -----------------------

def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def find_image_refs(md_path: Path) -> list[tuple[str, Path]]:
    """Return list of (relative_ref, absolute_source) for local images referenced in md.

    Handles markdown image syntax including optional title: ![alt](path "title").
    Strips URL fragments/queries. Skips remote URLs and data URIs.
    """
    text = md_path.read_text(encoding="utf-8", errors="replace")
    refs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text)
    out: list[tuple[str, Path]] = []
    for ref in refs:
        ref = ref.strip()
        # Strip optional title: `path "title"` or `path 'title'`
        ref = re.split(r'\s+["\']', ref, maxsplit=1)[0].strip()
        # Strip surrounding angle brackets: <path>
        if ref.startswith("<") and ref.endswith(">"):
            ref = ref[1:-1]
        if ref.startswith(("http://", "https://", "data:")):
            continue
        clean = re.sub(r'[#?].*$', '', ref).strip()
        if not clean:
            continue
        candidate = (md_path.parent / clean).resolve()
        if candidate.is_file():
            out.append((clean, candidate))
    return out


def preprocess(md_src: Path, helpers: dict) -> tuple[Path, list[Path]]:
    """Run optional preprocessors. Returns (final_path, list_of_temp_files_to_clean)."""
    cur = md_src
    temps: list[Path] = []
    for key in ("quote_converter", "list_fix"):
        script = helpers.get(key)
        if not script:
            continue
        sp = Path(script)
        if not sp.is_file():
            continue
        fd, tmppath = tempfile.mkstemp(suffix=".md")
        os.close(fd)
        with open(tmppath, "w", encoding="utf-8") as f:
            r = subprocess.run(["python3", str(sp), str(cur)], stdout=f)
            if r.returncode != 0:
                Path(tmppath).unlink(missing_ok=True)
                continue
        temps.append(Path(tmppath))
        cur = Path(tmppath)
    return cur, temps


def md_to_html_body(md_path: Path) -> str:
    r = subprocess.run(
        ["pandoc", str(md_path), "--mathjax", "-t", "html5"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        die(f"pandoc failed on {md_path}: {r.stderr}")
    return r.stdout


# ----------------------- HTML builders -----------------------

def render_sidebar(site: dict, pages: list[dict], current: str) -> str:
    brand_mark = escape(site.get("brand", site.get("title", "Site")))
    brand_sub = escape(site.get("brand_sub", ""))
    foot_lines = site.get("sidebar_foot", [])
    parts = ['<aside class="sidebar" id="sidebar" aria-label="导航">',
             '<div class="sidebar-inner">',
             f'<a class="brand" href="index.html"><span class="brand-mark">{brand_mark}</span>'
             f'<span class="brand-sub">{brand_sub}</span></a>',
             '<nav class="sidenav">',
             '<div class="sidenav-section">导航</div>']
    home_cls = ' class="active"' if current == "index" else ""
    parts.append(f'<a href="index.html"{home_cls}><span class="num">★</span><span>首页</span></a>')
    parts.append('<div class="sidenav-section">页面</div>')
    for i, p in enumerate(pages, 1):
        slug = p["slug"]
        title = escape(p.get("nav_title") or p["title"])
        num = f"{i:02d}"
        cls = ' class="active"' if current == slug else ""
        parts.append(
            f'<a href="{slug}.html"{cls}><span class="num">{num}</span><span>{title}</span></a>'
        )
    parts.append('</nav>')
    if foot_lines:
        parts.append('<div class="sidebar-foot">')
        for j, line in enumerate(foot_lines):
            cls = ' class="muted"' if j > 0 else ""
            parts.append(f'<p{cls}>{escape(line)}</p>')
        parts.append('</div>')
    parts += ['</div>', '</aside>',
              '<div class="sidebar-overlay" id="sidebarOverlay" aria-hidden="true"></div>']
    return "\n".join(parts)


def render_topbar(site: dict) -> str:
    brand = escape(site.get("brand", site.get("title", "Site")))
    return (
        '<header class="mobile-topbar">'
        '<button class="menu-toggle" id="menuToggle" aria-label="打开导航菜单" aria-expanded="false">'
        '<span class="hamburger"></span></button>'
        f'<a class="mobile-brand" href="index.html">{brand}</a>'
        '</header>'
    )


def render_footer(site: dict) -> str:
    lines = site.get("footer", [])
    if not lines:
        return '<footer class="site-footer"></footer>'
    parts = []
    for i, line in enumerate(lines):
        cls = ' class="muted"' if i > 0 else ''
        parts.append(f'<p{cls}>{line}</p>')  # raw HTML allowed in footer lines (links etc.)
    inner = "\n".join(parts)
    return f'<footer class="site-footer">{inner}</footer>'


def render_page(site: dict, pages: list[dict], idx: int, body: str) -> str:
    p = pages[idx]
    total = len(pages)
    title = escape(p["title"])
    short = escape(p.get("short", ""))
    site_title = escape(site.get("title", site.get("brand", "Site")))

    # prev / next
    if idx > 0:
        prev = pages[idx - 1]
        prev_html = (
            f'<a class="prev" href="{prev["slug"]}.html">'
            f'<span class="label">← 上一篇</span>{escape(prev["title"])}</a>'
        )
    else:
        prev_html = (
            '<a class="prev" href="index.html">'
            '<span class="label">← 返回</span>首页</a>'
        )
    if idx < total - 1:
        nxt = pages[idx + 1]
        next_html = (
            f'<a class="next" href="{nxt["slug"]}.html">'
            f'<span class="label">下一篇 →</span>{escape(nxt["title"])}</a>'
        )
    else:
        next_html = (
            '<a class="next" href="index.html">'
            '<span class="label">完成 →</span>返回首页</a>'
        )

    sidebar = render_sidebar(site, pages, p["slug"])
    topbar = render_topbar(site)
    footer = render_footer(site)

    return f"""<!DOCTYPE html>
<html lang="{site.get('lang', 'zh-CN')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {site_title}</title>
<link rel="stylesheet" href="assets/style.css">
<script>MathJax = {{ tex: {{ inlineMath: [["$","$"], ["\\\\(","\\\\)"]] }} }};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
<script src="assets/copy.js" defer></script>
</head>
<body>
{sidebar}
<div class="content">
{topbar}
<main class="page">
<div class="page-meta">第 {idx + 1} 篇 / 共 {total} 篇 · {short}</div>
<article>
{body}
</article>
<div class="page-nav">
{prev_html}
{next_html}
</div>
</main>
{footer}
</div>
</body>
</html>
"""


def render_index(site: dict, pages: list[dict]) -> str:
    site_title = escape(site.get("title", "Site"))
    sidebar = render_sidebar(site, pages, "index")
    footer = render_footer(site)

    hero_h1 = escape(site.get("hero_title", site.get("title", "Site")))
    hero_leads = site.get("hero_leads", [])
    hero_meta = site.get("hero_meta", [])

    leads_html = "\n".join(f'<p class="lead">{escape(l)}</p>' for l in hero_leads)
    meta_html = "".join(f'<span>{escape(m)}</span>' for m in hero_meta)
    meta_block = f'<div class="hero-meta">{meta_html}</div>' if meta_html else ""

    cards = []
    for i, p in enumerate(pages, 1):
        cards.append(
            f'<a class="card" href="{p["slug"]}.html">'
            f'<div class="card-num">{site.get("card_label", "页面")} {i:02d}</div>'
            f'<h3 class="card-title">{escape(p["title"])}</h3>'
            f'<p class="card-desc">{escape(p.get("short", ""))}</p>'
            f'<div class="card-foot">阅读 →</div>'
            f'</a>'
        )
    cards_html = "\n".join(cards)
    section_label = escape(site.get("section_title", "页面列表"))

    # NOTE: Index page intentionally omits the mobile-topbar — cards already
    # serve as navigation, so a hamburger would be redundant.
    return f"""<!DOCTYPE html>
<html lang="{site.get('lang', 'zh-CN')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{site_title}</title>
<link rel="stylesheet" href="assets/style.css">
<script src="assets/copy.js" defer></script>
</head>
<body>
{sidebar}
<div class="content">
<section class="hero">
<h1>{hero_h1}</h1>
{leads_html}
{meta_block}
</section>
<div class="section-title">{section_label}</div>
<div class="cards">
{cards_html}
</div>
{footer}
</div>
</body>
</html>
"""


# ----------------------- main -----------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Build a multi-page site from markdown bundle")
    ap.add_argument("--config", required=True, help="Path to JSON config")
    ap.add_argument("--out", required=True, help="Output directory")
    args = ap.parse_args()

    if not have("pandoc"):
        die("pandoc is required (brew install pandoc)")

    cfg_path = Path(args.config).resolve()
    if not cfg_path.is_file():
        die(f"config not found: {cfg_path}")
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

    site = cfg.get("site", {})
    pages = cfg.get("pages", [])
    if not pages:
        die("config has no pages")

    # Resolve preprocessor scripts (auto-detect if not set)
    helpers = cfg.get("helpers", {})
    if "quote_converter" not in helpers and DEFAULT_QUOTE_CONVERTER.is_file():
        helpers["quote_converter"] = str(DEFAULT_QUOTE_CONVERTER)
    if "list_fix" not in helpers and DEFAULT_LIST_FIX.is_file():
        helpers["list_fix"] = str(DEFAULT_LIST_FIX)
    if helpers:
        active = [k for k in ("quote_converter", "list_fix")
                  if helpers.get(k) and Path(helpers[k]).is_file()]
        if active:
            print(f"preprocessors: {', '.join(active)}")

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "assets").mkdir(exist_ok=True)
    (out_dir / "images").mkdir(exist_ok=True)

    # Copy bundled CSS/JS
    shutil.copy2(ASSETS_DIR / "style.css", out_dir / "assets/style.css")
    shutil.copy2(ASSETS_DIR / "copy.js", out_dir / "assets/copy.js")

    # Resolve source paths and validate
    base = cfg_path.parent
    for p in pages:
        for key in ("slug", "title", "source"):
            if key not in p:
                die(f"page missing required field '{key}': {p}")
        src = (base / p["source"]).resolve() if not Path(p["source"]).is_absolute() else Path(p["source"])
        if not src.is_file():
            die(f"source markdown not found: {src}")
        p["_source_path"] = src

    # Build each page
    for i, p in enumerate(pages):
        src = p["_source_path"]

        # Copy referenced images alongside (preserving relative ref structure)
        for ref, abs_src in find_image_refs(src):
            dest = out_dir / ref  # ref like "images/foo.png" — write under out/images/foo.png
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(abs_src, dest)

        processed, temps = preprocess(src, helpers)
        try:
            body = md_to_html_body(processed)
        finally:
            for t in temps:
                t.unlink(missing_ok=True)
        html = render_page(site, pages, i, body)
        (out_dir / f"{p['slug']}.html").write_text(html, encoding="utf-8")
        print(f"built: {p['slug']}.html")

    # Build index
    (out_dir / "index.html").write_text(render_index(site, pages), encoding="utf-8")
    print("built: index.html")
    print(f"\nDone. Output: {out_dir}")
    print(f"Preview: file://{out_dir}/index.html")


if __name__ == "__main__":
    main()
