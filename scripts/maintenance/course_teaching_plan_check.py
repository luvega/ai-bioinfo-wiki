"""Check weekly 90-minute teaching plans for the dual-track courseware model."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]
COURSE_WEEKS = ROOT / "course" / "weeks"

EXPECTED_HEADERS = (
    "Block",
    "Minutes",
    "Storyboard slides",
    "Teaching focus",
    "Teacher activity",
    "Student action",
    "Classroom product",
    "Assessment evidence",
    "Materials",
)
EXPECTED_BLOCKS = (
    ("课程定位与导入", "8 min", "1-4"),
    ("核心概念展开", "16 min", "5-12"),
    ("数据结构与案例", "20 min", "13-20"),
    ("方法流程与代码", "24 min", "21-30"),
    ("图表与结果解释", "14 min", "31-36"),
    ("AI 协作与核验收束", "8 min", "37-40"),
)
OBSERVABLE_ACTION_TERMS = (
    "标出",
    "计算",
    "比较",
    "运行",
    "检查",
    "改写",
    "判断",
    "说出",
    "写出",
    "列出",
    "圈出",
    "标注",
    "补写",
    "读出",
    "打开",
    "查看",
    "完成",
)
REQUIRED_SECTIONS = (
    "## 本周定位",
    "## 学习目标",
    "## 90 分钟时间切分",
    "## 课堂产物与评价证据",
    "## 所需素材",
    "## AI 协作边界",
    "## 与教材和 storyboard 的关系",
    "## 来源与待核验点",
)


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


def has_forbidden_reference(text: str) -> bool:
    normalized = text.replace("\\", "/")
    return "materials/raw" in normalized or "[[" in text or "]]" in text


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def table_headers(text: str) -> list[str]:
    for line in text.splitlines():
        cells = split_row(line)
        if cells and cells[0] == "Block":
            return cells
    return []


def table_rows(text: str) -> list[dict[str, str]]:
    headers = table_headers(text)
    rows: list[dict[str, str]] = []
    if not headers:
        return rows
    for line in text.splitlines():
        cells = split_row(line)
        if not cells or cells[0] not in {block for block, _minutes, _slides in EXPECTED_BLOCKS}:
            continue
        if len(cells) != len(headers):
            rows.append({"__bad_row__": line})
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def timing_minutes(value: str) -> int | None:
    match = re.match(r"^\s*(\d+)\s*min\s*$", value)
    return int(match.group(1)) if match else None


def source_paths(text: str) -> list[str]:
    return re.findall(r"`([^`]+)`", text)


def check_teaching_plan(root: Path, week: int) -> list[Issue]:
    path = root / "course" / "weeks" / f"week_{week:02d}" / "teaching_plan.md"
    issues: list[Issue] = []
    if not path.exists():
        return [Issue("MISSING_TEACHING_PLAN", path, f"Week {week:02d} teaching_plan.md is missing")]

    text = read_text(path)
    fm = frontmatter(text)
    rows = table_rows(text)
    headers = table_headers(text)

    if has_forbidden_reference(text):
        issues.append(Issue("FORBIDDEN_REFERENCE", path, "Teaching plan must not reference raw paths or Obsidian links"))
    for section in REQUIRED_SECTIONS:
        if section not in text:
            issues.append(Issue("MISSING_TEACHING_PLAN_SECTION", path, f"Missing required section: {section}"))
    if headers != list(EXPECTED_HEADERS):
        issues.append(Issue("BAD_TEACHING_PLAN_HEADER", path, f"Expected headers {EXPECTED_HEADERS}, found {headers or 'missing'}"))
    if len(rows) != len(EXPECTED_BLOCKS):
        issues.append(Issue("BAD_TEACHING_PLAN_BLOCK_COUNT", path, f"Expected {len(EXPECTED_BLOCKS)} blocks, found {len(rows)}"))
    if any("__bad_row__" in row for row in rows):
        issues.append(Issue("BAD_TEACHING_PLAN_ROW_SHAPE", path, "One or more teaching-plan rows do not match the header shape"))

    expected_frontmatter = {
        "type": "course-teaching-plan",
        "duration_minutes": "90",
        "teaching_plan_status": "teaching_plan_ready",
        "storyboard_source": f"course/weeks/week_{week:02d}/ppt_storyboard.md",
        "chapter_source": f"course/textbook/chapters/chapter_{week:02d}.md",
    }
    for key, expected in expected_frontmatter.items():
        found = frontmatter_scalar(fm, key)
        if found != expected:
            issues.append(Issue("BAD_TEACHING_PLAN_FRONTMATTER", path, f"{key} should be {expected}, found {found or 'missing'}"))
    if frontmatter_scalar(fm, "week") != str(week):
        issues.append(Issue("BAD_TEACHING_PLAN_WEEK", path, f"week should be {week}"))

    total = 0
    expected_by_block = {block: (minutes, slides) for block, minutes, slides in EXPECTED_BLOCKS}
    seen_blocks: list[str] = []
    for row in rows:
        if "__bad_row__" in row:
            continue
        block = row.get("Block", "")
        seen_blocks.append(block)
        expected = expected_by_block.get(block)
        if expected is None:
            issues.append(Issue("UNKNOWN_TEACHING_PLAN_BLOCK", path, f"Unknown block: {block}"))
            continue
        expected_minutes, expected_slides = expected
        if row.get("Minutes") != expected_minutes:
            issues.append(Issue("BAD_BLOCK_MINUTES", path, f"{block} should be {expected_minutes}, found {row.get('Minutes', 'missing')}"))
        if row.get("Storyboard slides") != expected_slides:
            issues.append(Issue("BAD_BLOCK_SLIDES", path, f"{block} should map to slides {expected_slides}"))
        minutes = timing_minutes(row.get("Minutes", ""))
        if minutes is None:
            issues.append(Issue("BAD_MINUTES_FORMAT", path, f"{block} Minutes should use '<int> min'"))
        else:
            total += minutes
        for field in ("Teaching focus", "Teacher activity", "Student action", "Classroom product", "Assessment evidence", "Materials"):
            if not row.get(field):
                issues.append(Issue("EMPTY_TEACHING_PLAN_FIELD", path, f"{block} has empty {field}"))
        student_action = row.get("Student action", "")
        if student_action and not any(term in student_action for term in OBSERVABLE_ACTION_TERMS):
            issues.append(Issue("NON_OBSERVABLE_STUDENT_ACTION", path, f"{block} Student action should use an observable verb"))
        material = row.get("Materials", "")
        if material and not (root / material).exists():
            issues.append(Issue("MISSING_TEACHING_PLAN_MATERIAL", path, f"Material path does not exist: {material}"))
    if seen_blocks != [block for block, _minutes, _slides in EXPECTED_BLOCKS]:
        issues.append(Issue("BAD_TEACHING_PLAN_BLOCK_ORDER", path, "Teaching-plan blocks must follow the fixed 90-minute sequence"))
    if total != 90:
        issues.append(Issue("BAD_TEACHING_PLAN_TOTAL", path, f"Expected 90 min total, found {total} min"))

    for source in source_paths(text):
        if source.startswith(("course/", "knowledge/", "materials/", "scripts/", "docs/")) and not (root / source).exists():
            issues.append(Issue("MISSING_REFERENCED_SOURCE", path, f"Referenced source does not exist: {source}"))
    return issues


def run_check(root: Path = ROOT) -> list[Issue]:
    issues: list[Issue] = []
    for week in range(1, 19):
        issues.extend(check_teaching_plan(root, week))
    return issues


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: 18 weekly teaching plans are current.")
        return
    for issue in issues:
        print(f"{issue.code}: {rel(issue.path, root)}: {issue.message}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    issues = run_check(root)
    print_issues(root, issues)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
