---
name: course-skill-router
description: Route AI_Course tasks to project-local workflows for lecture expansion, PPT storyboard, evidence review, research ingest, or vault maintenance.
---

# AI_Course Skill Router

This is the project-local entry point for `E:\Codex_Projects\AI_Course`. Use it before choosing a generic global skill. The project goal is courseware production, so routing starts from `course/`, not from a standalone wiki.

## Read First

1. `AGENTS.md`
2. `memory.md`
3. `course/weeks/_index.md`
4. The target week folder, usually `course/weeks/week_XX/`
5. Relevant `knowledge/index.md` entries only after the course week is clear

## Routing Matrix

| User intent | Use this local workflow | Supporting global skills |
|---|---|---|
| Expand a short weekly `script.md` | `course-lecture-expand` | `scientific-writing`, `academic-chinese-style`, `research-writing-skill` |
| Create a PPT plan or deck brief | `course-ppt-storyboard` | `scientific-slides`, `academic-presentation-teaching`, `office-academic-skill`, `pptx` |
| Review claims, statistics, biology, or AI output | `course-evidence-review` | `scientific-critical-thinking`, `peer-review`, `statistical-analysis`, `biomedical-research-framework` |
| Add or summarize external teaching material | `course-update-vault` for routing, then existing research/material skills | `building-llm-wiki`, `web-research`, `academic-paper-search` |
| Rebuild indexes, check links, or check stale week mapping | `course-update-vault` | `building-llm-wiki`, `markdown-mermaid-writing` |

## Non-Negotiable Boundaries

- `course/syllabus/` and `course/weeks/` are the course truth layer.
- `knowledge/` supports preparation; it does not override the syllabus.
- `materials/raw/` is read-only.
- Do not use Obsidian wiki links. Use standard Markdown links.
- Do not put generated PPT, PNG previews, logs, or raw external course files into Git.
- AI can draft explanations and checks, but medical, statistical, biological, and source claims require human or documented source verification.

## Expected Output

When routing a task, state:

1. Target workflow.
2. Files to read first.
3. Files that may be changed.
4. Validation commands to run.

For example:

```text
Workflow: course-lecture-expand
Read: course/weeks/week_15/{materials,outline,script}.md, knowledge/concepts/差异表达分析.md
Write: course/weeks/week_15/script.md, docs/course_script_depth_report.md
Validate: python scripts/maintenance/course_script_depth.py
```
