from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_online_book_check.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_online_book_check", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_parse_map_reads_all_chapters():
    module = load_module()
    chapters = module.parse_map(ROOT / "course" / "textbook" / "coursebook_map.yml")
    assert len(chapters) == 18
    assert {chapter["week"] for chapter in chapters} == set(range(1, 19))


def test_required_term_helper_reports_missing_terms():
    module = load_module()
    assert module.contains_required_terms("PCA UMAP 样章候选", ("PCA", "UMAP", "spatial matrix")) == ["spatial matrix"]


def test_raw_reference_helper_accepts_slash_and_backslash_paths():
    module = load_module()
    assert module.has_forbidden_raw_reference("materials/raw/source.pdf")
    assert module.has_forbidden_raw_reference(r"materials\raw\source.pdf")
    assert not module.has_forbidden_raw_reference("materials/markdown/aidd_bioinformatics/aidd.course_index.md")


def test_online_book_check_current_repo():
    module = load_module()
    assert module.run_check(ROOT) == []


def test_full_week_pilot_candidate_statuses_are_enforced():
    module = load_module()
    chapters = module.parse_map(ROOT / "course" / "textbook" / "coursebook_map.yml")
    assert all(chapter["review_status"] in module.MINIMUM_REVIEW_STATUSES for chapter in chapters)
    for week in range(1, 19):
        week_dir = ROOT / "course" / "weeks" / f"week_{week:02d}"
        for name in ("materials.md", "outline.md"):
            text = (week_dir / name).read_text(encoding="utf-8")
            assert any(f"status: {status}" in text for status in module.MINIMUM_WEEK_FILE_STATUSES)


def test_online_book_check_flags_missing_source(tmp_path):
    module = load_module()
    map_path = tmp_path / "course" / "textbook" / "coursebook_map.yml"
    map_path.parent.mkdir(parents=True)
    map_path.write_text(
        """version: 1
chapters:
  - chapter: 1
    week: 1
    title: Broken
    page: /coursebook#week-01
    source_week_files:
      - course/weeks/week_01/materials.md
    knowledge_sources:
      - missing.md
    material_sources:
      - course/syllabus/source.md
    ppt_status: not_started
    review_status: catalog_only
""",
        encoding="utf-8",
    )
    old_map_path = module.MAP_PATH
    try:
        module.MAP_PATH = map_path
        issues = module.check_map(tmp_path)
    finally:
        module.MAP_PATH = old_map_path
    assert any(issue.code == "MISSING_SOURCE_PATH" for issue in issues)
