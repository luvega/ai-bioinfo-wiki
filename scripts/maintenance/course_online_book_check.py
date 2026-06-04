"""Check AI_Course online Coursebook map, routes, and sample chapter coverage."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]
MAP_PATH = ROOT / "course" / "textbook" / "coursebook_map.yml"
SITE_DATA = ROOT / "site" / "src" / "data" / "coursebook.ts"
COURSEBOOK_INDEX = ROOT / "site" / "src" / "pages" / "coursebook.astro"
COURSEBOOK_ROUTE = ROOT / "site" / "src" / "pages" / "coursebook" / "[slug].astro"
WEEK_ROUTE = ROOT / "site" / "src" / "pages" / "weeks" / "[slug].astro"
SAMPLE_WEEKS = {3, 13, 14, 15, 16}
MODERN_OMICS_EXPECTATIONS = {
    13: ("Single_Cell_Best_Practices", "OSCA", "OSTA"),
    14: ("Single_Cell_Best_Practices", "OSCA", "OSTA"),
    15: ("Single_Cell_Best_Practices", "OSCA", "OSTA"),
    16: ("Single_Cell_Best_Practices", "OSCA", "OSTA"),
}
REPRODUCIBILITY_EXPECTATIONS = {
    2: ("OWF_Learn_Git", "OWF_Learn_Windows_Shell", "OWF_Learn_Linux_Shell"),
    3: ("OWF_Learn_Git",),
    17: ("OWF_Learn_Git", "OWF_Learn_Linux_Shell"),
}
REQUIRED_SAMPLE_FIELDS = (
    "introQuestion",
    "learningObjectives",
    "coreConcepts",
    "classroomCase",
    "aiBoundary",
    "verificationPoints",
    "pptBridge",
)
REQUIRED_SAMPLE_HEADINGS = (
    "导入问题",
    "学习目标",
    "核心概念",
    "课堂案例",
    "AI 协作边界",
    "来源",
    "待核验点",
    "PPT storyboard 生成入口说明",
)
WEEK13_TRANSITION_TERMS = (
    "表格矩阵",
    "bulk expression matrix",
    "single-cell",
    "spatial matrix",
    "样章候选",
    "UMAP",
)
PROJECT_WEEK_TERMS = {
    17: ("Git/GitHub", "素材溯源", "AI 使用声明", "storyboard", "图表证据边界"),
    18: ("数据来源", "图表表达", "证据边界", "AI 使用", "可复现记录"),
}


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


def contains_required_terms(text: str, terms: tuple[str, ...]) -> list[str]:
    return [term for term in terms if term not in text]


def has_forbidden_raw_reference(text: str) -> bool:
    return "materials/raw" in text.replace("\\", "/")


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
                if key in {"week", "chapter"}:
                    current[key] = int(value)
                else:
                    current[key] = value.strip("'\"")
                current_list = None
            else:
                current[key] = []
                current_list = key

    if current is not None:
        chapters.append(current)
    return chapters


def check_map(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    if not MAP_PATH.exists():
        return [Issue("MISSING_MAP", MAP_PATH, "coursebook_map.yml is missing")]
    chapters = parse_map(MAP_PATH)
    if len(chapters) != 18:
        issues.append(Issue("BAD_CHAPTER_COUNT", MAP_PATH, f"Expected 18 chapters, found {len(chapters)}"))
    seen_weeks = {chapter.get("week") for chapter in chapters}
    expected_weeks = set(range(1, 19))
    if seen_weeks != expected_weeks:
        issues.append(Issue("BAD_WEEK_COVERAGE", MAP_PATH, f"Expected weeks 1-18, found {sorted(seen_weeks)}"))

    for chapter in chapters:
        week = chapter.get("week")
        page = str(chapter.get("page", ""))
        if week in SAMPLE_WEEKS and page != f"/coursebook/week-{int(week):02d}":
            issues.append(Issue("BAD_SAMPLE_ROUTE", MAP_PATH, f"Week {week:02d} should route to /coursebook/week-{int(week):02d}"))
        if week not in SAMPLE_WEEKS and not page.startswith("/coursebook#week-"):
            issues.append(Issue("BAD_CATALOG_ROUTE", MAP_PATH, f"Week {week} should route to a Coursebook catalog anchor"))

        for field in ("source_week_files", "knowledge_sources", "material_sources"):
            values = chapter.get(field, [])
            if not isinstance(values, list) or not values:
                issues.append(Issue("EMPTY_SOURCE_FIELD", MAP_PATH, f"Week {week} has empty {field}"))
                continue
            for value in values:
                value_text = str(value)
                if has_forbidden_raw_reference(value_text):
                    issues.append(Issue("RAW_SOURCE_REFERENCE", MAP_PATH, f"{field} references raw source: {value_text}"))
                    continue
                candidate = root / value_text
                if not candidate.exists():
                    issues.append(Issue("MISSING_SOURCE_PATH", MAP_PATH, f"{field} -> {value_text}"))

        source_text = "\n".join(
            str(value)
            for field in ("knowledge_sources", "material_sources")
            for value in chapter.get(field, [])
        )
        if week in MODERN_OMICS_EXPECTATIONS:
            for marker in MODERN_OMICS_EXPECTATIONS[int(week)]:
                if marker not in source_text and marker.lower() not in source_text.lower():
                    issues.append(Issue("MISSING_MODERN_OMICS_SOURCE", MAP_PATH, f"Week {week:02d} should include {marker}"))
        if week in REPRODUCIBILITY_EXPECTATIONS:
            for marker in REPRODUCIBILITY_EXPECTATIONS[int(week)]:
                if marker not in source_text and marker.lower() not in source_text.lower():
                    issues.append(Issue("MISSING_REPRO_SOURCE", MAP_PATH, f"Week {week:02d} should include {marker}"))
    return issues


def check_site_data(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    if not SITE_DATA.exists():
        return [Issue("MISSING_SITE_DATA", SITE_DATA, "site/src/data/coursebook.ts is missing")]
    text = read_text(SITE_DATA)
    for week in SAMPLE_WEEKS:
        if f"slug: 'week-{week:02d}'" not in text and f'slug: "week-{week:02d}"' not in text:
            issues.append(Issue("MISSING_SAMPLE_DATA", SITE_DATA, f"Week {week:02d} sample chapter is missing"))
    for field in REQUIRED_SAMPLE_FIELDS:
        if field not in text:
            issues.append(Issue("MISSING_SAMPLE_FIELD", SITE_DATA, f"Missing sample field: {field}"))
    if "[[" in text or "]]" in text:
        issues.append(Issue("OBSIDIAN_LINK", SITE_DATA, "Obsidian wiki links are not allowed"))
    if has_forbidden_raw_reference(text):
        issues.append(Issue("RAW_SOURCE_REFERENCE", SITE_DATA, "Site data must not reference raw sources"))
    if re.search(r"script\.md.*formal_ready.*PPT", text, flags=re.S):
        issues.append(Issue("STATUS_CONFLATION", SITE_DATA, "Do not infer PPT readiness from script formal_ready status"))
    for required_text in ("现代组学拓展", "样章候选", "Single_Cell_Best_Practices", "OSCA", "OSTA"):
        if required_text not in text:
            issues.append(Issue("MISSING_MODERN_OMICS_DATA", SITE_DATA, f"Site data should expose {required_text}"))
    for required_text in ("可复现工作流", "OWF_Learn_Git"):
        if required_text not in text:
            issues.append(Issue("MISSING_REPRO_DATA", SITE_DATA, f"Site data should expose {required_text}"))
    return issues


def check_course_week_files(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    course_weeks_dir = root / "course" / "weeks"
    for week in range(1, 19):
        week_dir = course_weeks_dir / f"week_{week:02d}"
        materials_path = week_dir / "materials.md"
        if not materials_path.exists():
            issues.append(Issue("MISSING_WEEK_MATERIALS", materials_path, "Week materials.md is missing"))
            continue
        materials_text = read_text(materials_path)
        if "素材分层使用原则（2026-06-04）" not in materials_text:
            issues.append(Issue("MISSING_MATERIAL_LAYERING", materials_path, "Week materials must include the four-layer source policy"))
        week_files = (materials_path, week_dir / "outline.md", week_dir / "script.md")
        week_text_parts: list[str] = []
        for path in week_files:
            if not path.exists():
                continue
            path_text = read_text(path)
            week_text_parts.append(path_text)
            if has_forbidden_raw_reference(path_text):
                issues.append(Issue("RAW_SOURCE_REFERENCE", path, "Course week files must not reference materials/raw"))
        week_text = "\n".join(week_text_parts)
        if week == 13:
            for term in contains_required_terms(week_text, WEEK13_TRANSITION_TERMS):
                issues.append(Issue("MISSING_WEEK13_TRANSITION", week_dir, f"Week 13 should include {term}"))
        if week in PROJECT_WEEK_TERMS:
            for term in contains_required_terms(week_text, PROJECT_WEEK_TERMS[week]):
                issues.append(Issue("MISSING_PROJECT_WEEK_TERM", week_dir, f"Week {week:02d} should include {term}"))
    return issues


def check_routes() -> list[Issue]:
    issues: list[Issue] = []
    route_files = (COURSEBOOK_INDEX, COURSEBOOK_ROUTE, WEEK_ROUTE)
    for path in route_files:
        if not path.exists():
            issues.append(Issue("MISSING_ROUTE", path, "Required Astro route is missing"))
            continue
        text = read_text(path)
        if "[[" in text or "]]" in text:
            issues.append(Issue("OBSIDIAN_LINK", path, "Obsidian wiki links are not allowed"))
    if COURSEBOOK_ROUTE.exists():
        route_text = read_text(COURSEBOOK_ROUTE)
        for heading in REQUIRED_SAMPLE_HEADINGS:
            if heading not in route_text:
                issues.append(Issue("MISSING_SAMPLE_SECTION", COURSEBOOK_ROUTE, f"Missing rendered sample section: {heading}"))
    if WEEK_ROUTE.exists():
        week_route_text = read_text(WEEK_ROUTE)
        if "getCoursebookChapterByWeek" not in week_route_text or "/coursebook#week-" not in week_route_text:
            issues.append(Issue("MISSING_WEEK_BACKLINK", WEEK_ROUTE, "Week pages must link back to Coursebook sample or catalog status"))
    return issues


def run_check(root: Path = ROOT) -> list[Issue]:
    return [*check_map(root), *check_site_data(root), *check_routes(), *check_course_week_files(root)]


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: online Coursebook map, sample routes, source paths, and section coverage are current.")
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
