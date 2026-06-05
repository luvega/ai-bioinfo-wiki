"""Check expanded 40-page mainline PPT storyboards for all course weeks."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]
COURSE_WEEKS = ROOT / "course" / "weeks"
TEXTBOOK = ROOT / "course" / "textbook"

EXPECTED_HEADERS = (
    "Slide",
    "Module",
    "Action title",
    "Core content",
    "Visual intent",
    "Data/code asset",
    "Teacher explanation",
    "Student action",
    "Timing",
    "Textbook section link",
    "Evidence/source note",
    "Risk/boundary note",
)
EXPECTED_EXCLUDES = {"practice_pages", "answer_pages", "review_pages", "backup_pages"}
FORBIDDEN_MODULE_TERMS = ("练习页", "参考答案页", "复盘页", "备用页", "拓展页")
REQUIRED_ROW_FIELDS = ("Core content", "Teacher explanation", "Student action", "Timing", "Evidence/source note", "Risk/boundary note")
STRICT_REVIEW_WEEKS = {3, 5, 8, 11, 12, 13, 15, 16, 18}
OBSERVABLE_ACTION_TERMS = ("标出", "计算", "比较", "运行", "检查", "改写", "判断", "说出", "写出", "列出", "圈出", "标注", "补写", "读出", "打开", "查看")
GENERIC_EVIDENCE_NOTES = {"课程材料", "教材", "来源", "脚本", "知识支持层", "待核验"}
EXPECTED_TEACHING_PLAN_BLOCKS = {
    "课程定位与导入": ("8 min", "1-4"),
    "核心概念展开": ("16 min", "5-12"),
    "数据结构与案例": ("20 min", "13-20"),
    "方法流程与代码": ("24 min", "21-30"),
    "图表与结果解释": ("14 min", "31-36"),
    "AI 协作与核验收束": ("8 min", "37-40"),
}


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


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\n(.*?)\n---", text, flags=re.S)
    return match.group(1) if match else ""


def frontmatter_scalar(fm: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", fm, flags=re.M)
    return match.group(1).strip().strip("'\"") if match else ""


def frontmatter_inline_list(fm: str, key: str) -> list[str]:
    value = frontmatter_scalar(fm, key)
    if not value.startswith("[") or not value.endswith("]"):
        return []
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [part.strip().strip("'\"") for part in inner.split(",")]


def has_forbidden_reference(text: str) -> bool:
    normalized = text.replace("\\", "/")
    return "materials/raw" in normalized or "[[" in text or "]]" in text


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def table_headers(text: str) -> list[str]:
    for line in text.splitlines():
        cells = split_row(line)
        if cells and cells[0] == "Slide":
            return cells
    return []


def table_rows(text: str) -> list[dict[str, str]]:
    headers = table_headers(text)
    rows: list[dict[str, str]] = []
    if not headers:
        return rows
    for line in text.splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        cells = split_row(line)
        if len(cells) != len(headers):
            rows.append({"__bad_row__": line})
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def generic_table_headers(text: str, first_header: str) -> list[str]:
    for line in text.splitlines():
        cells = split_row(line)
        if cells and cells[0] == first_header:
            return cells
    return []


def generic_table_rows(text: str, first_header: str, first_column_values: set[str]) -> list[dict[str, str]]:
    headers = generic_table_headers(text, first_header)
    rows: list[dict[str, str]] = []
    if not headers:
        return rows
    for line in text.splitlines():
        cells = split_row(line)
        if not cells or cells[0] not in first_column_values:
            continue
        if len(cells) != len(headers):
            rows.append({"__bad_row__": line})
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def teaching_plan_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    return generic_table_rows(read_text(path), "Block", set(EXPECTED_TEACHING_PLAN_BLOCKS))


def timing_minutes(value: str) -> int | None:
    match = re.match(r"^\s*(\d+)\s*min\s*$", value)
    return int(match.group(1)) if match else None


def check_storyboard(root: Path, week: int) -> list[Issue]:
    path = root / "course" / "weeks" / f"week_{week:02d}" / "ppt_storyboard.md"
    teaching_plan_path = root / "course" / "weeks" / f"week_{week:02d}" / "teaching_plan.md"
    issues: list[Issue] = []
    if not path.exists():
        return [Issue("MISSING_STORYBOARD", path, f"Week {week:02d} ppt_storyboard.md is missing")]

    text = read_text(path)
    fm = frontmatter(text)
    rows = table_rows(text)
    headers = table_headers(text)

    if has_forbidden_reference(text):
        issues.append(Issue("FORBIDDEN_REFERENCE", path, "Storyboard must not reference raw paths or Obsidian links"))
    if headers != list(EXPECTED_HEADERS):
        issues.append(Issue("BAD_STORYBOARD_HEADER", path, f"Expected headers {EXPECTED_HEADERS}, found {headers or 'missing'}"))
    if len(rows) != 40:
        issues.append(Issue("BAD_STORYBOARD_ROW_COUNT", path, f"Expected 40 slide rows, found {len(rows)}"))
    if any("__bad_row__" in row for row in rows):
        issues.append(Issue("BAD_STORYBOARD_ROW_SHAPE", path, "One or more storyboard rows do not match the header shape"))

    expected_frontmatter = {
        "type": "course-ppt-storyboard",
        "ppt_status": "storyboard_expanded",
        "storyboard_kind": "mainline_source",
        "target_pages": "40",
    }
    for key, expected in expected_frontmatter.items():
        found = frontmatter_scalar(fm, key)
        if found != expected:
            issues.append(Issue("BAD_STORYBOARD_FRONTMATTER", path, f"{key} should be {expected}, found {found or 'missing'}"))
    if frontmatter_scalar(fm, "week") != str(week):
        issues.append(Issue("BAD_STORYBOARD_WEEK", path, f"week should be {week}"))
    excludes = set(frontmatter_inline_list(fm, "excludes"))
    if excludes != EXPECTED_EXCLUDES:
        issues.append(Issue("BAD_STORYBOARD_EXCLUDES", path, f"excludes should be {sorted(EXPECTED_EXCLUDES)}, found {sorted(excludes)}"))
    sources = frontmatter_inline_list(fm, "source")
    expected_chapter = f"course/textbook/chapters/chapter_{week:02d}.md"
    if expected_chapter not in sources:
        issues.append(Issue("MISSING_STORYBOARD_CHAPTER_SOURCE", path, f"source should include {expected_chapter}"))
    if "teaching_plan.md" not in sources:
        issues.append(Issue("MISSING_TEACHING_PLAN_SOURCE", path, "source should include teaching_plan.md"))
    plan_rows = teaching_plan_rows(teaching_plan_path)
    if not plan_rows:
        issues.append(Issue("MISSING_TEACHING_PLAN_LINK", path, "Storyboard should be backed by a readable teaching_plan.md"))

    data_or_code_rows = 0
    chart_rows = 0
    ai_rows = 0
    action_titles: list[str] = []
    teacher_notes: list[str] = []
    short_rows = 0
    generic_evidence_rows = 0
    timing_total = 0
    module_timing: dict[str, int] = {}
    module_slides: dict[str, list[int]] = {}
    for row in rows:
        if "__bad_row__" in row:
            continue
        action_titles.append(row.get("Action title", ""))
        teacher_notes.append(row.get("Teacher explanation", ""))
        for field in REQUIRED_ROW_FIELDS:
            if not row.get(field):
                issues.append(Issue("EMPTY_STORYBOARD_FIELD", path, f"Slide {row.get('Slide', '?')} has empty {field}"))
        student_action = row.get("Student action", "")
        if student_action and not any(term in student_action for term in OBSERVABLE_ACTION_TERMS):
            issues.append(Issue("NON_OBSERVABLE_STUDENT_ACTION", path, f"Slide {row.get('Slide', '?')} Student action should use an observable verb"))
        minutes = timing_minutes(row.get("Timing", ""))
        if minutes is None:
            issues.append(Issue("BAD_TIMING_FORMAT", path, f"Slide {row.get('Slide', '?')} Timing should use '<int> min'"))
        else:
            timing_total += minutes
            module = row.get("Module", "")
            module_timing[module] = module_timing.get(module, 0) + minutes
            slide_number = row.get("Slide", "")
            if slide_number.isdigit():
                module_slides.setdefault(module, []).append(int(slide_number))
        module_title = f"{row.get('Module', '')} {row.get('Action title', '')}"
        if any(term in module_title for term in FORBIDDEN_MODULE_TERMS):
            issues.append(Issue("FORBIDDEN_PAGE_MODULE", path, f"Slide {row.get('Slide', '?')} appears to be a deferred page type"))
        asset = row.get("Data/code asset", "")
        if "course/textbook/assets/datasets/" in asset or "course/textbook/assets/code/" in asset:
            data_or_code_rows += 1
        visual = row.get("Visual intent", "")
        core = row.get("Core content", "")
        if any(term in f"{visual} {core}" for term in ("图", "表", "结果", "图注", "visual", "matrix", "UMAP", "plot")):
            chart_rows += 1
        combined = " ".join(row.values())
        if any(term in combined for term in ("AI", "Prompt", "证据边界", "Claim-Evidence", "人工核验")):
            ai_rows += 1
        required_text = " ".join(row.get(field, "") for field in ("Core content", "Teacher explanation", "Student action", "Evidence/source note", "Risk/boundary note"))
        if len(required_text) < 120:
            short_rows += 1
        evidence = row.get("Evidence/source note", "").strip()
        if evidence in GENERIC_EVIDENCE_NOTES or ("/" not in evidence and "\\" not in evidence and "." not in evidence):
            generic_evidence_rows += 1

    if data_or_code_rows < 8:
        issues.append(Issue("LOW_DATA_CODE_COVERAGE", path, f"Expected at least 8 data/code rows, found {data_or_code_rows}"))
    if chart_rows < 6:
        issues.append(Issue("LOW_CHART_RESULT_COVERAGE", path, f"Expected at least 6 chart/result rows, found {chart_rows}"))
    if ai_rows < 4:
        issues.append(Issue("LOW_AI_BOUNDARY_COVERAGE", path, f"Expected at least 4 AI/boundary rows, found {ai_rows}"))
    if timing_total != 90:
        issues.append(Issue("BAD_TIMING_TOTAL", path, f"Expected Timing total to be 90 min, found {timing_total} min"))
    if plan_rows:
        plan_blocks = {row.get("Block", ""): row for row in plan_rows if "__bad_row__" not in row}
        for module, (expected_minutes, expected_slide_range) in EXPECTED_TEACHING_PLAN_BLOCKS.items():
            plan = plan_blocks.get(module)
            if not plan:
                issues.append(Issue("MISSING_TEACHING_PLAN_MODULE", teaching_plan_path, f"Teaching plan missing block {module}"))
                continue
            if plan.get("Minutes") != expected_minutes or plan.get("Storyboard slides") != expected_slide_range:
                issues.append(Issue("BAD_TEACHING_PLAN_MODULE", teaching_plan_path, f"{module} should be {expected_minutes} and slides {expected_slide_range}"))
            plan_minutes = timing_minutes(plan.get("Minutes", ""))
            if plan_minutes is not None and module_timing.get(module, 0) != plan_minutes:
                issues.append(Issue("STORYBOARD_PLAN_TIMING_MISMATCH", path, f"{module} storyboard timing {module_timing.get(module, 0)} min does not match teaching plan {plan_minutes} min"))
        unknown_modules = set(module_timing) - set(EXPECTED_TEACHING_PLAN_BLOCKS)
        for module in sorted(unknown_modules):
            issues.append(Issue("UNKNOWN_STORYBOARD_MODULE", path, f"Storyboard module is not in teaching plan: {module}"))
    if week in STRICT_REVIEW_WEEKS:
        duplicate_titles = len(action_titles) - len(set(action_titles))
        if duplicate_titles:
            issues.append(Issue("DUPLICATE_ACTION_TITLES", path, f"Strict review weeks should not repeat Action title, found {duplicate_titles} duplicates"))
        max_teacher_repeat = max((teacher_notes.count(note) for note in set(teacher_notes)), default=0)
        if max_teacher_repeat > 3:
            issues.append(Issue("REPEATED_TEACHER_EXPLANATION", path, f"Teacher explanation repeats too often: max {max_teacher_repeat}"))
        if short_rows:
            issues.append(Issue("SHORT_STORYBOARD_ROWS", path, f"Strict review weeks should not have short rows, found {short_rows}"))
        if generic_evidence_rows > 2:
            issues.append(Issue("GENERIC_EVIDENCE_NOTES", path, f"Strict review weeks should not use generic evidence notes, found {generic_evidence_rows}"))

    return issues


def run_check(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    for week in range(1, 19):
        issues.extend(check_storyboard(root, week))
    return issues


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: 18 expanded mainline PPT storyboards are current.")
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
