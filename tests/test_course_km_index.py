from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_km_index.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_km_index", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_root_is_derived_from_script_location():
    module = load_module()
    assert module.ROOT == ROOT


def test_week_index_contains_all_weeks_and_current_week_11_15_topics():
    module = load_module()
    content = module.build_weeks_index(ROOT)
    assert content.count("| [week_") == 18
    assert "[week_11](week_11/)" in content
    assert "科研图表规范与 SCI 图表表达" in content
    assert "[week_15](week_15/)" in content
    assert "差异表达分析与功能解读" in content


def test_markdown_link_checker_flags_missing_standard_links(tmp_path):
    module = load_module()
    note = tmp_path / "note.md"
    note.write_text("[missing](missing.md)\n[external](https://example.com)\n", encoding="utf-8")
    issues = module.find_broken_links(tmp_path, [note])
    assert len(issues) == 1
    assert "missing.md" in issues[0].message


def test_stale_week_mapping_check_accepts_current_course_mainline():
    module = load_module()
    issues = module.check_week_topic_alignment(ROOT)
    assert not issues
