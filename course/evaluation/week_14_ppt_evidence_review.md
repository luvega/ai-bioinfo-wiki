---
type: evidence-review
week: 14
title: Week 14 PPT Storyboard Evidence Review
status: evidence_review_pass
updated: 2026-06-04
---

# Week 14 PPT Storyboard Evidence Review

## Verdict

pass-for-storyboard-assets

Week 14 storyboard 的教学链条成立，可以作为 PPTX 前的审查稿。公开素材策略已收口：正式 PPT 优先使用教师自绘流程图和 generated teaching example，不直接复用外部教材、论文或网页图形。AIDD 上游流程中的命令名、软件名和文件格式仍需在进入 PPTX 脚本前逐项复核，但这不再阻塞 Coursebook 的 evidence review 状态。

## Findings

| Severity | Location | Issue | Fix |
|---|---|---|---|
| P1 | `course/weeks/week_14/ppt_storyboard.md` | FASTQ、SAM/BAM、count matrix 等流程表述需要进入 PPT 前复核原始来源 | 回查 AIDD `07_NGS_data_Analysis_on_Bash` 和课程主讲稿，保留来源说明 |
| P1 | storyboard visual intent | 上游流程不应直接复用外部图形 | 正式 PPT 默认使用教师自绘流程图；若引用外部图，必须重新降级为 source review |
| P2 | count matrix 示例 | 教学矩阵需要明确 generated teaching example | 在 PPT 图注和 speaker note 中标注教学模拟 |
| P2 | SCBP/OSCA/OSTA 对照 | 现代组学容器只适合结构对照，不应扩展成学生必跑 API | 保留 AnnData/SCE 为概念对照，避免 API 教程化 |

## Claim-Evidence Gate

| Claim | Evidence status | Action |
|---|---|---|
| RNA-seq 的课堂目标是理解表达矩阵来源 | supported by syllabus | 可保留 |
| FASTQ 到 count matrix 需要 QC、比对或计数等步骤 | supported with wording review before PPTX | 进入 PPTX 脚本前核 AIDD 和知识页术语 |
| count matrix 与 metadata 必须样本对齐 | supported by course week files | 可保留并作为课堂核验任务 |
| AnnData/SCE 可作为现代组学数据结构对照 | supported as extension | 只作教师备课和结构对照 |
| 总 counts 差异可能影响组间比较 | supported as teaching caution | 避免扩写成完整 normalization 课程 |

## Next Checks

1. 生成 PPTX 前核对 AIDD 上游流程材料中的命令名、软件名和文件格式。
2. 正式 PPT 默认使用自绘流程图和教学模拟矩阵，不直接引用外部图形。
3. 若进入 PPTX，先更新 storyboard，再做 PNG/contact sheet 视觉 QA。
