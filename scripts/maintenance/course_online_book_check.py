"""Check the single-track 12-chapter Coursebook site integration."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]
LOGICAL_V2_MAP_PATH = ROOT / "course" / "textbook" / "logical_v2" / "coursebook_map.yml"
SITE_DATA = ROOT / "site" / "src" / "data" / "coursebook.ts"
COURSEBOOK_INDEX = ROOT / "site" / "src" / "pages" / "coursebook.astro"
COURSEBOOK_ROUTE = ROOT / "site" / "src" / "pages" / "coursebook" / "[slug].astro"
LOGICAL_V2_INDEX = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2.astro"
LOGICAL_V2_ROUTE = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2" / "[slug].astro"
COURSEWARE_INDEX = ROOT / "site" / "src" / "pages" / "courseware.astro"
COURSEWARE_ROUTE = ROOT / "site" / "src" / "pages" / "courseware" / "[slug].astro"
WEEK_ROUTE = ROOT / "site" / "src" / "pages" / "weeks" / "[slug].astro"
COURSEBOOK_STATUS = "coursebook_ready"
REQUIRED_SUPPORT_FILES = (
    "course/evaluation/learning_outcome_matrix.md",
    "course/evaluation/student_project_rubric.md",
    "docs/course_status_dictionary.md",
    "course/templates/ai_use_statement_template.md",
    "course/templates/project_readme_template.md",
    "course/templates/data_sources_template.md",
)
FORBIDDEN_SITE_TERMS = (
    "Dual Track",
    "不替换 18 周",
    "并行审查",
    "审查样章",
    "教材写作口径",
)


class Issue(NamedTuple):
    code: str
    path: Path
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def has_forbidden_raw_reference(text: str) -> bool:
    return "materials/raw" in text.replace("\\", "/")


def has_obsidian_link(text: str) -> bool:
    return "[[" in text or "]]" in text


def has_banned_contrast(text: str) -> bool:
    return bool(re.search(r"不是.{0,30}而是", text))


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
                current[current_list].append(stripped[2:].strip().strip("'\""))
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = int(value) if key == "chapter" else value.strip("'\"")
                current_list = None
            else:
                current[key] = []
                current_list = key

    if current is not None:
        chapters.append(current)
    return chapters


def list_value(chapter: dict[str, object], field: str) -> list[str]:
    value = chapter.get(field, [])
    if not isinstance(value, list):
        return []
    return [str(item) for item in value if str(item).strip()]


def check_text_style(path: Path, text: str) -> list[Issue]:
    issues: list[Issue] = []
    if has_obsidian_link(text):
        issues.append(Issue("OBSIDIAN_LINK", path, "Obsidian wiki links are not allowed"))
    if has_forbidden_raw_reference(text):
        issues.append(Issue("RAW_SOURCE_REFERENCE", path, "Site and Coursebook files must not reference materials/raw"))
    for term in FORBIDDEN_SITE_TERMS:
        if term in text:
            issues.append(Issue("FORBIDDEN_SITE_TERM", path, f"Forbidden old Coursebook wording: {term}"))
    if has_banned_contrast(text):
        issues.append(Issue("BANNED_CONTRAST", path, "Avoid the 不是...而是 contrast pattern in site-facing prose"))
    return issues


def check_logical_v2_map(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    if not LOGICAL_V2_MAP_PATH.exists():
        return [Issue("MISSING_LOGICAL_V2_MAP", LOGICAL_V2_MAP_PATH, "logical_v2/coursebook_map.yml is missing")]
    chapters = parse_map(LOGICAL_V2_MAP_PATH)
    if len(chapters) != 12:
        issues.append(Issue("BAD_COURSEBOOK_COUNT", LOGICAL_V2_MAP_PATH, f"Expected 12 Coursebook chapters, found {len(chapters)}"))
    seen = [int(chapter.get("chapter", 0)) for chapter in chapters]
    if seen != list(range(1, 13)):
        issues.append(Issue("BAD_COURSEBOOK_SEQUENCE", LOGICAL_V2_MAP_PATH, f"Expected chapters 1-12, found {seen}"))

    for chapter in chapters:
        chapter_no = int(chapter.get("chapter", 0))
        expected_page = f"/coursebook/chapter-{chapter_no:02d}"
        expected_source = f"course/textbook/logical_v2/chapters/chapter_{chapter_no:02d}.md"
        expected_graph = f"course/textbook/logical_v2/graphs/chapter_{chapter_no:02d}_knowledge_graph.mmd"
        expected_image = f"/assets/coursebook/knowledge-maps/chapter-{chapter_no:02d}.svg"
        if str(chapter.get("status", "")) != COURSEBOOK_STATUS:
            issues.append(Issue("BAD_COURSEBOOK_STATUS", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should be {COURSEBOOK_STATUS}"))
        if str(chapter.get("coursebook_status", "")) != COURSEBOOK_STATUS:
            issues.append(Issue("BAD_COURSEBOOK_STATUS", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should expose coursebook_status"))
        if str(chapter.get("page", "")) != expected_page:
            issues.append(Issue("BAD_COURSEBOOK_PAGE", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should route to {expected_page}"))
        if str(chapter.get("chapter_source", "")) != expected_source:
            issues.append(Issue("BAD_COURSEBOOK_SOURCE", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should use {expected_source}"))
        if str(chapter.get("knowledge_graph", "")) != expected_graph:
            issues.append(Issue("BAD_KNOWLEDGE_GRAPH", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should use {expected_graph}"))
        if str(chapter.get("knowledge_map_image", "")) != expected_image:
            issues.append(Issue("BAD_KNOWLEDGE_MAP_IMAGE", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should expose {expected_image}"))
        if not str(chapter.get("chapter_focus", "")).strip():
            issues.append(Issue("EMPTY_CHAPTER_FOCUS", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should list chapter_focus"))
        if not str(chapter.get("core_question", "")).endswith("？"):
            issues.append(Issue("BAD_CORE_QUESTION", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} core_question should be a question"))
        for field in ("source_weeks", "source_chapters", "knowledge_sources", "material_sources", "asset_sources", "learning_evidence"):
            if not list_value(chapter, field):
                issues.append(Issue("EMPTY_COURSEBOOK_FIELD", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} has empty {field}"))
        for field in ("source_weeks", "source_chapters", "knowledge_sources", "material_sources", "asset_sources"):
            for value in list_value(chapter, field):
                if has_forbidden_raw_reference(value) or has_obsidian_link(value):
                    issues.append(Issue("FORBIDDEN_SOURCE_REFERENCE", LOGICAL_V2_MAP_PATH, f"Forbidden reference in {field}: {value}"))
                    continue
                if not (root / value).exists():
                    issues.append(Issue("MISSING_SOURCE_PATH", LOGICAL_V2_MAP_PATH, f"{field} -> {value}"))
        for value in [expected_source, expected_graph, *list_value(chapter, "process_diagrams")]:
            if not (root / value).exists():
                issues.append(Issue("MISSING_COURSEBOOK_ASSET", LOGICAL_V2_MAP_PATH, f"Expected generated source: {value}"))
        image_path = root / "site" / "public" / expected_image.lstrip("/")
        if not image_path.exists():
            issues.append(Issue("MISSING_KNOWLEDGE_MAP_IMAGE", image_path, "Generated chapter knowledge map image is missing"))
    return issues


def check_site_data(root: Path) -> list[Issue]:
    if not SITE_DATA.exists():
        return [Issue("MISSING_SITE_DATA", SITE_DATA, "site/src/data/coursebook.ts is missing")]
    text = read_text(SITE_DATA)
    issues = check_text_style(SITE_DATA, text)
    for required_text in (
        "CoursebookChapterStatus",
        "coursebook_ready",
        "coursebookChapters",
        "textbookChapters = coursebookChapters",
        "logicalV2Chapters = coursebookChapters",
        "coursewareWeeks",
        "weekToCoursebookChapter",
        "getCoursebookChapterByWeek",
        "/coursebook/chapter-01",
        "/coursebook/chapter-12",
        "knowledgeMapImage",
        "processDiagrams",
    ):
        if required_text not in text:
            issues.append(Issue("MISSING_SITE_DATA_FIELD", SITE_DATA, f"Site data should expose {required_text}"))
    for forbidden_text in ("page: '/coursebook/week-01'", "review_ready", "source_mapped", "CoursebookSample"):
        if forbidden_text in text:
            issues.append(Issue("STALE_SITE_DATA", SITE_DATA, f"Site data still contains old Coursebook term: {forbidden_text}"))
    return issues


def check_routes() -> list[Issue]:
    issues: list[Issue] = []
    route_files = (COURSEBOOK_INDEX, COURSEBOOK_ROUTE, LOGICAL_V2_INDEX, LOGICAL_V2_ROUTE, COURSEWARE_INDEX, COURSEWARE_ROUTE, WEEK_ROUTE)
    for path in route_files:
        if not path.exists():
            issues.append(Issue("MISSING_ROUTE", path, "Required Astro route is missing"))
            continue
        issues.extend(check_text_style(path, read_text(path)))

    if COURSEBOOK_INDEX.exists():
        text = read_text(COURSEBOOK_INDEX)
        for required_text in ("12 章", "coursebookChapters", "coursebook_ready", "知识图谱", "Courseware", "Weeks"):
            if required_text not in text:
                issues.append(Issue("MISSING_COURSEBOOK_INDEX", COURSEBOOK_INDEX, f"Coursebook index should expose {required_text}"))
        if "/coursebook/logical-v2" in text:
            issues.append(Issue("STALE_COURSEBOOK_INDEX", COURSEBOOK_INDEX, "Coursebook index should not link to the old logical-v2 entry"))

    if COURSEBOOK_ROUTE.exists():
        text = read_text(COURSEBOOK_ROUTE)
        for required_text in ("教材正文", "知识图谱", "来源映射", "学习证据", "反向周次", "Missing Coursebook chapter source", "knowledgeMapImage"):
            if required_text not in text:
                issues.append(Issue("MISSING_COURSEBOOK_ROUTE", COURSEBOOK_ROUTE, f"Coursebook route should expose {required_text}"))
        if "sampleChapters" in text or "chapter.sample" in text or "候选样章" in text:
            issues.append(Issue("STALE_SAMPLE_ROUTE", COURSEBOOK_ROUTE, "Coursebook route should not use sample-chapter semantics"))

    if LOGICAL_V2_INDEX.exists() and "http-equiv=\"refresh\"" not in read_text(LOGICAL_V2_INDEX):
        issues.append(Issue("MISSING_COMPAT_REDIRECT", LOGICAL_V2_INDEX, "Old logical-v2 index should redirect to /coursebook"))
    if LOGICAL_V2_ROUTE.exists() and "http-equiv=\"refresh\"" not in read_text(LOGICAL_V2_ROUTE):
        issues.append(Issue("MISSING_COMPAT_REDIRECT", LOGICAL_V2_ROUTE, "Old logical-v2 chapter route should redirect to the new chapter page"))

    if COURSEWARE_INDEX.exists():
        text = read_text(COURSEWARE_INDEX)
        for required_text in ("Teaching Plan 与 Storyboard 审核台", "Student action", "Timing", "storyboardReviewMetrics", "coursewareWeeks"):
            if required_text not in text:
                issues.append(Issue("MISSING_COURSEWARE_INDEX", COURSEWARE_INDEX, f"Courseware index should expose {required_text}"))

    if COURSEWARE_ROUTE.exists():
        text = read_text(COURSEWARE_ROUTE)
        for required_text in ("Teaching Plan", "Storyboard Review", "getCoursebookChapterByWeek", "40 页主干 storyboard 审核表", "studentAction", "storyboardMetrics"):
            if required_text not in text:
                issues.append(Issue("MISSING_COURSEWARE_ROUTE", COURSEWARE_ROUTE, f"Courseware route should expose {required_text}"))

    if WEEK_ROUTE.exists():
        text = read_text(WEEK_ROUTE)
        if "getCoursebookChapterByWeek" not in text or "/coursebook" not in text:
            issues.append(Issue("MISSING_WEEK_BACKLINK", WEEK_ROUTE, "Week pages must link back to the mapped Coursebook chapter"))
        if "/courseware/" not in text:
            issues.append(Issue("MISSING_COURSEWARE_BACKLINK", WEEK_ROUTE, "Week pages should link to Courseware teaching-plan pages"))
    return issues


def run_check(root: Path = ROOT) -> list[Issue]:
    missing_support = [
        Issue("MISSING_SUPPORT_FILE", root / relative_path, f"Required support file is missing: {relative_path}")
        for relative_path in REQUIRED_SUPPORT_FILES
        if not (root / relative_path).exists()
    ]
    return [*missing_support, *check_logical_v2_map(root), *check_site_data(root), *check_routes()]


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: single-track 12-chapter Coursebook routes, data, and generated visual assets are current.")
        return
    for issue in issues:
        print(f"{issue.code}: {rel(issue.path, root)}: {issue.message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Project root for tests or alternate workspaces.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()
    issues = run_check(root)
    print_issues(root, issues)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
