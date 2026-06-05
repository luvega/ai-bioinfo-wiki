from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "maintenance" / "course_textbook_check.py"


def load_module():
    spec = importlib.util.spec_from_file_location("course_textbook_check", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_textbook_check_current_repo():
    module = load_module()
    assert module.run_check(ROOT) == []


def test_all_chapters_have_assets_and_sections():
    module = load_module()
    for week in range(1, 19):
        path = ROOT / "course" / "textbook" / "chapters" / f"chapter_{week:02d}.md"
        text = path.read_text(encoding="utf-8")
        fm = module.frontmatter(text)
        assert module.frontmatter_scalar(fm, "textbook_status") == "expanded_draft"
        assert module.frontmatter_scalar(fm, "teaching_plan_source") == f"course/weeks/week_{week:02d}/teaching_plan.md"
        assert module.frontmatter_scalar(fm, "storyboard_source") == f"course/weeks/week_{week:02d}/ppt_storyboard.md"
        assert module.frontmatter_scalar(fm, "storyboard_pages") == "40"
        assert module.chinese_count(text) >= (7000 if week in module.FOCUS_WEEKS else 5000)
        assert len(module.frontmatter_list(fm, "asset_sources")) >= 3
        for heading in module.REQUIRED_HEADINGS:
            assert heading in text
        assert "这一页属于" not in text
        assert "### Slide " not in text


def test_map_exposes_textbook_interface():
    module = load_module()
    chapters = module.parse_map(ROOT / "course" / "textbook" / "coursebook_map.yml")
    assert len(chapters) == 18
    for chapter in chapters:
        week = chapter["week"]
        assert chapter["page"] == f"/coursebook/week-{week:02d}"
        assert chapter["chapter_source"] == f"course/textbook/chapters/chapter_{week:02d}.md"
        assert chapter["textbook_status"] == "expanded_draft"
        assert chapter["teaching_plan_source"] == f"course/weeks/week_{week:02d}/teaching_plan.md"
        assert chapter["storyboard_source"] == f"course/weeks/week_{week:02d}/ppt_storyboard.md"
        assert chapter["storyboard_pages"] == 40
        assert chapter["ppt_status"] == "storyboard_expanded"
        assert len(chapter["asset_sources"]) >= 3


def test_logical_v2_map_exposes_source_mapped_structure():
    module = load_module()
    path = ROOT / "course" / "textbook" / "logical_v2" / "coursebook_map.yml"
    chapters = module.parse_map(path)
    assert len(chapters) == 12
    assert [chapter["chapter"] for chapter in chapters] == list(range(1, 13))
    for chapter in chapters:
        chapter_no = chapter["chapter"]
        if chapter_no in module.LOGICAL_V2_REVIEW_CHAPTERS:
            assert chapter["status"] == "review_ready"
            assert chapter["review_status"] == "review_ready"
            assert chapter["page"] == f"/coursebook/logical-v2/chapter-{chapter_no:02d}"
            assert chapter["chapter_source"] == f"course/textbook/logical_v2/chapters/chapter_{chapter_no:02d}.md"
            assert chapter["review_focus"]
        else:
            assert chapter["status"] == "source_mapped"
        assert chapter["core_question"].endswith("？")
        for field in module.LOGICAL_V2_REQUIRED_FIELDS:
            assert field in chapter
        for field in ("source_weeks", "source_chapters", "knowledge_sources", "material_sources", "asset_sources"):
            assert module.list_value(chapter, field)
            for value in module.list_value(chapter, field):
                assert (ROOT / value).exists(), value
        assert module.list_value(chapter, "learning_evidence")


def test_logical_v2_review_chapters_have_review_ready_body():
    module = load_module()
    for chapter_no in sorted(module.LOGICAL_V2_REVIEW_CHAPTERS):
        path = ROOT / "course" / "textbook" / "logical_v2" / "chapters" / f"chapter_{chapter_no:02d}.md"
        text = path.read_text(encoding="utf-8")
        fm = module.frontmatter(text)
        assert module.frontmatter_scalar(fm, "status") == "review_ready"
        assert module.frontmatter_scalar(fm, "review_status") == "review_ready"
        assert module.chinese_count(text) >= module.LOGICAL_V2_REVIEW_MIN_CHINESE
        for heading in module.LOGICAL_V2_REVIEW_HEADINGS:
            assert heading in text
        for field in module.LOGICAL_V2_REVIEW_FRONTMATTER_LISTS:
            assert module.frontmatter_list(fm, field)


def test_knowledge_graph_links_all_weeks():
    edges = (ROOT / "course" / "textbook" / "assets" / "knowledge_graph" / "course_graph_edges.csv").read_text(encoding="utf-8")
    graph = (ROOT / "course" / "textbook" / "assets" / "knowledge_graph" / "course_graph.mmd").read_text(encoding="utf-8")
    for week in range(1, 19):
        assert f"Week {week:02d}" in edges
        assert f"Chapter {week:02d}" in edges
        assert f"Week {week:02d}" in graph
        assert f"Chapter {week:02d}" in graph


def test_raw_and_obsidian_references_are_rejected():
    module = load_module()
    assert module.has_forbidden_reference("materials/raw/private.pdf")
    assert module.has_forbidden_reference("[[old obsidian link]]")
    assert not module.has_forbidden_reference("materials/markdown/aidd_bioinformatics/aidd.course_index.md")
