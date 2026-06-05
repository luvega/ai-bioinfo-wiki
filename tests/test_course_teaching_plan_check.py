from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_teaching_plan_check.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_teaching_plan_check", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_teaching_plan_check_current_repo():
    module = load_module()
    assert module.run_check(ROOT) == []


def test_all_weeks_have_90_minute_teaching_plans():
    module = load_module()
    for week in range(1, 19):
        path = ROOT / "course" / "weeks" / f"week_{week:02d}" / "teaching_plan.md"
        text = path.read_text(encoding="utf-8")
        fm = module.frontmatter(text)
        assert module.frontmatter_scalar(fm, "type") == "course-teaching-plan"
        assert module.frontmatter_scalar(fm, "duration_minutes") == "90"
        assert module.frontmatter_scalar(fm, "teaching_plan_status") == "teaching_plan_ready"
        assert module.frontmatter_scalar(fm, "storyboard_source") == f"course/weeks/week_{week:02d}/ppt_storyboard.md"
        assert module.frontmatter_scalar(fm, "chapter_source") == f"course/textbook/chapters/chapter_{week:02d}.md"
        rows = module.table_rows(text)
        assert module.table_headers(text) == list(module.EXPECTED_HEADERS)
        assert len(rows) == 6
        assert sum(module.timing_minutes(row["Minutes"]) or 0 for row in rows) == 90
        assert [row["Block"] for row in rows] == [block for block, _minutes, _slides in module.EXPECTED_BLOCKS]


def test_teaching_plan_rows_have_student_actions_products_and_evidence():
    module = load_module()
    for week in range(1, 19):
        path = ROOT / "course" / "weeks" / f"week_{week:02d}" / "teaching_plan.md"
        rows = module.table_rows(path.read_text(encoding="utf-8"))
        for row in rows:
            assert any(term in row["Student action"] for term in module.OBSERVABLE_ACTION_TERMS)
            assert row["Classroom product"]
            assert row["Assessment evidence"]
            material_path = ROOT / row["Materials"]
            assert material_path.exists()


def test_forbidden_reference_helper():
    module = load_module()
    assert module.has_forbidden_reference("materials/raw/private.pdf")
    assert module.has_forbidden_reference("[[old link]]")
    assert not module.has_forbidden_reference("course/textbook/assets/datasets/week01.csv")
