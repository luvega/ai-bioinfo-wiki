---
name: course-update-vault
description: Maintain AI_Course indexes, skill registry, links, week mapping, and courseware quality gates.
---

# Course Update Vault

Use this workflow after meaningful ingest, courseware drafting, skill loading, folder moves, or when retrieval feels stale.

## Maintenance Scope

- Rebuild generated indexes.
- Check standard Markdown links.
- Check Week 11/15 historical mapping.
- Check sample-week quality markers.
- Check lecture script depth.
- Check local and global skill registry.
- Write reports under `docs/` when the result should persist.

## Commands

```powershell
python scripts/maintenance/course_km_index.py --write
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py --write docs/course_script_depth_report.md
python scripts/maintenance/course_skill_inventory.py --check
python -m pytest -q
```

## Boundaries

- Maintenance reports problems; it does not create new scientific claims.
- Do not move or delete `materials/raw/`.
- Do not use Obsidian wiki links.
- Do not push or change remote visibility without explicit user confirmation.
