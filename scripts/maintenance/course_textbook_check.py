"""Check AI_Course textbook source drafts and source-controlled assets."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]
TEXTBOOK = ROOT / "course" / "textbook"
CHAPTERS = TEXTBOOK / "chapters"
ASSETS = TEXTBOOK / "assets"
MAP_PATH = TEXTBOOK / "coursebook_map.yml"
SITE_DATA = ROOT / "site" / "src" / "data" / "coursebook.ts"
GRAPH_EDGES = ASSETS / "knowledge_graph" / "course_graph_edges.csv"
GRAPH_MERMAID = ASSETS / "knowledge_graph" / "course_graph.mmd"

REQUIRED_HEADINGS = (
    "## 本章导入",
    "## 学习目标",
    "## Storyboard 对应表",
    "## 本章主线与课程位置",
    "## 核心概念",
    "## 方法路线",
    "## 工具实现与代码样例",
    "## 方法流程与代码解读",
    "## 图表与结果解释",
    "## 课堂案例",
    "## AI 协作与核验",
    "## 练习与参考答案要点",
    "## 来源与待核验点",
)
TEXTBOOK_STATUSES = {"full_draft", "draft_needs_assets", "expanded_draft"}
EXPANDED_TEXTBOOK_STATUS = "expanded_draft"
EXPANDED_PPT_STATUS = "storyboard_expanded"
FOCUS_WEEKS = {3, 11, 12, 13, 14, 15, 16}
STATUS_CONFLATION_TERMS = {"pilot_candidate", "pilot_ready", "sample_ready", "evidence_review_pass", "storyboard", "pptx_trial_done"}


class Issue(NamedTuple):
    code: str
    path: Path
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel(path: Path, root: Path = ROOT) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def has_forbidden_reference(text: str) -> bool:
    normalized = text.replace("\\", "/")
    return "materials/raw" in normalized or "[[" in text or "]]" in text


def chinese_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\n(.*?)\n---", text, flags=re.S)
    return match.group(1) if match else ""


def frontmatter_scalar(fm: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", fm, flags=re.M)
    return match.group(1).strip().strip("'\"") if match else ""


def frontmatter_list(fm: str, key: str) -> list[str]:
    values: list[str] = []
    in_block = False
    for line in fm.splitlines():
        stripped = line.strip()
        if stripped == f"{key}:":
            in_block = True
            continue
        if in_block:
            if stripped.startswith("- "):
                values.append(stripped[2:].strip().strip("'\""))
                continue
            if stripped and not line.startswith((" ", "\t")):
                break
    return values


def scalar_value(line: str) -> str:
    return line.split(":", 1)[1].strip().strip("'\"")


def parse_map(path: Path) -> list[dict[str, object]]:
    chapters: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list: str | None = None
    in_chapters = False
    for raw_line in read_text(path).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        stripped = raw_line.strip()
        if stripped == "chapters:":
            in_chapters = True
            continue
        if not in_chapters:
            continue
        if stripped.startswith("- chapter:"):
            if current is not None:
                chapters.append(current)
            current = {"chapter": int(scalar_value(stripped))}
            current_list = None
            continue
        if current is None:
            continue
        if stripped.startswith("- "):
            if current_list:
                current.setdefault(current_list, [])
                assert isinstance(current[current_list], list)
                current[current_list].append(stripped[2:].strip())
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = int(value) if key in {"week", "chapter", "storyboard_pages"} else value.strip("'\"")
                current_list = None
            else:
                current[key] = []
                current_list = key
    if current is not None:
        chapters.append(current)
    return chapters


def check_chapters(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    for week in range(1, 19):
        path = root / "course" / "textbook" / "chapters" / f"chapter_{week:02d}.md"
        if not path.exists():
            issues.append(Issue("MISSING_CHAPTER", path, f"Chapter {week:02d} source draft is missing"))
            continue
        text = read_text(path)
        fm = frontmatter(text)
        if has_forbidden_reference(text):
            issues.append(Issue("FORBIDDEN_REFERENCE", path, "Textbook chapters must not reference raw paths or Obsidian links"))
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                issues.append(Issue("MISSING_CHAPTER_SECTION", path, f"Missing required section: {heading}"))
        textbook_status = frontmatter_scalar(fm, "textbook_status")
        if textbook_status not in TEXTBOOK_STATUSES:
            issues.append(Issue("BAD_TEXTBOOK_STATUS", path, f"textbook_status must be one of {sorted(TEXTBOOK_STATUSES)}, found {textbook_status or 'missing'}"))
        if textbook_status != EXPANDED_TEXTBOOK_STATUS:
            issues.append(Issue("TEXTBOOK_NOT_EXPANDED", path, f"textbook_status should be {EXPANDED_TEXTBOOK_STATUS}, found {textbook_status or 'missing'}"))
        if textbook_status in STATUS_CONFLATION_TERMS:
            issues.append(Issue("STATUS_CONFLATION", path, "textbook_status must not reuse review_status or ppt_status values"))
        if frontmatter_scalar(fm, "storyboard_source") != f"course/weeks/week_{week:02d}/ppt_storyboard.md":
            issues.append(Issue("BAD_STORYBOARD_SOURCE", path, "Each expanded chapter must point to its weekly storyboard"))
        if frontmatter_scalar(fm, "storyboard_pages") != "40":
            issues.append(Issue("BAD_STORYBOARD_PAGES", path, "Each expanded chapter must list storyboard_pages: 40"))
        min_chars = 7000 if week in FOCUS_WEEKS else 5000
        count = chinese_count(text)
        if count < min_chars:
            issues.append(Issue("SHORT_EXPANDED_CHAPTER", path, f"Expected at least {min_chars} Chinese chars, found {count}"))
        assets = frontmatter_list(fm, "asset_sources")
        if len(assets) < 3:
            issues.append(Issue("MISSING_ASSET_SOURCES", path, "Each chapter must list dataset, code, and diagram assets"))
        for asset in assets:
            candidate = root / asset
            if not candidate.exists():
                issues.append(Issue("MISSING_ASSET", path, f"asset source does not exist: {asset}"))
    return issues


def check_map(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    chapters = parse_map(root / "course" / "textbook" / "coursebook_map.yml")
    if len(chapters) != 18:
        issues.append(Issue("BAD_MAP_SIZE", MAP_PATH, f"Expected 18 mapped chapters, found {len(chapters)}"))
    for chapter in chapters:
        week = int(chapter.get("week", 0))
        expected_page = f"/coursebook/week-{week:02d}"
        if chapter.get("page") != expected_page:
            issues.append(Issue("BAD_TEXTBOOK_ROUTE", MAP_PATH, f"Week {week:02d} should route to {expected_page}"))
        chapter_source = str(chapter.get("chapter_source", ""))
        if chapter_source != f"course/textbook/chapters/chapter_{week:02d}.md":
            issues.append(Issue("BAD_CHAPTER_SOURCE", MAP_PATH, f"Week {week:02d} chapter_source is missing or wrong"))
        textbook_status = str(chapter.get("textbook_status", ""))
        if textbook_status not in TEXTBOOK_STATUSES:
            issues.append(Issue("BAD_MAP_TEXTBOOK_STATUS", MAP_PATH, f"Week {week:02d} textbook_status is {textbook_status or 'missing'}"))
        if textbook_status != EXPANDED_TEXTBOOK_STATUS:
            issues.append(Issue("MAP_TEXTBOOK_NOT_EXPANDED", MAP_PATH, f"Week {week:02d} textbook_status should be {EXPANDED_TEXTBOOK_STATUS}"))
        if textbook_status in STATUS_CONFLATION_TERMS:
            issues.append(Issue("STATUS_CONFLATION", MAP_PATH, f"Week {week:02d} textbook_status reuses non-textbook status"))
        if chapter.get("storyboard_source") != f"course/weeks/week_{week:02d}/ppt_storyboard.md":
            issues.append(Issue("BAD_MAP_STORYBOARD_SOURCE", MAP_PATH, f"Week {week:02d} storyboard_source is missing or wrong"))
        if chapter.get("storyboard_pages") != 40:
            issues.append(Issue("BAD_MAP_STORYBOARD_PAGES", MAP_PATH, f"Week {week:02d} storyboard_pages should be 40"))
        if chapter.get("ppt_status") != EXPANDED_PPT_STATUS:
            issues.append(Issue("BAD_MAP_PPT_STATUS", MAP_PATH, f"Week {week:02d} ppt_status should be {EXPANDED_PPT_STATUS}"))
        assets = chapter.get("asset_sources", [])
        if not isinstance(assets, list) or len(assets) < 3:
            issues.append(Issue("MISSING_MAP_ASSETS", MAP_PATH, f"Week {week:02d} must list source-controlled assets"))
            continue
        for asset in assets:
            asset_text = str(asset)
            if has_forbidden_reference(asset_text):
                issues.append(Issue("FORBIDDEN_REFERENCE", MAP_PATH, f"Map must not reference raw paths: {asset_text}"))
                continue
            if not (root / asset_text).exists():
                issues.append(Issue("MISSING_MAP_ASSET", MAP_PATH, f"asset source does not exist: {asset_text}"))
    return issues


def check_knowledge_graph(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    edges = root / "course" / "textbook" / "assets" / "knowledge_graph" / "course_graph_edges.csv"
    mermaid = root / "course" / "textbook" / "assets" / "knowledge_graph" / "course_graph.mmd"
    if not edges.exists():
        issues.append(Issue("MISSING_GRAPH_EDGES", edges, "Knowledge graph edge table is missing"))
        return issues
    if not mermaid.exists():
        issues.append(Issue("MISSING_GRAPH_MERMAID", mermaid, "Knowledge graph Mermaid source is missing"))
        return issues
    graph_text = read_text(mermaid)
    rows = list(csv.DictReader(edges.open(encoding="utf-8", newline="")))
    if len(rows) < 18 * 4:
        issues.append(Issue("SMALL_GRAPH", edges, "Knowledge graph edge table is unexpectedly small"))
    for week in range(1, 19):
        if f"Week {week:02d}" not in graph_text or f"Chapter {week:02d}" not in graph_text:
            issues.append(Issue("MISSING_GRAPH_NODE", mermaid, f"Mermaid graph should include Week/Chapter {week:02d}"))
        if not any(row["source"] == f"Week {week:02d}" and row["target"] == f"Chapter {week:02d}" for row in rows):
            issues.append(Issue("MISSING_GRAPH_EDGE", edges, f"Edge table should map Week {week:02d} to Chapter {week:02d}"))
    return issues


def check_site_data(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    text = read_text(root / "site" / "src" / "data" / "coursebook.ts")
    for required in ("textbook_expanded_draft", "storyboard_expanded", "textbookChapterSource", "textbookAssetSources", "textbookStoryboardSource", "教材扩写稿"):
        if required not in text:
            issues.append(Issue("MISSING_SITE_TEXTBOOK_INTERFACE", SITE_DATA, f"Site data should expose {required}"))
    for week in range(1, 19):
        if f"page: '/coursebook/week-{week:02d}'" not in text and f'page: "/coursebook/week-{week:02d}"' not in text:
            issues.append(Issue("MISSING_SITE_ROUTE", SITE_DATA, f"Site data should route Week {week:02d} to textbook chapter page"))
    return issues


def run_check(root: Path = ROOT) -> list[Issue]:
    return [*check_chapters(root), *check_map(root), *check_knowledge_graph(root), *check_site_data(root)]


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: textbook chapters, source assets, knowledge graph, and status separation are current.")
        return
    for issue in issues:
        print(f"{issue.code}: {rel(issue.path, root)}: {issue.message}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    issues = run_check(root)
    print_issues(root, issues)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
