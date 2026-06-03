---
name: course-evidence-review
description: Review AI_Course scripts, outlines, PPT storyboards, or generated explanations for claim-evidence alignment and overclaim risk.
---

# Course Evidence Review

Use this workflow when reviewing course content, AI-generated explanations, biological interpretations, statistical claims, or PPT storyboards.

## Review Axes

| Axis | Question |
|---|---|
| Course fit | Is the statement appropriate for pharmacy undergraduates? |
| Source grounding | Is the claim supported by syllabus, materials, knowledge pages, database, or literature? |
| Statistics | Are `pvalue`, `padj`, effect size, sample size, and model assumptions described correctly? |
| Biology | Are gene, pathway, cell type, and mechanism statements marked as verified or needing verification? |
| Visualization | Does the graph interpretation distinguish what is shown from what is inferred? |
| AI boundary | Does the text separate AI suggestions from confirmed evidence? |

## Output Format

Use this structure:

```markdown
## Verdict

pass / revise-before-ppt / needs-source-review

## Findings

| Severity | Location | Issue | Fix |
|---|---|---|---|

## Claim-Evidence Gate

| Claim | Evidence status | Action |
|---|---|---|

## Next Checks
```

## Hard Rules

- Do not accept unsupported gene function or pathway mechanism as fact.
- Do not accept causal language from a visualization or association alone.
- Do not let `pilot_ready` mean `formal_ready`.
- When source evidence is missing, mark `needs-source-review` instead of inventing a citation.
