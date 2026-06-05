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


def test_parse_map_reads_12_coursebook_chapters():
    module = load_module()
    chapters = module.parse_map(ROOT / "course" / "textbook" / "logical_v2" / "coursebook_map.yml")
    assert len(chapters) == 12
    assert [chapter["chapter"] for chapter in chapters] == list(range(1, 13))
    assert all(chapter["status"] == "coursebook_ready" for chapter in chapters)
    assert all(chapter["page"] == f"/coursebook/chapter-{chapter['chapter']:02d}" for chapter in chapters)


def test_raw_reference_helper_accepts_markdown_sources():
    module = load_module()
    assert module.has_forbidden_raw_reference("materials/raw/source.pdf")
    assert module.has_forbidden_raw_reference(r"materials\raw\source.pdf")
    assert not module.has_forbidden_raw_reference("materials/markdown/aidd_bioinformatics/aidd.course_index.md")


def test_online_book_check_current_repo():
    module = load_module()
    assert module.run_check(ROOT) == []


def test_single_track_coursebook_routes_are_present():
    index_route = ROOT / "site" / "src" / "pages" / "coursebook.astro"
    chapter_route = ROOT / "site" / "src" / "pages" / "coursebook" / "[slug].astro"
    logical_v2_index = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2.astro"
    logical_v2_route = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2" / "[slug].astro"
    courseware_route = ROOT / "site" / "src" / "pages" / "courseware" / "[slug].astro"
    week_route = ROOT / "site" / "src" / "pages" / "weeks" / "[slug].astro"

    index_text = index_route.read_text(encoding="utf-8")
    assert "12 章目录" in index_text
    assert "coursebookChapters" in index_text
    assert "/coursebook/logical-v2" not in index_text

    chapter_text = chapter_route.read_text(encoding="utf-8")
    assert "教材正文" in chapter_text
    assert "知识图谱" in chapter_text
    assert "来源映射" in chapter_text
    assert "反向周次" in chapter_text
    assert "Missing Coursebook chapter source" in chapter_text
    assert "候选样章" not in chapter_text

    assert "http-equiv=\"refresh\"" in logical_v2_index.read_text(encoding="utf-8")
    assert "http-equiv=\"refresh\"" in logical_v2_route.read_text(encoding="utf-8")
    assert "getCoursebookChapterByWeek" in courseware_route.read_text(encoding="utf-8")
    assert "getCoursebookChapterByWeek" in week_route.read_text(encoding="utf-8")


def test_online_book_check_flags_missing_source(tmp_path):
    module = load_module()
    map_path = tmp_path / "course" / "textbook" / "logical_v2" / "coursebook_map.yml"
    map_path.parent.mkdir(parents=True)
    map_path.write_text(
        """version: 2
chapters:
  - chapter: 1
    title: Broken
    part: Broken
    core_question: Broken？
    status: coursebook_ready
    coursebook_status: coursebook_ready
    page: /coursebook/chapter-01
    chapter_source: missing.md
    chapter_focus: broken
    summary: broken
    knowledge_graph: missing_graph.mmd
    knowledge_map_image: /assets/coursebook/knowledge-maps/chapter-01.svg
    source_weeks:
      - course/weeks/week_01
    source_chapters:
      - missing_chapter.md
    knowledge_sources:
      - missing_knowledge.md
    material_sources:
      - missing_material.md
    asset_sources:
      - missing_asset.csv
    learning_evidence:
      - broken evidence
""",
        encoding="utf-8",
    )
    old_map_path = module.LOGICAL_V2_MAP_PATH
    try:
        module.LOGICAL_V2_MAP_PATH = map_path
        issues = module.check_logical_v2_map(tmp_path)
    finally:
        module.LOGICAL_V2_MAP_PATH = old_map_path
    assert any(issue.code == "MISSING_SOURCE_PATH" for issue in issues)
