from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_ppt_storyboard_check.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_ppt_storyboard_check", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_storyboard_check_current_repo():
    module = load_module()
    assert module.run_check(ROOT) == []


def test_all_storyboards_have_40_mainline_rows():
    module = load_module()
    for week in range(1, 19):
        path = ROOT / "course" / "weeks" / f"week_{week:02d}" / "ppt_storyboard.md"
        text = path.read_text(encoding="utf-8")
        rows = module.table_rows(text)
        assert len(rows) == 40
        assert module.table_headers(text) == list(module.EXPECTED_HEADERS)
        assert "Student action" in module.table_headers(text)
        assert "Timing" in module.table_headers(text)
        fm = module.frontmatter(text)
        assert module.frontmatter_scalar(fm, "ppt_status") == "storyboard_expanded"
        assert module.frontmatter_scalar(fm, "storyboard_kind") == "mainline_source"
        assert module.frontmatter_scalar(fm, "target_pages") == "40"
        assert set(module.frontmatter_inline_list(fm, "excludes")) == module.EXPECTED_EXCLUDES


def test_storyboard_rows_keep_required_fields_and_coverage():
    module = load_module()
    for week in range(1, 19):
        path = ROOT / "course" / "weeks" / f"week_{week:02d}" / "ppt_storyboard.md"
        rows = module.table_rows(path.read_text(encoding="utf-8"))
        assert sum("course/textbook/assets/datasets/" in row["Data/code asset"] or "course/textbook/assets/code/" in row["Data/code asset"] for row in rows) >= 8
        assert sum(any(term in f"{row['Visual intent']} {row['Core content']}" for term in ("图", "表", "结果", "图注", "matrix", "UMAP", "plot")) for row in rows) >= 6
        assert sum(any(term in " ".join(row.values()) for term in ("AI", "Prompt", "证据边界", "Claim-Evidence", "人工核验")) for row in rows) >= 4
        assert sum(module.timing_minutes(row["Timing"]) or 0 for row in rows) == 90
        for row in rows:
            for field in module.REQUIRED_ROW_FIELDS:
                assert row[field]
            assert any(term in row["Student action"] for term in module.OBSERVABLE_ACTION_TERMS)
            assert not any(term in f"{row['Module']} {row['Action title']}" for term in module.FORBIDDEN_MODULE_TERMS)


def test_strict_review_weeks_are_de_template_checked():
    module = load_module()
    for week in module.STRICT_REVIEW_WEEKS:
        path = ROOT / "course" / "weeks" / f"week_{week:02d}" / "ppt_storyboard.md"
        rows = module.table_rows(path.read_text(encoding="utf-8"))
        action_titles = [row["Action title"] for row in rows]
        teacher_notes = [row["Teacher explanation"] for row in rows]
        assert len(action_titles) == len(set(action_titles))
        assert max(teacher_notes.count(note) for note in set(teacher_notes)) <= 3


def test_forbidden_reference_helper():
    module = load_module()
    assert module.has_forbidden_reference("materials/raw/private.pdf")
    assert module.has_forbidden_reference("[[old link]]")
    assert not module.has_forbidden_reference("course/textbook/assets/datasets/week01.csv")
