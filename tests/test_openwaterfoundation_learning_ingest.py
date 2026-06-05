from __future__ import annotations

import importlib.util
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "convert" / "ingest_openwaterfoundation_learning.py"


def load_ingest():
    assert MODULE_PATH.exists(), "OWF ingest script is missing"
    spec = importlib.util.spec_from_file_location("ingest_openwaterfoundation_learning", MODULE_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


MKDOCS_FIXTURE = """
site_name: Learn / Git
nav:
- Home: index.md
- Install:
  - Git: install/git.md
  - GitHub: cloud/github.md
- Resources: resources.md
copyright: Copyright Open Water Foundation
"""


def test_sources_are_fixed_to_expected_commits_and_root_is_derived():
    ingest = load_ingest()

    assert ingest.ROOT == ROOT
    assert ingest.SOURCES["git"].commit_sha == "42a393fb0e2daff55ae973f940ca946ae8d05acf"
    assert ingest.SOURCES["windows_shell"].commit_sha == "3d459b386751e1d799f13c63fa9a7dbcda1ac6d3"
    assert ingest.SOURCES["linux_shell"].commit_sha == "4cf789ec9b3ae88a6f8be218dcd4dadcf86ac18d"
    assert all("E:\\Codex_Projects\\AI_Course" not in str(value) for value in ingest.SOURCES.values())


def test_parse_mkdocs_nav_pages_preserves_order():
    ingest = load_ingest()

    pages = ingest.parse_mkdocs_nav_pages(MKDOCS_FIXTURE)

    assert pages == ["index.md", "install/git.md", "cloud/github.md", "resources.md"]


def test_rewrite_markdown_links_keeps_external_and_normalizes_local_targets():
    ingest = load_ingest()
    text = (
        "[GitHub](https://github.com/OpenWaterFoundation/owf-learn-git)\n"
        "[Install](install/git.html)\n"
        "[Cloud](cloud/github.md#setup)\n"
        "![Logo](images/logo.png)\n"
        "[Script](examples/demo.sh)\n"
    )
    registry = {
        "index.md",
        "install/git.md",
        "cloud/github.md",
        "images/logo.png",
        "examples/demo.sh",
    }

    rewritten = ingest.rewrite_local_links(text, Path("index.md"), registry)

    assert "https://github.com/OpenWaterFoundation/owf-learn-git" in rewritten
    assert "(install/git.md)" in rewritten
    assert "(cloud/github.md#setup)" in rewritten
    assert "(images/logo.png)" in rewritten
    assert "(examples/demo.sh)" in rewritten


def test_rewrite_markdown_links_repairs_mkdocs_root_relative_patterns():
    ingest = load_ingest()
    registry = {"install/git.md", "introduction/introduction.md"}

    eol = ingest.rewrite_local_links(
        "[Git for Windows](../install/git#install-git-on-windows)",
        Path("eol.md"),
        registry,
    )
    cron = ingest.rewrite_local_links(
        "[Introduction](introduction)",
        Path("appendix-cron/cron-wsl/cron-wsl.md"),
        registry,
    )

    assert "(install/git.md#install-git-on-windows)" in eol
    assert "(../../introduction/introduction.md)" in cron


def test_unresolved_local_links_become_upstream_urls_when_site_url_is_supplied():
    ingest = load_ingest()

    rewritten = ingest.rewrite_local_links(
        "[Shell Script Basics](../shell-script-basics/shell-script-basics)",
        Path("introduction/introduction.md"),
        {"index.md"},
        site_url="https://learn.openwaterfoundation.org/owf-learn-windows-shell/",
    )

    assert (
        "https://learn.openwaterfoundation.org/owf-learn-windows-shell/"
        "shell-script-basics/shell-script-basics.html"
    ) in rewritten


def test_discover_docs_tree_registers_markdown_assets_and_examples(tmp_path):
    ingest = load_ingest()
    docs = tmp_path / "mkdocs-project" / "docs"
    (docs / "guide").mkdir(parents=True)
    (docs / "images").mkdir(parents=True)
    (docs / "examples").mkdir(parents=True)
    (docs / "index.md").write_text("# Home\n", encoding="utf-8")
    (docs / "guide" / "setup.md").write_text("# Setup\n", encoding="utf-8")
    (docs / "images" / "logo.png").write_bytes(b"png")
    (docs / "examples" / "demo.sh").write_text("echo ok\n", encoding="utf-8")

    tree = ingest.discover_docs_tree(docs)

    assert [item.as_posix() for item in tree.markdown_files] == ["guide/setup.md", "index.md"]
    assert [item.as_posix() for item in tree.asset_files] == ["images/logo.png"]
    assert [item.as_posix() for item in tree.example_files] == ["examples/demo.sh"]


def test_safe_extract_zip_rejects_path_traversal(tmp_path):
    ingest = load_ingest()
    archive = tmp_path / "bad.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr("../escape.txt", "bad")

    try:
        ingest.safe_extract_zip(archive, tmp_path / "out")
    except RuntimeError as exc:
        assert "Unsafe zip member path" in str(exc)
    else:
        raise AssertionError("unsafe zip member was accepted")
