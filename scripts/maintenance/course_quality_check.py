"""Check AI_Course week packages and sample-week quality markers."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_WEEK_FILES = ("materials.md", "outline.md", "script.md")
SAMPLE_WEEKS = ("week_03", "week_14", "week_15", "week_16")

MATERIAL_TERMS = ("素材来源", "可用程度", "待核验")
OUTLINE_TERMS = ("教学目标", "药学", "核心数据结构", "课堂任务", "AI协作边界", "课后练习", "待核验")
SCRIPT_TERMS = ("教学目标", "药学", "核心数据结构", "课堂任务", "AI协作边界", "课后练习", "待核验")


class Issue(NamedTuple):
    code: str
    path: Path
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def normalized(text: str) -> str:
    return "".join(text.split())


def contains_term(text: str, term: str) -> bool:
    return normalized(term) in normalized(text)


def check_week_files(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    weeks_root = root / "course" / "weeks"
    for week in range(1, 19):
        folder = weeks_root / f"week_{week:02d}"
        if not folder.is_dir():
            issues.append(Issue("MISSING_WEEK", folder, "Week folder is missing"))
            continue
        for file_name in REQUIRED_WEEK_FILES:
            path = folder / file_name
            if not path.is_file():
                issues.append(Issue("MISSING_WEEK_FILE", path, "Required week file is missing"))
    return issues


def check_terms(path: Path, terms: tuple[str, ...]) -> list[Issue]:
    if not path.exists():
        return []
    text = read_text(path)
    return [
        Issue("MISSING_SAMPLE_MARKER", path, f"Missing required sample-week marker: {term}")
        for term in terms
        if not contains_term(text, term)
    ]


def check_sample_weeks(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    weeks_root = root / "course" / "weeks"
    for week in SAMPLE_WEEKS:
        folder = weeks_root / week
        issues.extend(check_terms(folder / "materials.md", MATERIAL_TERMS))
        issues.extend(check_terms(folder / "outline.md", OUTLINE_TERMS))
        issues.extend(check_terms(folder / "script.md", SCRIPT_TERMS))
    return issues


def run_check(root: Path = ROOT) -> list[Issue]:
    issues = check_week_files(root)
    issues.extend(check_sample_weeks(root))
    return issues


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: week files and sample-week quality markers are present.")
        return
    root_resolved = root.resolve()
    for issue in issues:
        try:
            path = issue.path.resolve().relative_to(root_resolved).as_posix()
        except ValueError:
            path = str(issue.path)
        print(f"{issue.code}: {path}: {issue.message}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check course week package quality.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Project root for tests or alternate workspaces.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.check:
        parser.error("Choose --check")
    root = args.root.resolve()
    issues = run_check(root)
    print_issues(root, issues)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
