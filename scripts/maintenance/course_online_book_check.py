"""Check AI_Course online Coursebook map, routes, and sample chapter coverage."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]
MAP_PATH = ROOT / "course" / "textbook" / "coursebook_map.yml"
LOGICAL_V2_MAP_PATH = ROOT / "course" / "textbook" / "logical_v2" / "coursebook_map.yml"
SITE_DATA = ROOT / "site" / "src" / "data" / "coursebook.ts"
COURSEBOOK_INDEX = ROOT / "site" / "src" / "pages" / "coursebook.astro"
COURSEBOOK_REVIEW = ROOT / "site" / "src" / "pages" / "coursebook" / "review.astro"
COURSEBOOK_ROUTE = ROOT / "site" / "src" / "pages" / "coursebook" / "[slug].astro"
LOGICAL_V2_INDEX = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2.astro"
LOGICAL_V2_ROUTE = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2" / "[slug].astro"
COURSEWARE_INDEX = ROOT / "site" / "src" / "pages" / "courseware.astro"
COURSEWARE_ROUTE = ROOT / "site" / "src" / "pages" / "courseware" / "[slug].astro"
WEEK_ROUTE = ROOT / "site" / "src" / "pages" / "weeks" / "[slug].astro"
SAMPLE_WEEKS = {3, 13, 14, 15, 16}
LOGICAL_V2_REVIEW_CHAPTERS = {1, 2, 4, 8, 11, 12}
MINIMUM_REVIEW_STATUSES = {"pilot_candidate", "pilot_ready", "sample_ready", "evidence_review_pass"}
MINIMUM_WEEK_FILE_STATUSES = {"pilot_candidate", "pilot_ready"}
TRIAL_READY_PACK_WEEKS = {1, 2, 4, 5, 6, 7, 8, 9, 10, 17, 18}
TRIAL_READY_PACK_TERMS = (
    "2 学时时间切分",
    "课堂",
    "预期输出",
    "参考答案",
    "常见误区",
    "AI 审计提示",
)
STALE_PLACEHOLDERS = ("待提炼", "待抽取", "待定")
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
    "教学计划与 PPT storyboard 入口",
)
WEEK13_TRANSITION_TERMS = (
    "表格矩阵",
    "bulk expression matrix",
    "single-cell",
    "spatial matrix",
    "试讲就绪",
    "UMAP",
    "PCA 坐标",
    "聚类参数",
)
PROJECT_WEEK_TERMS = {
    17: ("Git/GitHub", "素材溯源", "AI 使用声明", "storyboard", "图表证据边界"),
    18: ("数据来源", "图表表达", "证据边界", "AI 使用", "可复现记录"),
}
REQUIRED_SUPPORT_FILES = (
    "course/evaluation/learning_outcome_matrix.md",
    "course/evaluation/student_project_rubric.md",
    "course/evaluation/week_13_ppt_evidence_review.md",
    "course/evaluation/week_14_ppt_evidence_review.md",
    "course/evaluation/week_16_ppt_evidence_review.md",
    "course/evaluation/full_week_pilot_candidate_review.md",
    "docs/course_status_dictionary.md",
    "course/templates/ai_use_statement_template.md",
    "course/templates/project_readme_template.md",
    "course/templates/data_sources_template.md",
    "course/templates/ppt_storyboard_template.md",
    "course/weeks/week_11_13_micro_project.md",
    "course/weeks/week_11_13_classroom_tables.md",
    "course/weeks/week_13/ppt_storyboard.md",
    "course/weeks/week_13/teaching_assets.md",
    "scripts/courseware/build_week13_teaching_figures.py",
)
REQUIRED_TRIAL_READY_PACKS = tuple(
    f"course/weeks/week_{week:02d}/teaching_pack_v1.md" for week in sorted(TRIAL_READY_PACK_WEEKS)
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
                if key in {"week", "chapter", "storyboard_pages"}:
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
        review_status = str(chapter.get("review_status", ""))
        ppt_status = str(chapter.get("ppt_status", ""))
        title = str(chapter.get("title", ""))
        if page != f"/coursebook/week-{int(week):02d}":
            issues.append(Issue("BAD_TEXTBOOK_ROUTE", MAP_PATH, f"Week {week:02d} should route to /coursebook/week-{int(week):02d}"))
        if week == 5 and title != "数据读取与整理":
            issues.append(Issue("BAD_WEEK05_TITLE", MAP_PATH, "Week 05 title should be 数据读取与整理"))
        if str(chapter.get("chapter_source", "")) != f"course/textbook/chapters/chapter_{int(week):02d}.md":
            issues.append(Issue("MISSING_CHAPTER_SOURCE", MAP_PATH, f"Week {week:02d} should list a chapter_source"))
        if str(chapter.get("textbook_status", "")) not in {"full_draft", "draft_needs_assets", "expanded_draft"}:
            issues.append(Issue("BAD_TEXTBOOK_STATUS", MAP_PATH, f"Week {week:02d} should list a textbook_status"))
        if str(chapter.get("textbook_status", "")) != "expanded_draft":
            issues.append(Issue("TEXTBOOK_NOT_EXPANDED", MAP_PATH, f"Week {week:02d} textbook_status should be expanded_draft"))
        if str(chapter.get("storyboard_source", "")) != f"course/weeks/week_{int(week):02d}/ppt_storyboard.md":
            issues.append(Issue("BAD_STORYBOARD_SOURCE", MAP_PATH, f"Week {week:02d} should list a storyboard_source"))
        if str(chapter.get("teaching_plan_source", "")) != f"course/weeks/week_{int(week):02d}/teaching_plan.md":
            issues.append(Issue("BAD_TEACHING_PLAN_SOURCE", MAP_PATH, f"Week {week:02d} should list a teaching_plan_source"))
        teaching_plan_source = str(chapter.get("teaching_plan_source", ""))
        if teaching_plan_source and not (root / teaching_plan_source).exists():
            issues.append(Issue("MISSING_TEACHING_PLAN_SOURCE", MAP_PATH, f"teaching_plan_source -> {teaching_plan_source}"))
        if chapter.get("storyboard_pages") != 40:
            issues.append(Issue("BAD_STORYBOARD_PAGES", MAP_PATH, f"Week {week:02d} storyboard_pages should be 40"))
        asset_sources = chapter.get("asset_sources", [])
        if not isinstance(asset_sources, list) or len(asset_sources) < 3:
            issues.append(Issue("MISSING_ASSET_SOURCES", MAP_PATH, f"Week {week:02d} should list source-controlled textbook assets"))
        else:
            for asset in asset_sources:
                candidate = root / str(asset)
                if not candidate.exists():
                    issues.append(Issue("MISSING_ASSET_PATH", MAP_PATH, f"asset_sources -> {asset}"))
        if review_status not in MINIMUM_REVIEW_STATUSES:
            issues.append(Issue("LOW_REVIEW_STATUS", MAP_PATH, f"Week {week:02d} review_status should be at least pilot_candidate, found {review_status}"))
        if week == 13 and review_status != "pilot_ready":
            issues.append(Issue("BAD_WEEK13_STATUS", MAP_PATH, "Week 13 should be pilot_ready after reproducible teaching figures and evidence review"))
        if ppt_status != "storyboard_expanded":
            issues.append(Issue("BAD_EXPANDED_PPT_STATUS", MAP_PATH, f"Week {week:02d} ppt_status should be storyboard_expanded without claiming PPTX completion"))
        if week in {14, 16} and review_status != "evidence_review_pass":
            issues.append(Issue("BAD_EVIDENCE_STATUS", MAP_PATH, f"Week {week:02d} should be evidence_review_pass after public asset strategy is closed"))

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


def check_logical_v2_map(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    if not LOGICAL_V2_MAP_PATH.exists():
        return [Issue("MISSING_LOGICAL_V2_MAP", LOGICAL_V2_MAP_PATH, "logical_v2/coursebook_map.yml is missing")]
    chapters = parse_map(LOGICAL_V2_MAP_PATH)
    if len(chapters) != 12:
        issues.append(Issue("BAD_LOGICAL_V2_COUNT", LOGICAL_V2_MAP_PATH, f"Expected 12 logical v2 chapters, found {len(chapters)}"))
    seen = {int(chapter.get("chapter", 0)) for chapter in chapters}
    if seen != set(range(1, 13)):
        issues.append(Issue("BAD_LOGICAL_V2_COVERAGE", LOGICAL_V2_MAP_PATH, f"Expected chapters 1-12, found {sorted(seen)}"))
    for chapter in chapters:
        chapter_no = int(chapter.get("chapter", 0))
        status = str(chapter.get("status", ""))
        if chapter_no in LOGICAL_V2_REVIEW_CHAPTERS:
            expected_page = f"/coursebook/logical-v2/chapter-{chapter_no:02d}"
            expected_source = f"course/textbook/logical_v2/chapters/chapter_{chapter_no:02d}.md"
            if status != "review_ready":
                issues.append(Issue("LOGICAL_V2_NOT_REVIEW_READY", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should be review_ready"))
            if str(chapter.get("review_status", "")) != "review_ready":
                issues.append(Issue("LOGICAL_V2_BAD_REVIEW_STATUS", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should expose review_status"))
            if str(chapter.get("page", "")) != expected_page:
                issues.append(Issue("LOGICAL_V2_BAD_PAGE", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should route to {expected_page}"))
            if str(chapter.get("chapter_source", "")) != expected_source:
                issues.append(Issue("LOGICAL_V2_BAD_SOURCE", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should use {expected_source}"))
            if not (root / expected_source).exists():
                issues.append(Issue("LOGICAL_V2_MISSING_CHAPTER", root / expected_source, f"Chapter {chapter_no:02d} review draft is missing"))
        elif status != "source_mapped":
            issues.append(Issue("LOGICAL_V2_UNEXPECTED_STATUS", LOGICAL_V2_MAP_PATH, f"Chapter {chapter_no:02d} should remain source_mapped"))
    return issues


def check_site_data(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    if not SITE_DATA.exists():
        return [Issue("MISSING_SITE_DATA", SITE_DATA, "site/src/data/coursebook.ts is missing")]
    text = read_text(SITE_DATA)
    for week in range(1, 19):
        if f"slug: 'week-{week:02d}'" not in text and f'slug: "week-{week:02d}"' not in text:
            issues.append(Issue("MISSING_CHAPTER_DATA", SITE_DATA, f"Week {week:02d} chapter data is missing"))
        if f"page: '/coursebook/week-{week:02d}'" not in text and f'page: "/coursebook/week-{week:02d}"' not in text:
            issues.append(Issue("MISSING_TEXTBOOK_ROUTE", SITE_DATA, f"Week {week:02d} should route to full textbook page"))
    for field in REQUIRED_SAMPLE_FIELDS:
        if field not in text:
            issues.append(Issue("MISSING_SAMPLE_FIELD", SITE_DATA, f"Missing sample field: {field}"))
    if "[[" in text or "]]" in text:
        issues.append(Issue("OBSIDIAN_LINK", SITE_DATA, "Obsidian wiki links are not allowed"))
    if has_forbidden_raw_reference(text):
        issues.append(Issue("RAW_SOURCE_REFERENCE", SITE_DATA, "Site data must not reference raw sources"))
    if "数据读取与整形" in text:
        issues.append(Issue("BAD_WEEK05_TITLE", SITE_DATA, "Week 05 title should use 数据读取与整理"))
    if re.search(r"script\.md.*formal_ready.*PPT", text, flags=re.S):
        issues.append(Issue("STATUS_CONFLATION", SITE_DATA, "Do not infer PPT readiness from script formal_ready status"))
    if re.search(r"reviewStatus:\s*['\"]catalog_only", text):
        issues.append(Issue("LOW_REVIEW_STATUS", SITE_DATA, "Coursebook data should not leave any week at catalog_only after full-week pilot candidate review"))
    if re.search(r"status:\s*['\"]目录占位", text):
        issues.append(Issue("LOW_DISPLAY_STATUS", SITE_DATA, "Coursebook data should display expanded textbook draft status, not catalog placeholders"))
    for required_text in ("expanded_draft", "storyboard_expanded", "textbookChapterSource", "textbookAssetSources", "textbookStoryboardSource", "textbookTeachingPlanSource", "textbookChapters", "coursewareWeeks", "CoursewareWeek", "教材扩写稿"):
        if required_text not in text:
            issues.append(Issue("MISSING_TEXTBOOK_INTERFACE", SITE_DATA, f"Site data should expose {required_text}"))
    for required_text in ("LogicalV2Chapter", "logicalV2Chapters", "logicalV2ReviewChapters", "review_ready", "/coursebook/logical-v2/chapter-01", "/coursebook/logical-v2/chapter-12"):
        if required_text not in text:
            issues.append(Issue("MISSING_LOGICAL_V2_DATA", SITE_DATA, f"Site data should expose {required_text}"))
    if "CoursebookStatus" in text:
        issues.append(Issue("STATUS_CONFLATION", SITE_DATA, "Site data should split textbookChapters and coursewareWeeks instead of a single CoursebookStatus"))
    for required_text in ("现代组学拓展", "试点候选", "pilot_candidate", "pilot_ready", "evidence_review_pass", "Single_Cell_Best_Practices", "OSCA", "OSTA"):
        if required_text not in text:
            issues.append(Issue("MISSING_MODERN_OMICS_DATA", SITE_DATA, f"Site data should expose {required_text}"))
    if "试讲包 v1" not in text:
        issues.append(Issue("MISSING_TRIAL_READY_PACK_DATA", SITE_DATA, "Site data should expose trial-ready pack badges"))
    for required_text in ("可复现工作流", "OWF_Learn_Git", "AI 使用声明", "项目 rubric", "student_project_rubric"):
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
        trial_pack_path = week_dir / "teaching_pack_v1.md"
        week_files = (materials_path, week_dir / "outline.md", week_dir / "script.md")
        week_text_parts: list[str] = []
        for path in week_files:
            if not path.exists():
                continue
            path_text = read_text(path)
            week_text_parts.append(path_text)
            if path.name in {"materials.md", "outline.md"}:
                status_match = re.search(r"^status:\s*(\S+)", path_text, flags=re.M)
                status_value = status_match.group(1).strip("'\"") if status_match else ""
                if status_value not in MINIMUM_WEEK_FILE_STATUSES:
                    issues.append(Issue("LOW_WEEK_FILE_STATUS", path, f"{path.name} should be pilot_candidate or pilot_ready, found {status_value or 'missing'}"))
                if status_value in MINIMUM_WEEK_FILE_STATUSES:
                    for placeholder in STALE_PLACEHOLDERS:
                        if placeholder in path_text:
                            issues.append(Issue("STALE_WEEK_PLACEHOLDER", path, f"{path.name} still contains placeholder text: {placeholder}"))
            if has_forbidden_raw_reference(path_text):
                issues.append(Issue("RAW_SOURCE_REFERENCE", path, "Course week files must not reference materials/raw"))
        if week in TRIAL_READY_PACK_WEEKS:
            if not trial_pack_path.exists():
                issues.append(Issue("MISSING_TRIAL_READY_PACK", trial_pack_path, f"Week {week:02d} should include teaching_pack_v1.md"))
            else:
                pack_text = read_text(trial_pack_path)
                week_text_parts.append(pack_text)
                for term in contains_required_terms(pack_text, TRIAL_READY_PACK_TERMS):
                    issues.append(Issue("MISSING_TRIAL_READY_PACK_TERM", trial_pack_path, f"Week {week:02d} teaching pack should include {term}"))
                if has_forbidden_raw_reference(pack_text):
                    issues.append(Issue("RAW_SOURCE_REFERENCE", trial_pack_path, "Teaching packs must not reference materials/raw"))
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
    route_files = (COURSEBOOK_INDEX, COURSEBOOK_ROUTE, LOGICAL_V2_INDEX, LOGICAL_V2_ROUTE, COURSEWARE_INDEX, COURSEWARE_ROUTE, WEEK_ROUTE)
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
        if "候选样章待完成事项" not in route_text:
            issues.append(Issue("MISSING_CANDIDATE_CHECKS", COURSEBOOK_ROUTE, "Sample route should render candidate chapter pending checks"))
        for forbidden_text in ("Storyboard 审核表", "studentAction", "storyboardMetrics"):
            if forbidden_text in route_text:
                issues.append(Issue("COURSEBOOK_STORYBOARD_CONFLATION", COURSEBOOK_ROUTE, f"Coursebook chapter route should not render page-level review table: {forbidden_text}"))
        for required_text in ("教材正文", "Courseware 审核页", "教学计划与 PPT storyboard 入口"):
            if required_text not in route_text:
                issues.append(Issue("MISSING_COURSEBOOK_TEXTBOOK_VIEW", COURSEBOOK_ROUTE, f"Coursebook chapter route should expose {required_text}"))
    if COURSEBOOK_REVIEW.exists():
        review_text = read_text(COURSEBOOK_REVIEW)
        for required_text in ("Courseware", "/courseware", "兼容入口"):
            if required_text not in review_text:
                issues.append(Issue("STALE_COURSEBOOK_REVIEW_VIEW", COURSEBOOK_REVIEW, f"Coursebook review compatibility route should expose {required_text}"))
    if COURSEWARE_INDEX.exists():
        courseware_index_text = read_text(COURSEWARE_INDEX)
        for required_text in ("Teaching Plan 与 Storyboard 审核台", "Student action", "Timing", "storyboardReviewMetrics", "coursewareWeeks"):
            if required_text not in courseware_index_text:
                issues.append(Issue("MISSING_COURSEWARE_INDEX", COURSEWARE_INDEX, f"Courseware index should expose {required_text}"))
    if COURSEWARE_ROUTE.exists():
        courseware_route_text = read_text(COURSEWARE_ROUTE)
        for required_text in ("Teaching Plan", "Storyboard Review", "40 页主干 storyboard 审核表", "studentAction", "storyboardMetrics", "teachingPlanSource"):
            if required_text not in courseware_route_text:
                issues.append(Issue("MISSING_COURSEWARE_ROUTE", COURSEWARE_ROUTE, f"Courseware route should expose {required_text}"))
    if COURSEBOOK_INDEX.exists():
        index_text = read_text(COURSEBOOK_INDEX)
        for required_text in ("在线教材目录", "教材与课件分工", "textbookChapters", "coursewareWeeks", "/courseware", "docs/course_status_dictionary.md", "/coursebook/logical-v2", "logical v2"):
            if required_text not in index_text:
                issues.append(Issue("MISSING_COURSEBOOK_INDEX", COURSEBOOK_INDEX, f"Coursebook index should explain {required_text}"))
    if LOGICAL_V2_INDEX.exists():
        index_text = read_text(LOGICAL_V2_INDEX)
        for required_text in ("教材 v2 逻辑章节审查入口", "logicalV2Chapters", "review_ready", "source_mapped", "不替换 18 周"):
            if required_text not in index_text:
                issues.append(Issue("MISSING_LOGICAL_V2_INDEX", LOGICAL_V2_INDEX, f"Logical v2 index should expose {required_text}"))
    if LOGICAL_V2_ROUTE.exists():
        route_text = read_text(LOGICAL_V2_ROUTE)
        for required_text in ("logicalV2ReviewChapters", "教材正文", "来源映射", "学习证据", "审查状态", "Courseware 审核台"):
            if required_text not in route_text:
                issues.append(Issue("MISSING_LOGICAL_V2_ROUTE", LOGICAL_V2_ROUTE, f"Logical v2 route should expose {required_text}"))
    if WEEK_ROUTE.exists():
        week_route_text = read_text(WEEK_ROUTE)
        if "getCoursebookChapterByWeek" not in week_route_text or "/coursebook/" not in week_route_text:
            issues.append(Issue("MISSING_WEEK_BACKLINK", WEEK_ROUTE, "Week pages must link back to Coursebook chapter pages"))
        if "/courseware/" not in week_route_text:
            issues.append(Issue("MISSING_COURSEWARE_BACKLINK", WEEK_ROUTE, "Week pages should link to Courseware teaching-plan pages"))
    return issues


def run_check(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    for relative_path in (*REQUIRED_SUPPORT_FILES, *REQUIRED_TRIAL_READY_PACKS):
        candidate = root / relative_path
        if not candidate.exists():
            issues.append(Issue("MISSING_SUPPORT_FILE", candidate, f"Required support file is missing: {relative_path}"))
    return [*issues, *check_map(root), *check_logical_v2_map(root), *check_site_data(root), *check_routes(), *check_course_week_files(root)]


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: online Coursebook map, chapter routes, source paths, and section coverage are current.")
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
