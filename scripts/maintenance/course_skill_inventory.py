"""Check AI_Course project-local and global skill inventory."""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import zipfile
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[2]

GLOBAL_SKILLS = (
    "building-llm-wiki",
    "academic-chinese-style",
    "scientific-critical-thinking",
    "peer-review",
    "scientific-writing",
    "scientific-slides",
    "scientific-visualization",
    "statistical-analysis",
    "markdown-mermaid-writing",
    "academic-presentation-teaching",
    "biomedical-research-framework",
    "office-academic-skill",
    "research-writing-skill",
)

PROJECT_COURSE_SKILLS = (
    "course-skill-router",
    "course-lecture-expand",
    "course-ppt-storyboard",
    "course-evidence-review",
    "course-update-vault",
)

MANIFEST = Path("docs/skill_loading_manifest_2026-06-03.md")
README = Path("skills/README.md")
SKILLS_ZIP = Path("skills.zip")
SKILLS_ZIP_REPORT = Path("docs/skills_zip_install_report_2026-06-05.md")


class Issue(NamedTuple):
    code: str
    path: Path
    message: str


def default_codex_skills_root() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home) / "skills"
    return Path.home() / ".codex" / "skills"


def local_skill_dirs(root: Path) -> list[Path]:
    skills_root = root / "skills"
    if not skills_root.exists():
        return []
    return sorted(path for path in skills_root.iterdir() if path.is_dir())


def declared_skill_count(readme_text: str) -> int | None:
    match = re.search(r"本目录包含\s+\*\*(\d+)\s+个", readme_text)
    if match:
        return int(match.group(1))
    match = re.search(r"包含\s+(\d+)\s+个", readme_text)
    if match:
        return int(match.group(1))
    return None


def check_local_skills(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in local_skill_dirs(root):
        if not (path / "SKILL.md").is_file():
            issues.append(Issue("MISSING_LOCAL_SKILL_MD", path, "Local skill folder lacks SKILL.md"))
    for name in PROJECT_COURSE_SKILLS:
        path = root / "skills" / name
        if not (path / "SKILL.md").is_file():
            issues.append(Issue("MISSING_PROJECT_COURSE_SKILL", path, "Required course workflow skill is missing"))
    return issues


def check_global_skills(global_root: Path) -> list[Issue]:
    return [
        Issue("MISSING_GLOBAL_SKILL", global_root / name, "Required global whitelist skill is missing")
        for name in GLOBAL_SKILLS
        if not (global_root / name / "SKILL.md").is_file()
    ]


def check_readme_count(root: Path) -> list[Issue]:
    readme = root / README
    if not readme.is_file():
        return [Issue("MISSING_SKILLS_README", readme, "skills/README.md is missing")]
    text = readme.read_text(encoding="utf-8", errors="replace")
    declared = declared_skill_count(text)
    actual = len(local_skill_dirs(root))
    if declared != actual:
        return [
            Issue(
                "STALE_SKILLS_README_COUNT",
                readme,
                f"README declares {declared!r} skills but skills/ contains {actual}",
            )
        ]
    return []


def check_manifest(root: Path) -> list[Issue]:
    path = root / MANIFEST
    if not path.is_file():
        return [Issue("MISSING_SKILL_MANIFEST", path, "Global/local skill loading manifest is missing")]
    text = path.read_text(encoding="utf-8", errors="replace")
    missing = [name for name in (*GLOBAL_SKILLS, *PROJECT_COURSE_SKILLS) if name not in text]
    if missing:
        return [Issue("INCOMPLETE_SKILL_MANIFEST", path, "Manifest missing entries: " + ", ".join(missing))]
    return []


def is_ignored_zip_entry(name: str) -> bool:
    parts = name.replace("\\", "/").split("/")
    return "__pycache__" in parts or name.endswith(".pyc") or name.endswith("/")


def zip_skill_names(zip_path: Path) -> list[str]:
    names: set[str] = set()
    with open_skills_zip(zip_path) as archive:
        for name in archive.namelist():
            parts = name.replace("\\", "/").split("/")
            if len(parts) >= 3 and parts[0] == "skills" and parts[1]:
                names.add(parts[1])
    return sorted(names)


def open_skills_zip(zip_path: Path) -> zipfile.ZipFile:
    try:
        return zipfile.ZipFile(zip_path, metadata_encoding="utf-8")
    except TypeError:
        return zipfile.ZipFile(zip_path)


def hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check_skills_zip_install(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    zip_path = root / SKILLS_ZIP
    if not zip_path.exists():
        return issues
    if not (root / SKILLS_ZIP_REPORT).is_file():
        issues.append(Issue("MISSING_SKILLS_ZIP_REPORT", root / SKILLS_ZIP_REPORT, "skills.zip install report is missing"))
    with open_skills_zip(zip_path) as archive:
        for name in zip_skill_names(zip_path):
            if not (root / "skills" / name / "SKILL.md").is_file():
                issues.append(Issue("MISSING_ZIP_SKILL", root / "skills" / name, "Skill directory from skills.zip is not installed locally"))
        for entry in archive.infolist():
            name = entry.filename.replace("\\", "/")
            if name == "skills/README.md":
                continue
            if not name.startswith("skills/") or is_ignored_zip_entry(name):
                continue
            local_path = root / Path(*name.split("/"))
            if not local_path.exists():
                issues.append(Issue("MISSING_ZIP_SKILL_FILE", local_path, "Non-cache file from skills.zip is missing locally"))
                continue
            with archive.open(entry) as stream:
                zip_hash = hash_bytes(stream.read())
            local_hash = hash_bytes(local_path.read_bytes())
            if zip_hash != local_hash:
                issues.append(Issue("ZIP_SKILL_FILE_DIFFERS", local_path, "Local skill file differs from skills.zip; do not overwrite without review"))
    return issues


def run_check(root: Path = ROOT, global_root: Path | None = None) -> list[Issue]:
    root = root.resolve()
    global_root = (global_root or default_codex_skills_root()).resolve()
    issues = check_local_skills(root)
    issues.extend(check_global_skills(global_root))
    issues.extend(check_readme_count(root))
    issues.extend(check_manifest(root))
    issues.extend(check_skills_zip_install(root))
    return issues


def print_issues(root: Path, issues: list[Issue]) -> None:
    if not issues:
        print("OK: project-local and global skill inventory is current.")
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
    parser.add_argument("--check", action="store_true", help="Check local and global skill inventory.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Project root for tests or alternate workspaces.")
    parser.add_argument(
        "--global-skills-root",
        type=Path,
        default=None,
        help="Override global Codex skills root for tests or alternate installs.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.check:
        parser.error("Choose --check")
    root = args.root.resolve()
    issues = run_check(root, args.global_skills_root)
    print_issues(root, issues)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
