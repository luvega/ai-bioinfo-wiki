# AI_Course Courseware Restructure Design

## Goal

Reframe `F:\AI_Course` from a wiki-first knowledge base into a courseware production workspace for `course/syllabus/36课时-AI前置调整版.docx`, while preserving the useful wiki content as a secondary knowledge layer.

## Current Problems

- The repository README and AGENTS schema describe the project as an LLM Wiki, but the current work target is PPT outline, lecture script, and courseware production.
- The existing `knowledge/` has useful distilled content, but it now contains stale teaching-week mapping. The most important mismatch is Week 11: current syllabus/lecture notes define Week 11 as scientific figure standards, while old wiki pages still treat Week 11 as DESeq2 and enrichment.
- `sources/` mixes several concepts: old PDF markdown, MinerU API output, and an AIDD text mirror. This makes it unclear which files are source inputs, generated markdown, or course-ready material.
- `materials/raw/aidd_bioinformatics/` and `materials/markdown/aidd_bioinformatics/` duplicate the same 73 text files.
- `course/syllabus/` contains the actual course source of truth, but it is presented as a raw layer rather than the center of the courseware process.
- `scripts/convert/clean_aidd_subtitles.py` and `scripts/convert/pdf_to_markdown.py` still hard-code `E:/AI_Course`, which is wrong for the current `F:\AI_Course` checkout.
- `嵩天Python/Pythonppt.pdf` is a course reference asset sitting at repository root.

## Design Decision

Use a courseware-first layout:

```text
F:\AI_Course\
├── AGENTS.md
├── memory.md
├── README.md
├── materials\
│   ├── raw\
│   │   ├── pdf_originals\
│   │   ├── aidd_bioinformatics\
│   │   └── external_ppt\
│   ├── markdown\
│   │   ├── pdf_library_legacy\
│   │   ├── pdf_library_mineru\
│   │   └── aidd_bioinformatics
│   └── manifests\
├── course\
│   ├── syllabus\
│   ├── weeks\
│   ├── templates\
│   └── assessments\
├── knowledge\
│   ├── index.md
│   ├── log.md
│   ├── sources\
│   ├── entities\
│   ├── concepts\
│   ├── topics\
│   ├── synthesis\
│   ├── queries\
│   └── assets\
├── scripts\
│   ├── convert\
│   ├── audit\
│   └── courseware\
├── outputs\
│   ├── pptx\
│   ├── scripts\
│   └── handouts\
└── docs\superpowers\
```

## Layer Responsibilities

### `materials/`

Stores input and generated source material. It is not directly courseware.

- `materials/raw/pdf_originals/`: immutable original PDFs, ignored by git.
- `materials/raw/aidd_bioinformatics/`: cleaned AIDD text files, treated as source input.
- `materials/raw/external_ppt/`: external reference courseware such as `Pythonppt.pdf`.
- `materials/markdown/pdf_library_legacy/`: old lightweight PDF-to-Markdown output.
- `materials/markdown/pdf_library_mineru/`: MinerU API output and promoted `book.mineru.md`.
- `materials/markdown/aidd_bioinformatics/`: optional AIDD mirror if retained for backward compatibility.
- `materials/manifests/`: future cross-material inventories and conversion manifests.

### `course/`

Stores the actual teaching design and courseware source.

- `course/syllabus/`: official syllabus docx and teacher-written lecture notes.
- `course/weeks/`: one folder per week, each ready to hold PPT outline, lecture script, material notes, and future slide source.
- `course/templates/`: reusable AI log, grading, and PPT/script templates.
- `course/assessments/`: quizzes, rubrics, homework, and final-project materials.

### `knowledge/`

Preserves the former `knowledge/` content as distilled knowledge and cross-source synthesis. It no longer owns the project architecture. It supports courseware production but does not replace the course syllabus.

### `scripts/`

Group scripts by responsibility:

- `scripts/convert/`: source conversion and extraction scripts.
- `scripts/audit/`: future checks for broken links, stale week mappings, and material inventories.
- `scripts/courseware/`: future PPT/script generation tools.

### `outputs/`

Generated deliverables. Most of this should be ignored unless a final export is intentionally tracked.

## Migration Rules

- Do not delete source material.
- Do not overwrite generated MinerU state.
- Keep raw PDFs ignored by git.
- Keep stable generated Markdown trackable unless later decided otherwise.
- Preserve current uncommitted MinerU files under their new path.
- Keep `AGENTS.md` and `memory.md` at repository root, but update them to describe the new courseware-first architecture.
- Keep standard Markdown links, not Obsidian wiki links.
- Use repository-root-relative paths in scripts, never hard-coded drive letters.

## Content Corrections Required During Migration

The course source of truth is `course/syllabus/36课时-AI前置调整版.docx` and `course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md`.

The migrated knowledge layer must update stale week mappings:

- Week 11: 科研图表规范与 SCI 图表表达
- Week 14: 转录组数据分析基础
- Week 15: 差异表达分析与功能解读
- Week 16: 单细胞转录组可视化

DESeq2, differential expression, and enrichment remain useful concepts, but their main course position is Week 15 rather than Week 11.

## Initial Week Folder Contract

Create `course/weeks/week_01` through `course/weeks/week_18`, each containing:

- `outline.md`: PPT outline skeleton.
- `script.md`: lecture script skeleton.
- `materials.md`: source-material mapping skeleton.

These are courseware working files, not final exported slides.

## Verification

After migration:

- `python -m py_compile scripts/convert/*.py` must pass.
- `rg -n "knowledge/" README.md AGENTS.md memory.md knowledge course scripts` should only show intentional historical references or updated references.
- `rg -n "E:/AI_Course|E:\\AI_Course|e:\\AI_Course|llm_wiki_kb"` should not find active script paths.
- `rg -n "第 11 周.*DESeq2|Week 11.*DESeq2|第 11 周.*富集"` should not find current course-position claims outside historical log entries.
- `git status --short` should show moves and edits but no accidental generated cache directories.
