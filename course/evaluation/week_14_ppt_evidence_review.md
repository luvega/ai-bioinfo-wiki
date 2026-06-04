---
type: evidence-review
week: 14
title: Week 14 PPT Storyboard Evidence Review
status: evidence_review_assets_pending
updated: 2026-06-04
---

# Week 14 PPT Storyboard Evidence Review

## Verdict

revise-before-ppt

Week 14 storyboard 的教学链条成立，可以作为 PPTX 前的审查稿；但进入正式 PPTX 前仍需核对 AIDD 上游流程中的命令名、软件名、文件格式表述，并补齐可公开展示图形或明确使用自生成教学示意图。

## Findings

| Severity | Location | Issue | Fix |
|---|---|---|---|
| P1 | `course/weeks/week_14/ppt_storyboard.md` | FASTQ、SAM/BAM、count matrix 等流程表述需要进入 PPT 前复核原始来源 | 回查 AIDD `07_NGS_data_Analysis_on_Bash` 和课程主讲稿，保留来源说明 |
| P1 | storyboard visual intent | 上游流程若使用真实工具截图或流程图，需要确认授权和图注边界 | 优先使用教师自绘流程图；若引用外部图，补来源和授权 |
| P2 | count matrix 示例 | 教学矩阵需要明确 generated teaching example | 在 PPT 图注和 speaker note 中标注教学模拟 |
| P2 | SCBP/OSCA/OSTA 对照 | 现代组学容器只适合结构对照，不应扩展成学生必跑 API | 保留 AnnData/SCE 为概念对照，避免 API 教程化 |

## Claim-Evidence Gate

| Claim | Evidence status | Action |
|---|---|---|
| RNA-seq 的课堂目标是理解表达矩阵来源 | supported by syllabus | 可保留 |
| FASTQ 到 count matrix 需要 QC、比对或计数等步骤 | needs source wording review | 进入 PPT 前核 AIDD 和知识页术语 |
| count matrix 与 metadata 必须样本对齐 | supported by course week files | 可保留并作为课堂核验任务 |
| AnnData/SCE 可作为现代组学数据结构对照 | supported as extension | 只作教师备课和结构对照 |
| 总 counts 差异可能影响组间比较 | supported as teaching caution | 避免扩写成完整 normalization 课程 |

## Next Checks

1. 核对 AIDD 上游流程材料中的命令名、软件名和文件格式。
2. 决定正式 PPT 使用自绘流程图还是已授权图形。
3. 若进入 PPTX，先更新 storyboard，再做 PNG/contact sheet 视觉 QA。
