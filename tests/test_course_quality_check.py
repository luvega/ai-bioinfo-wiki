from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_quality_check.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_quality_check", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_week(root: Path, week: int, sample: bool = False) -> None:
    folder = root / "course" / "weeks" / f"week_{week:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    if sample:
        materials = "## 素材来源\n## 可用程度\n## 待核验\n"
        outline = "## 教学目标\n## 药学问题入口\n## 核心数据结构\n## 课堂任务\n## AI协作边界\n## 课后练习\n## 待核验\n"
        script = "## 教学目标\n## 药学场景\n## 核心数据结构\n## 课堂任务\n## AI协作边界\n## 课后练习\n## 待核验\n"
    else:
        materials = "# materials\n"
        outline = "# outline\n"
        script = "# script\n"
    (folder / "materials.md").write_text(materials, encoding="utf-8")
    (folder / "outline.md").write_text(outline, encoding="utf-8")
    (folder / "script.md").write_text(script, encoding="utf-8")


def make_course(root: Path) -> None:
    for week in range(1, 19):
        make_week(root, week, sample=week in (3, 14, 15, 16))


def test_quality_check_accepts_complete_course(tmp_path):
    module = load_module()
    make_course(tmp_path)
    assert module.run_check(tmp_path) == []


def test_quality_check_flags_missing_week_file(tmp_path):
    module = load_module()
    make_course(tmp_path)
    (tmp_path / "course" / "weeks" / "week_03" / "script.md").unlink()
    issues = module.run_check(tmp_path)
    assert any(issue.code == "MISSING_WEEK_FILE" for issue in issues)


def test_quality_check_flags_missing_sample_marker(tmp_path):
    module = load_module()
    make_course(tmp_path)
    path = tmp_path / "course" / "weeks" / "week_15" / "outline.md"
    path.write_text("## 教学目标\n", encoding="utf-8")
    issues = module.run_check(tmp_path)
    assert any(issue.code == "MISSING_SAMPLE_MARKER" for issue in issues)
