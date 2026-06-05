# AI_Course 状态与术语词典

本文统一解释课程大纲、教学计划、PPT storyboard、教材章节和教学审查状态。状态只描述所属轴，不允许跨轴推断。

## 产物术语

| 术语 | 对应文件 | 回答的问题 | 禁止误用 |
|---|---|---|---|
| 课程大纲 | `course/weeks/week_XX/outline.md` | 本周教什么、为什么教、放在 18 周主线中的位置。 | 不承担 90 分钟逐段教学组织。 |
| 教学计划 | `course/weeks/week_XX/teaching_plan.md` | 90 分钟怎么教、学生每段做什么、课堂产物和评价证据是什么。 | 不替代教材正文，不作为 PPT 页级源稿。 |
| PPT storyboard | `course/weeks/week_XX/ppt_storyboard.md` | 40 页主干投屏源稿如何呈现、每页 Student action 和 Timing 是什么。 | 不等于最终投屏页数，不表示 PPTX 或视觉 QA 完成。 |
| 教材章节 | `course/textbook/chapters/chapter_XX.md` | 知识体系如何组织、学生如何课前预习和课后复习。 | 不逐页复述 storyboard，不承担课堂时间组织。 |

## textbook_status

| 状态 | 含义 | 禁止误用 |
|---|---|---|
| `draft_needs_assets` | 章节正文有草稿，但缺少至少一类可入库素材资产。 | 不表示可以进入 PPT。 |
| `full_draft` | 章节正文初稿完整，有基础素材入口。 | 不表示已完成 40 页 storyboard。 |
| `expanded_draft` | 章节已按 40 页主干 storyboard 扩写，适合人工精修。 | 不表示试讲完成或 PPTX 完成。 |

## ppt_status

| 状态 | 含义 | 禁止误用 |
|---|---|---|
| `not_started` | 尚未启动 PPT 生产线。 | 不因讲义完成自动提升。 |
| `storyboard` | 已有可审查 storyboard 或 brief。 | 不表示 PPTX 已生成。 |
| `storyboard_expanded` | 已有 40 页主干 storyboard 源稿，并包含 Student action 和 Timing。 | 不表示最终投屏页数、PPTX、PNG 预览或视觉 QA 完成。 |
| `storyboard_reviewed` | storyboard 已完成专项 evidence review。 | 不表示视觉 QA 完成。 |
| `pptx_trial_done` | 已生成试点 PPTX。 | 只对对应版本有效，storyboard 改版后需重新生成和 QA。 |

## review_status

| 状态 | 含义 | 禁止误用 |
|---|---|---|
| `pilot_candidate` | 周次材料、讲义、教材和 storyboard 具备试讲候选基础。 | 不表示人工试讲通过。 |
| `pilot_ready` | 已完成较充分的教学结构和证据边界审查，可进入试讲或 PPTX 前置准备。 | 不表示 PPTX 完成。 |
| `sample_ready` | 在线样章可读，具备导入问题、目标、概念、案例和边界说明。 | 不表示全周所有素材已最终定稿。 |
| `evidence_review_pass` | 关键证据、图表和公开素材策略已通过专项审查。 | 不替代视觉 QA 或课堂试讲反馈。 |

## 当前基线

- 18 周 `textbook_status` 统一为 `expanded_draft`。
- 18 周 `ppt_status` 统一为 `storyboard_expanded`。
- 18 周均新增 `teaching_plan.md`，用于承载 90 分钟课堂组织、学生动作、课堂产物和评价证据。
- Coursebook 只作为教材章节和知识体系入口；Courseware / Teaching Plan 入口承载教学计划和 storyboard 审核。
- Week 03/05/08/11/12/13/15/16/18 是 storyboard 去模板化重点精修周。
- 本轮不生成 PPTX、PNG、contact sheet，也不把 40 页主干源稿等同于最终投屏课件。
