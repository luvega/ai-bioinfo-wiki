# MinerU API-only PDF Structuring Implementation Plan

**Goal:** Convert the four reference-book PDFs into structured Markdown through MinerU cloud API, without keeping a local MinerU CLI environment.

**Architecture:** Keep `materials/raw/pdf_originals/` immutable. Store MinerU-derived API metadata and promoted Markdown under `materials/markdown/pdf_library_mineru/`. Ignore downloaded zips and raw extracted payloads. Use `page_ranges` to split long books into API tasks instead of creating local PDF split files.

**Tech Stack:** PowerShell on Windows, Python standard library, `pypdf` for page counting, MinerU Precision API.

## Completed

- [x] Add `scripts/convert/mineru_pdf_pipeline.py` as an API-only pipeline.
- [x] Remove local CLI assumptions, including `.venv-mineru` and `mineru run` commands.
- [x] Generate `materials/markdown/pdf_library_mineru/INDEX.md` and `manifest.json`.
- [x] Add `prepare-parts` to write `api_parts.json` with `page_ranges`.
- [x] Add `api-submit`, `api-poll --download`, and `api-promote`.
- [x] Update README, project memory, wiki synthesis, and log to reflect API-only mode.
- [x] Ignore bulky API caches: `api_zips/`, `api_raw/`, images, and zip files.

## Verification

```powershell
python -m py_compile scripts/convert/mineru_pdf_pipeline.py
python scripts/convert/mineru_pdf_pipeline.py inventory
python scripts/convert/mineru_pdf_pipeline.py prepare-parts
python scripts/convert/mineru_pdf_pipeline.py api-check
```

`api-check` is expected to return non-zero if `MINERU_API_TOKEN` is not set. Do not write the token to files.
