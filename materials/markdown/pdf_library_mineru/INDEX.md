---
type: raw-index
title: MinerU PDF Library Index
source_dirs:
  - materials/raw/pdf_originals
  - materials/raw/external_ppt
output_dir: materials/markdown/pdf_library_mineru
generated: 2026-05-24 12:15:33
status: generated
---

# MinerU PDF Library Index

This directory stores Markdown and JSON returned by MinerU Precision API.
Original PDFs remain under `materials/raw/` and are not modified.

| Book | Source PDF | Pages | Size MB | Output folder |
|---|---|---:|---:|---|
| An Introduction to Statistical Learning_ with Applications Python | `materials/raw/pdf_originals/An Introduction to Statistical Learning_ with Applications Python.pdf` | 613 | 19.12 | `An_Introduction_to_Statistical_Learning_with_Applications_Python/` |
| An Introduction to Statistical Learning_ with Applications R-- | `materials/raw/pdf_originals/An Introduction to Statistical Learning_ with Applications R--.pdf` | 436 | 10.35 | `An_Introduction_to_Statistical_Learning_with_Applications_R/` |
| Starting Data Analytics with Generative AI and Python 9781633437210 | `materials/raw/pdf_originals/Starting Data Analytics with Generative AI and Python 9781633437210.pdf` | 362 | 15.49 | `Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210/` |
| 【R240】Learn AI-Assisted Python Programming With GitHub Copilot and ChatGPT (2023)【Leo Porter, Daniel Zingaro】 | `materials/raw/pdf_originals/【R240】Learn AI-Assisted Python Programming With GitHub Copilot and ChatGPT (2023)【Leo Porter, Daniel Zingaro】.pdf` | 298 | 8.83 | `R240_Learn_AI_Assisted_Python_Programming_With_GitHub_Copilot_and_ChatGPT_2023_Leo_Porter_Daniel_Zingaro/` |
| Pythonppt | `materials/raw/external_ppt/嵩天Python/Pythonppt.pdf` | 1287 | 32.9 | `Pythonppt/` |

## API Workflow

```powershell
$env:MINERU_API_TOKEN = "<token>"
python scripts/convert/mineru_pdf_pipeline.py prepare-parts
python scripts/convert/mineru_pdf_pipeline.py api-submit --model-version vlm
python scripts/convert/mineru_pdf_pipeline.py api-poll --wait --download
python scripts/convert/mineru_pdf_pipeline.py api-promote
```

`api_zips/` and `api_raw/` are generated caches.
Promoted files use `book.mineru.md` and `book.part_XXX.mineru.md`.
