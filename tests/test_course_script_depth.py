from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_script_depth.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_script_depth", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_root_is_derived_from_script_location():
    module = load_module()
    assert module.ROOT == ROOT


def test_depth_report_explains_status_scope():
    module = load_module()
    content = module.build_report(ROOT)
    assert "only measures `script.md` frontmatter status and CJK character depth" in content
    assert "materials.md" in content
    assert "PPT visual QA" in content
