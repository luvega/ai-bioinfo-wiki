from __future__ import annotations

import base64
import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UTILS = ROOT / "scripts" / "convert" / "scbp_utils.py"


def load_utils():
    spec = importlib.util.spec_from_file_location("scbp_utils", UTILS)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_root_is_derived_from_script_location():
    module = load_utils()
    assert module.ROOT == ROOT


def test_parse_toc_resolves_root_and_chapters():
    module = load_utils()
    toc = """format: jb-book
root: preamble
parts:
  - caption: Introduction
    chapters:
      - file: introduction/scrna_seq
      - file: CHANGELOG
        title: "Changelog"
"""
    tree_paths = {
        "jupyter-book/preamble.md",
        "jupyter-book/introduction/scrna_seq.ipynb",
        "jupyter-book/CHANGELOG.md",
    }
    entries = module.parse_toc(toc, tree_paths)
    assert [entry.file for entry in entries] == ["preamble", "introduction/scrna_seq", "CHANGELOG"]
    assert entries[0].source_path == "jupyter-book/preamble.md"
    assert entries[1].source_type == "ipynb"
    assert entries[2].title == "Changelog"


def test_notebook_to_markdown_preserves_markdown_code_and_rewrites_links():
    module = load_utils()
    nb = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Title\n", "[relative](../other/page)\n"]},
            {"cell_type": "code", "source": ["import scanpy as sc\n", "sc.settings.verbosity = 0\n"], "outputs": []},
        ]
    }
    out = module.notebook_to_markdown(
        nb,
        title="Title",
        ref="abc123",
        source_path="jupyter-book/introduction/scrna_seq.ipynb",
    )
    assert "```python\nimport scanpy as sc" in out
    assert "https://github.com/theislab/single-cell-best-practices/blob/abc123/jupyter-book/other/page" in out


def test_export_notebook_code_uses_cell_markers():
    module = load_utils()
    nb = {
        "cells": [
            {"cell_type": "markdown", "source": "## Context"},
            {"cell_type": "code", "source": "%%R\nlibrary(Seurat)\n", "outputs": []},
        ]
    }
    code = module.export_notebook_code(nb, title="R cell", ref="abc123", source_path="jupyter-book/x.ipynb")
    assert "# %% [markdown]" in code
    assert "# %%" in code
    assert "%%R\nlibrary(Seurat)" in code


def test_extract_dataset_references_keeps_blocked_and_lamindb_entries():
    module = load_utils()
    text = """
! wget -O data.csv https://figshare.com/ndownloader/files/35574338
https://s3-eu-west-1.amazonaws.com/file.csv?X-Amz-Signature=old&X-Amz-Expires=10
af = ln.Artifact.connect("theislab/sc-best-practices").get(key="sample.h5ad", is_latest=True)
adata = sc.read_h5ad("local.h5ad")
"""
    refs = module.extract_dataset_references(text, source_id="demo")
    statuses = {item["value"]: item["status"] for item in refs}
    assert statuses["https://figshare.com/ndownloader/files/35574338"] == "pending_download"
    assert any(item["status"] == "blocked" for item in refs)
    assert any(item["kind"] == "lamindb_artifact" for item in refs)
    assert any(item["kind"] == "data_read_call" for item in refs)


def test_extract_notebook_output_files_decodes_images_and_text(tmp_path):
    module = load_utils()
    payload = base64.b64encode(b"fake-png").decode("ascii")
    nb = {
        "cells": [
            {
                "cell_type": "code",
                "source": "display(plot)",
                "outputs": [
                    {"output_type": "display_data", "data": {"image/png": payload, "text/plain": ["plot"]}},
                    {"output_type": "stream", "text": ["hello\n"]},
                ],
            }
        ]
    }
    records = module.extract_notebook_output_files(nb, tmp_path)
    assert len(records) == 3
    assert any(record["mime"] == "image/png" for record in records)
    assert any((tmp_path / Path(record["path"]).name).exists() for record in records)
