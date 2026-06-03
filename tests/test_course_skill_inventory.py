from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_skill_inventory.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_skill_inventory", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_skill(root: Path, name: str) -> None:
    path = root / "skills" / name
    path.mkdir(parents=True, exist_ok=True)
    (path / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")


def write_global_skill(global_root: Path, name: str) -> None:
    path = global_root / name
    path.mkdir(parents=True, exist_ok=True)
    (path / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")


def make_project(root: Path, module) -> Path:
    (root / "skills").mkdir(parents=True)
    all_local = list(module.PROJECT_COURSE_SKILLS) + ["existing-skill"]
    for name in all_local:
        write_skill(root, name)
    (root / "skills" / "README.md").write_text(f"# Skills\n\n本目录包含 **{len(all_local)} 个** skill。\n", encoding="utf-8")
    (root / "docs").mkdir()
    manifest_entries = "\n".join([*module.GLOBAL_SKILLS, *module.PROJECT_COURSE_SKILLS])
    (root / module.MANIFEST).write_text(manifest_entries, encoding="utf-8")

    global_root = root / "global_skills"
    for name in module.GLOBAL_SKILLS:
        write_global_skill(global_root, name)
    return global_root


def test_root_is_derived_from_script_location():
    module = load_module()
    assert module.ROOT == ROOT


def test_skill_inventory_accepts_complete_project(tmp_path):
    module = load_module()
    global_root = make_project(tmp_path, module)
    assert module.run_check(tmp_path, global_root) == []


def test_skill_inventory_flags_missing_project_course_skill(tmp_path):
    module = load_module()
    global_root = make_project(tmp_path, module)
    (tmp_path / "skills" / "course-evidence-review" / "SKILL.md").unlink()
    issues = module.run_check(tmp_path, global_root)
    assert any(issue.code == "MISSING_LOCAL_SKILL_MD" for issue in issues)
    assert any(issue.code == "MISSING_PROJECT_COURSE_SKILL" for issue in issues)


def test_skill_inventory_flags_stale_readme_count(tmp_path):
    module = load_module()
    global_root = make_project(tmp_path, module)
    (tmp_path / "skills" / "README.md").write_text("# Skills\n\n本目录包含 **1 个** skill。\n", encoding="utf-8")
    issues = module.run_check(tmp_path, global_root)
    assert any(issue.code == "STALE_SKILLS_README_COUNT" for issue in issues)
