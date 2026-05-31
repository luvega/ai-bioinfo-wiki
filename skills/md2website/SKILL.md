---
name: md2website
description: Bundle multiple Markdown files into a styled multi-page website with left sidebar navigation, hamburger menu on mobile, copy buttons on code/quote blocks, and a card-based landing page. Use this whenever the user provides 2+ .md files (or a directory of them) and asks to "整合成网站", "打包成网站", "做一个资料站", "做一个学员资料站", "build a website from these markdowns", "combine markdowns into a site", "create a navigation page for these docs", or wants to share a collection of related markdown docs as a browsable site. The skill handles pandoc conversion, image copying, optional Chinese-quote/list pre-processing, and asks the user whether to publish to page.xueheng.site or keep the site local-only.
---

# md2website

Turn a collection of Markdown files into a clean, navigable static website. The output is plain HTML/CSS/JS — no build tooling, no dependencies at runtime.

## When this skill applies

The user gives you several `.md` files (or a directory containing them) and wants them browsable as a small site. Examples:

- "把这几个 markdown 整合成一个学员资料站"
- "make a site from these tutorial markdowns"
- "I want a navigation page for docs/intro.md docs/setup.md docs/api.md"

If the user just wants **one** markdown file rendered as a single HTML page, prefer `publish-page` directly — this skill is for **multi-page bundles** with shared navigation.

## What the output looks like

- Left sidebar (260 px) listing every page numbered 01, 02, …, with a "首页" link pinned at the top
- Index page is a card grid with hero header — **no top bar** (the cards themselves are the navigation)
- Subpages share a sticky mobile top bar with a hamburger button that slides the sidebar in/out on screens ≤ 900 px
- Color palette: gray / white / light-blue (accent `#2563eb`)
- Code blocks (`<pre>`) and blockquotes get a "复制" button on hover; mobile shows it always
- Pandoc-rendered article body with MathJax support
- Mobile-safe: `overflow-x: hidden` on html/body so the page can't drift sideways from a long line of code (this bug bit me before — the CSS in `assets/style.css` already prevents it)

## Workflow

### 1. Collect the inputs

Find every `.md` the user wants on the site. If they pasted a list of paths, use exactly those in the order given. If they pointed at a directory, list the .md files (excluding obvious non-content like `README.md` for a tutorial bundle, unless the user asked otherwise) and confirm the order.

For each file, infer:
- **slug** — URL-safe, kebab-case, prefixed with `01-`, `02-`, … to keep ordering visible (`01-course-outline`, not `course-outline`)
- **title** — first H1 of the file, or filename stem with prefixes/extensions stripped
- **short** — one short subtitle line, 1 sentence max. Read the file's first paragraph or blockquote for inspiration; don't make it up if unclear, leave it short and generic

### 2. Plan with the user

Show a compact preview before building. Don't dump huge JSON:

```
Site title:   <inferred>
Total pages:  6
Pages:
  01 · T5+T6 课程内容大纲   — 课程整体规划与流程
  02 · 安装 plugin-dev 教程  — Claude Code 插件开发环境
  ...
```

Confirm:
- Does the order look right?
- Site title / hero text correct?
- **Publish to page.xueheng.site, or build locally only?** (this is mandatory — always ask explicitly)

If publishing, propose a slug like `<keyword>_<YYYYMMDD>` (today's date, kebab-case keyword). Examples: `lianxh-t5t6_20260502`, `python-tutorial_20260615`. The date suffix protects against accidentally overwriting a previous publish.

### 3. Write the config

Build a JSON config in a temp workspace (default: `/tmp/<slug>-site/`). The full annotated schema is in `references/config_example.json`. Truly minimal:

```json
{
  "site": { "title": "My docs" },
  "pages": [
    { "slug": "01-intro", "title": "Introduction", "source": "/abs/path/intro.md" },
    { "slug": "02-setup", "title": "Setup",        "source": "/abs/path/setup.md" }
  ]
}
```

That's enough to produce a working site (sidebar + landing cards + pages). Add the rest of the `site` fields (`brand`, `hero_*`, `footer`, etc.) for a polished landing page.

Field notes:
- `source` paths can be absolute or relative-to-the-config-file. Use absolute paths to avoid surprises.
- `nav_title` (optional, per page) is a shorter label for the sidebar when `title` is long.
- `footer` lines are inserted as raw HTML — handy for inline links, but you must escape `<`/`&` yourself if they appear in plain text.

### 4. Build

```bash
python3 ~/.claude/skills/md2website/scripts/build_site.py \
  --config /tmp/<slug>-site/config.json \
  --out /tmp/<slug>-site/build
```

The script:
- Auto-detects and applies `chinese-quote-converter` and the `publish-page` list-fix preprocessor if installed (no config needed; prints `preprocessors: …` to confirm)
- Runs pandoc with `--mathjax` per page
- Walks each markdown for `![](relative/path.png)` references — handles `![alt](path "title")` and `<path>` syntax — and copies the local images alongside the output preserving the relative path
- Writes `index.html` plus one `<slug>.html` per page, with `assets/style.css` and `assets/copy.js`

Verify by spot-checking the output:

```bash
ls /tmp/<slug>-site/build/
open /tmp/<slug>-site/build/index.html   # macOS preview
```

If the user wants to view it on another device on the same LAN (or the browser misbehaves with `file://`), serve the directory:

```bash
cd /tmp/<slug>-site/build && python3 -m http.server 8765
# then open http://localhost:8765/  or http://<your-LAN-ip>:8765/
```

### 5. Publish (only if user agreed)

Use the existing `publish-page` skill — don't reimplement uploading. Pass `--name <slug>_YYYYMMDD` so the URL is stable and date-stamped:

```bash
~/.claude/skills/publish-page/scripts/publish-page.sh \
  --name <slug>_<YYYYMMDD> \
  /tmp/<slug>-site/build/
```

Then verify with curl:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://page.xueheng.site/<slug>_<YYYYMMDD>/
```

A few things that have bitten me before:

- The `publish-page` script via the background-task runner sometimes hangs on slow scp. If you spawn it in the background and the output file stays empty after ~30 s, check `ps aux | grep sshpass`. If it's stuck, kill it and re-run in the foreground.
- For incremental fixes after the first publish (e.g. you tweaked one CSS value), don't re-run the whole publish — that re-uploads every file. Just `sshpass scp` the changed file straight into the live directory:

  ```bash
  sshpass -p 'IlikeMario1' scp -o StrictHostKeyChecking=no \
    /tmp/<slug>-site/build/assets/style.css \
    root@10.147.17.64:/var/www/page.xueheng.site/<slug>_<YYYYMMDD>/assets/
  ```

  Do NOT call `publish-page.sh <single-file>` to update a file inside a published subdirectory — that command uploads single files to the **site root** (`/`), not into your subdirectory, which both fails to update the site AND leaves a stray file at the root.

### 6. Report back

Tell the user:
- The local preview path (`file:///tmp/.../index.html`) — always
- The published URL (if applicable)
- Anything that didn't work cleanly (image not found, pandoc warning on a specific page)

## Customization knobs

If the user wants to tweak the look:

- **Different accent color**: edit `--accent` and `--accent-soft` in the generated `assets/style.css` (the script copies the bundled CSS verbatim — to override, edit the copy in `out_dir/assets/` after build, or pre-edit the bundled `~/.claude/skills/md2website/assets/style.css` for a permanent change)
- **Wider content area**: change `.page { max-width: 860px; ... }`
- **Narrower sidebar**: change `--sidebar-width: 260px`
- **Mobile breakpoint**: change `@media (max-width: 900px)` block

For one-off tweaks just edit the generated CSS in the workspace before publishing. For permanent style changes, edit the source CSS in this skill.

## What this skill is *not* for

- Single-file markdown rendering — use `publish-page` directly
- Real documentation sites with search / versioning / cross-page TOC — use Quarto, Docusaurus, MkDocs etc.
- Slide decks — use `marp-slides-creator` or `beamer-slides-creator`

## Files

- `scripts/build_site.py` — the builder; takes `--config` + `--out`
- `assets/style.css` — copied into every built site (modify here for global look changes)
- `assets/copy.js` — sidebar toggle + copy buttons (modify here for behavior changes)
- `references/config_example.json` — full annotated config schema
