# MinerU Course Markdown Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert MinerU `book.mineru.md` outputs into course-facing `book.course.md` and `structure_report.md` files for AI_Course lesson preparation, and include AIDD txt lectures as a parallel course-material index.

**Architecture:** Keep raw MinerU Markdown and AIDD txt files unchanged. Add one deterministic courseware script under `scripts/courseware/` that reads each `book.mineru.md`, extracts heading hierarchy, short teaching-focused highlights, formulas, code/example/image/table markers, and maps content to the 18-week course. The same script reads `materials/markdown/aidd_bioinformatics/**/*.txt` and generates a course index plus per-chapter lecture cards. Generated files stay inside the corresponding material folders.

**Tech Stack:** Python standard library, Markdown heuristics, existing `materials/markdown/pdf_library_mineru/` layout.

---

### Task 1: Add Course Markdown Generator

**Files:**
- Create: `scripts/courseware/mineru_course_markdown.py`

- [x] **Step 1: Implement parser and output writer**

Create a script that:
- Finds `materials/markdown/pdf_library_mineru/*/book.mineru.md`.
- Parses YAML front matter, headings, code blocks, images, tables, and formula-like lines.
- Builds a full heading outline.
- Groups content by top-level sections.
- Writes `book.course.md` with course positioning, week mapping, outline, and per-section teaching cards.
- Writes `structure_report.md` with counts, warning flags, and generated file paths.

- [x] **Step 2: Keep extraction bounded**

Limit direct excerpts to short snippets per section. Do not copy full chapters into `book.course.md`; the complete parsed text remains in `book.mineru.md`.

### Task 2: Run Generator

**Files:**
- Create/Update: `materials/markdown/pdf_library_mineru/<slug>/book.course.md`
- Create/Update: `materials/markdown/pdf_library_mineru/<slug>/structure_report.md`

- [x] **Step 1: Run generator for all books**

Run:

```powershell
python scripts/courseware/mineru_course_markdown.py
```

Expected: five `book.course.md` files and five `structure_report.md` files.

- [x] **Step 2: Generate AIDD txt lecture index**

The same command also creates:
- `materials/markdown/aidd_bioinformatics/aidd.course_index.md`
- `materials/markdown/aidd_bioinformatics/aidd.structure_report.md`
- `materials/markdown/aidd_bioinformatics/<chapter>/chapter.course.md`

Expected: 71 txt lectures indexed into 11 chapter course files.

### Task 3: Verify Outputs

**Files:**
- Read: generated `book.course.md` files
- Read: generated `structure_report.md` files

- [x] **Step 1: Check generated counts**

Run summary commands to confirm all five book folders have both files.

- [x] **Step 2: Inspect representative outputs**

Open one AI programming book and one Python PPT course file. Confirm:
- YAML front matter exists.
- Course week mapping exists.
- Heading hierarchy is present.
- Section cards include highlights, formulas/examples/code/images/tables when available.
- Warnings identify noisy OCR/Mermaid when present.

- [x] **Step 3: Inspect AIDD output**

Open the AIDD root index and one chapter course file. Confirm:
- The 36-hour week mapping exists.
- The full txt lecture table exists.
- Chapter files contain per-lesson material cards with source paths, duration, keywords/entities, and short review snippets.

### Task 4: Update Documentation

**Files:**
- Modify: `knowledge/synthesis/MinerU_PDF结构化转换方案.md`
- Modify: `knowledge/log.md`
- Modify: `memory.md`

- [x] **Step 1: Record generated course layer**

Document that `book.course.md` and `structure_report.md` were generated as course-facing derivatives of `book.mineru.md`.

- [x] **Step 2: Run final checks**

Run:

```powershell
python -m py_compile scripts/courseware/mineru_course_markdown.py
rg -n -F "<known-token-fragment>" . -g "*.md" -g "*.json" -g "*.py" -g "*.ps1"
```

Expected: compile passes; no token string in project files.
