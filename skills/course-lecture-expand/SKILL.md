---
name: course-lecture-expand
description: Expand AI_Course weekly script.md files from scaffold or placeholder into pilot-script lecture notes for pharmacy undergraduates.
---

# Course Lecture Expand

Use this workflow when a weekly `course/weeks/week_XX/script.md` is too short or only repeats the PPT outline. The goal is a teacher-usable 2-hour lecture script, not a bullet summary.

## Inputs

Read in this order:

1. `course/weeks/week_XX/materials.md`
2. `course/weeks/week_XX/outline.md`
3. `course/weeks/week_XX/script.md`
4. `course/evaluation/lecture_script_standard.md`
5. Relevant `knowledge/` pages named by the week materials
6. `course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md` for course-level continuity

## Target Depth

| Level | CJK chars | Status |
|---|---:|---|
| scaffold | 800-1500 | Not enough for PPT production |
| pilot-script | 3500-5500 | Target for Week 14/15/16 expansion |
| full-lecture | 6500-9000 | Later formal teaching handout |

## Required Structure

Each expanded `script.md` must include:

- Direct teacher-facing opening.
- Why this topic matters in pharmacy or biomedical data work.
- Core concept explanations in complete paragraphs.
- One small classroom dataset, table, graph reading task, or code-reading task.
- Teacher questions, expected student answers, follow-up questions, and corrections.
- AI collaboration prompt and AI output audit checklist.
- Common misunderstandings.
- Board or slide pacing notes.
- Closing transition to the next week.
- Post-class exercise and scoring points.

## Writing Rules

- Write for pharmacy undergraduates; do not assume bioinformatics, statistics, or programming background.
- Keep terms such as `DESeq2`, `log2FoldChange`, `padj`, `UMAP`, `metadata`, `count matrix` in English when they are standard.
- Do not invent biological facts, gene functions, database claims, or software behavior.
- If a claim needs source review, mark it as `需数据库或文献核验`.
- Use teaching language that can be read aloud.
- Do not paste long external source text.

## Validation

After expansion, run:

```powershell
python scripts/maintenance/course_script_depth.py --write docs/course_script_depth_report.md
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_km_index.py --check
```
