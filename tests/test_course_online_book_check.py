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
    assert all(chapter["textbook_status"] == "expanded_draft" for chapter in chapters)
    assert all(chapter["ppt_status"] == "storyboard_expanded" for chapter in chapters)
    assert all(chapter["storyboard_pages"] == 40 for chapter in chapters)
    assert all(chapter["teaching_plan_source"] == f"course/weeks/week_{chapter['week']:02d}/teaching_plan.md" for chapter in chapters)
    week05 = next(chapter for chapter in chapters if chapter["week"] == 5)
    assert week05["title"] == "数据读取与整理"


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


def test_dual_track_coursebook_and_courseware_routes_are_present():
    review_route = ROOT / "site" / "src" / "pages" / "coursebook" / "review.astro"
    chapter_route = ROOT / "site" / "src" / "pages" / "coursebook" / "[slug].astro"
    index_route = ROOT / "site" / "src" / "pages" / "coursebook.astro"
    logical_v2_index = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2.astro"
    logical_v2_route = ROOT / "site" / "src" / "pages" / "coursebook" / "logical-v2" / "[slug].astro"
    courseware_index = ROOT / "site" / "src" / "pages" / "courseware.astro"
    courseware_route = ROOT / "site" / "src" / "pages" / "courseware" / "[slug].astro"
    assert review_route.exists()
    assert "兼容入口" in review_route.read_text(encoding="utf-8")
    chapter_text = chapter_route.read_text(encoding="utf-8")
    assert "教材正文" in chapter_text
    assert "Storyboard 审核表" not in chapter_text
    index_text = index_route.read_text(encoding="utf-8")
    assert "/courseware" in index_text
    assert "/coursebook/logical-v2" in index_text
    assert logical_v2_index.exists()
    assert logical_v2_route.exists()
    assert "logicalV2Chapters" in logical_v2_index.read_text(encoding="utf-8")
    logical_v2_route_text = logical_v2_route.read_text(encoding="utf-8")
    assert "logicalV2ReviewChapters" in logical_v2_route_text
    assert "cwd()" in logical_v2_route_text
    assert "Missing logical v2 chapter source" in logical_v2_route_text
    assert "正文尚未生成" not in logical_v2_route_text
    assert "Teaching Plan 与 Storyboard 审核台" in courseware_index.read_text(encoding="utf-8")
    route_text = courseware_route.read_text(encoding="utf-8")
    assert "40 页主干 storyboard 审核表" in route_text
    assert "studentAction" in route_text


def test_logical_v2_online_map_exposes_review_ready_batch():
    module = load_module()
    chapters = module.parse_map(ROOT / "course" / "textbook" / "logical_v2" / "coursebook_map.yml")
    ready = {chapter["chapter"] for chapter in chapters if chapter["status"] == "review_ready"}
    assert ready == module.LOGICAL_V2_REVIEW_CHAPTERS
    for chapter in chapters:
        if chapter["chapter"] in module.LOGICAL_V2_REVIEW_CHAPTERS:
            assert chapter["page"] == f"/coursebook/logical-v2/chapter-{chapter['chapter']:02d}"
            assert chapter["review_status"] == "review_ready"


def test_full_week_pilot_candidate_statuses_are_enforced():
    module = load_module()
    chapters = module.parse_map(ROOT / "course" / "textbook" / "coursebook_map.yml")
    assert all(chapter["review_status"] in module.MINIMUM_REVIEW_STATUSES for chapter in chapters)
    week13 = next(chapter for chapter in chapters if chapter["week"] == 13)
    assert week13["review_status"] == "pilot_ready"
    assert week13["ppt_status"] == "storyboard_expanded"
    for week in range(1, 19):
        week_dir = ROOT / "course" / "weeks" / f"week_{week:02d}"
        for name in ("materials.md", "outline.md"):
            text = (week_dir / name).read_text(encoding="utf-8")
            assert any(f"status: {status}" in text for status in module.MINIMUM_WEEK_FILE_STATUSES)


def test_trial_ready_packs_cover_teacher_needs():
    module = load_module()
    for week in module.TRIAL_READY_PACK_WEEKS:
        pack = ROOT / "course" / "weeks" / f"week_{week:02d}" / "teaching_pack_v1.md"
        text = pack.read_text(encoding="utf-8")
        assert module.contains_required_terms(text, module.TRIAL_READY_PACK_TERMS) == []


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
