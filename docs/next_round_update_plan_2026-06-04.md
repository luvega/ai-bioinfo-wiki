# AI_Course 下一轮更新计划（质量闭环后续）

## Summary

- 当前状态：在线教材已有 Week 03/14/15/16 样章，Week 13 已开放为 `sample_candidate` 候选样章；Week 14/16 已有 storyboard 与 evidence review，但公开图形/素材仍处于 `evidence_review_assets_pending`。
- 下一轮目标：把 Week 13 从“样章候选”推进到“可授课试点候选”，同时为 Week 14/16 补齐可公开展示素材核验，为 Week 17/18 项目交付提供学生可直接使用的模板包。
- 质量边界：继续保持 `script.md formal_ready`、周次 `materials/outline` 状态、Coursebook 样章状态和 PPT 生产状态分层，不因讲义或 storyboard 完成而自动宣称 PPTX 完成。

## Priority Work

### P0 · Week 13 候选样章验收

- 补齐 Week 13 的可公开教学矩阵、PCA 坐标表、聚类参数表和热图/UMAP 示意说明。
- 对 `course/weeks/week_13/ppt_storyboard.md` 做 evidence review，形成 `course/evaluation/week_13_ppt_evidence_review.md`。
- 若 evidence review 通过，将 Week 13 从 `sample_candidate` 推进到 `pilot_candidate` 或 `pilot_ready`，但仍不宣称 PPTX 完成。

### P1 · Week 14/16 素材资产核验

- Week 14：核对 AIDD 上游流程中的命令名、软件名和文件格式，确定正式 PPT 是否使用自绘流程图。
- Week 16：准备可公开展示的 QC、UMAP、marker、spatial 示例图，或统一改用自生成教学示意图。
- 完成后将 Week 14/16 从 `evidence_review_assets_pending` 推进到 `evidence_review_pass`，再决定是否进入 PPTX。

### P2 · Week 17/18 学生项目模板包

- 新增或完善学生可直接使用的模板：
  - `course/templates/project_readme_template.md`
  - `course/templates/data_sources_template.md`
  - `course/templates/ppt_storyboard_template.md`
  - 继续使用 `course/templates/ai_use_statement_template.md`
- 在 Week 17/18 `materials.md` 与 `outline.md` 中显式绑定模板包和 [student_project_rubric.md](../course/evaluation/student_project_rubric.md)。

### P3 · Week 11/12 微项目课堂素材化

- 把 [Week 11-13 连续微项目](../course/weeks/week_11_13_micro_project.md) 中的教学矩阵拆成教师可直接投屏/打印的课堂表格。
- Week 11 增加“错误图注 -> 修订图注”示例。
- Week 12 增加“临床表格 -> 样本 x 指标矩阵 -> metadata”示例。
- 目标是让 Week 11/12 从 `draft` 推进到 `pilot_candidate`，为后续 Coursebook 样章扩展做准备。

### P4 · 在线教材体验与状态解释

- Coursebook 页面增加“状态流水线”说明：`catalog_only -> sample_candidate -> sample_ready -> storyboard -> evidence_review_pass -> pptx_trial_done`。
- 在 Week 13 页面显式显示“候选样章”的待完成事项。
- 检查 Pagefind 搜索是否能检索到“样章候选”“AI 使用声明”“项目 rubric”“evidence_review_assets_pending”。

## Implementation Sequence

1. 先补 Week 13 evidence review 和教学图表素材说明。
2. 再补 Week 14/16 公开素材核验记录。
3. 再补 Week 17/18 学生项目模板包。
4. 同步 Coursebook map、`site/src/data/coursebook.ts` 和维护检查脚本。
5. 运行维护、pytest、Astro build 和本地 preview smoke check。

## Test Plan

```powershell
python scripts/maintenance/course_km_index.py --write
python scripts/maintenance/course_km_index.py --check
python scripts/maintenance/course_quality_check.py --check
python scripts/maintenance/course_script_depth.py --write docs/course_script_depth_report.md
python scripts/maintenance/course_skill_inventory.py --check
python scripts/maintenance/course_online_book_check.py
python -m pytest tests/test_course_online_book_check.py -q
python -m pytest -q
Push-Location site; npm run build; Pop-Location
```

本地预览至少检查：

- `/coursebook/`
- `/coursebook/week-13/`
- `/coursebook/week-14/`
- `/coursebook/week-16/`
- `/weeks/week-17/`
- `/weeks/week-18/`

## Acceptance Criteria

- Week 13 有 evidence review 文档，且状态不再停留在“只有 storyboard”。
- Week 14/16 的公开素材风险被关闭或明确保留为 blocking item。
- Week 17/18 学生模板包能直接支撑综合项目提交。
- Coursebook 状态说明与 `coursebook_map.yml`、`coursebook.ts` 和维护脚本一致。
- 不新增 raw 路径引用，不把外部图形或 AI 输出写成事实证据。

## Assumptions

- 课程对象仍为药学本科生。
- 继续沿用 Astro + Pagefind 在线教材，不切换技术栈。
- 下一轮仍以结构化可审查工件为主，不一次性补完 18 周完整教材正文或批量生成 PPTX。
- 发布仍通过当前 GitHub Pages workflow；公开图形和 PPTX 生成前必须完成 evidence review。
