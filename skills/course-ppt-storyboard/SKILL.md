---
name: course-ppt-storyboard
description: Create reviewable AI_Course PPT storyboards and slide briefs before generating editable PPTX decks.
---

# Course PPT Storyboard

Use this workflow before generating a PPTX for AI_Course. The first output is a reviewable storyboard or brief, not a binary deck.

## Inputs

1. `course/weeks/week_XX/outline.md`
2. `course/weeks/week_XX/script.md`
3. `course/weeks/week_XX/materials.md`
4. Any week review in `course/evaluation/`
5. Relevant source or concept pages from `knowledge/`

## Storyboard Contract

Each slide must include:

- Action title: a sentence-level teaching point, not a topic label.
- Visual intent: table, workflow, small dataset, schematic, code fragment, or graph.
- Teacher note: what the instructor says or asks.
- Student action: what students calculate, inspect, discuss, or submit.
- Evidence/source note: where the content comes from.
- Risk note: what must not be overclaimed.

## PPT Boundary

- Do not generate PPTX until the storyboard is reviewable.
- Do not put dense paragraphs on slides.
- Every technical figure needs source, data, or generated-example status.
- AI-generated diagrams are allowed only as teaching schematics, not as source evidence.
- Final PPTX must be visually checked through exported page previews.

## Validation

Run the normal course checks plus any PPT-specific preview export when a deck is generated:

```powershell
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_km_index.py --check
```
