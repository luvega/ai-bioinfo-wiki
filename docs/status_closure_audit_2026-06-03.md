# AI_Course 技能与状态收口审计 · 2026-06-03

本页用于收口当前本地改动，避免技能体系、讲义扩写、PPT 试点和状态文档混在一起失去边界。

## 审计结论

- 工作区：`E:\Codex_Projects\AI_Course`
- 当前主线：courseware-first；`course/` 是生产主线，`knowledge/` 是备课辅助层。
- 旧根目录：`F:\AI_Course` 已删除，不作为工作区、回退目录或 Obsidian vault。
- Git 边界：不 push、不改远端可见性、不删除远端；`outputs/`、原始商业 PDF、外部 PPT/PDF、缓存和学生数据不进入 Git。

## 四组改动

| Group | Scope | Files / Evidence | Acceptance |
|---|---|---|---|
| 技能体系 | 全局白名单、本地 workflow skills、技能清单检查 | `docs/skill_loading_manifest_2026-06-03.md`、`skills/README.md`、`scripts/maintenance/course_skill_inventory.py`、`skills/course-*`、`tests/test_course_skill_inventory.py` | `python scripts/maintenance/course_skill_inventory.py --check` 输出 OK |
| 18 周讲义扩写 | 18 个 `script.md` 达到 `formal_ready/full-lecture` | `course/weeks/week_01/script.md` 到 `course/weeks/week_18/script.md`、`scripts/maintenance/course_script_depth.py`、`docs/course_script_depth_report.md` | `course_script_depth.py` 报告 18 周均为 `full-lecture`，且说明该状态只适用于 `script.md` |
| Week 15 PPT 试点 | storyboard、证据审查、官方蓝模板 PPT 输出和视觉 QA | `course/weeks/week_15/ppt_storyboard.md`、`course/evaluation/week_15_ppt_evidence_review.md`、`scripts/courseware/build_week15_sysu_official_ppt.py`、`outputs/ppt/sysu_official_blue/week_15/qa-notes.md` | Git 只跟踪 storyboard/review/script；PPTX、PNG、contact sheet 和输出 QA 留在 `outputs/` |
| 项目说明与状态文档 | 状态语义、当前进展、维护入口和本轮审计 | `AGENTS.md`、`README.md`、`memory.md`、`docs/project_review_2026-06-03.md`、本页 | 不再把 `formal_ready/full-lecture` 误写成整周正式完成或 PPT 自动可生成 |

## 状态语义

- `script.md` 的 `status: formal_ready` 与 `depth: full-lecture` 只代表讲义深度和教师话术长度达标。
- `materials.md` 与 `outline.md` 的 `status` 才代表周次素材/大纲准备度；当前只有 Week 03/14/15/16 为样板周 `pilot_ready`。
- PPT 状态单独按 `storyboard -> evidence review -> PPTX -> PNG/contact sheet QA` 判断。
- AI、统计、生物学、医学和图形解释仍需要 claim-evidence gate；讲义字数不能替代事实核验。

## 本地输出边界

已确认存在但不入 Git 的输出：

- `outputs/ppt/week_03_pilot/`
- `outputs/ppt/sysu_official_blue/week_15/`

这些目录可用于人工查看 PPTX、PNG 预览、contact sheet 和 QA 文本，但不应移动到 `course/`、`knowledge/` 或 `docs/`。

## 维护命令

```powershell
$env:PYTHONUTF8='1'
python scripts/maintenance/course_km_index.py --write
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py --write docs/course_script_depth_report.md
python scripts/maintenance/course_skill_inventory.py --check
python -m pytest -q
```

## 收口后仍不做

- 不全量生成 18 周 PPT。
- 不把项目本地 `skills/` 安装到全局。
- 不扩大外部资料面。
- 不 push、不改远端、不删除远端仓库。
