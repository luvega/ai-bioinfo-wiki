---
type: evidence-review
week: 16
title: Week 16 PPT Storyboard Evidence Review
status: evidence_review_pass
updated: 2026-06-04
---

# Week 16 PPT Storyboard Evidence Review

## Verdict

pass-for-storyboard-assets

Week 16 storyboard 的教学定位合理：面向药学本科生训练 QC、UMAP、cluster、marker 和 spatial 图形的阅读边界。公开素材策略已收口：正式 PPT 优先使用自生成教学示意图或教师自绘图形，不直接复用外部 workflow 图。marker、cell type、spatial domain 仍必须保留候选和待核验语言。

## Findings

| Severity | Location | Issue | Fix |
|---|---|---|---|
| P1 | `course/weeks/week_16/ppt_storyboard.md` | UMAP、cluster、marker、spatial domain 容易被学生理解为最终生物学结论 | 每页 risk note 保留“候选解释”和“待核验”语言 |
| P1 | visual examples | QC/UMAP/marker/spatial 图若来自外部材料，需要确认数据来源和授权 | 正式 PPT 默认使用自生成示意图；若引用外部图，必须重新进入 source review |
| P1 | marker gene explanation | marker 不能直接推出最终细胞类型 | 要求学生写“候选细胞类型，需要 marker 组合/数据库/文献核验” |
| P2 | spatial interpretation | spatial domain 不能写成病理区域或机制事实 | 保留空间模式、候选区域和待核验措辞 |
| P2 | student workload | 不要求运行完整 SCBP/OSCA/OSTA workflow | PPT 只保留图形阅读、参数敏感性和证据边界 |

## Claim-Evidence Gate

| Claim | Evidence status | Action |
|---|---|---|
| 单细胞矩阵以 cell x gene 为主要观测结构 | supported as teaching simplification | 可保留，避免展开稀疏矩阵工程细节 |
| QC 指标可提示低质量细胞或异常细胞群 | supported as caution | 需说明不能单靠一个阈值自动删除 |
| UMAP 展示探索性邻近结构，不是真实生物距离 | supported | 必须进入 PPT 风险提示 |
| marker gene 支持候选注释 | supported with verification required | 禁止写成最终注释 |
| spatial domain 代表空间模式候选 | supported as teaching schematic | 仅用自生成示意图或授权图形，保留候选语言 |

## Next Checks

1. 正式 PPT 默认准备自生成 QC、UMAP、marker 和 spatial 教学示意图。
2. 为每张图补参数敏感性说明：过滤阈值、PCA 维度、邻居图、resolution 或 spatial method。
3. 进入 PPTX 前再次运行 evidence review，并在导出 PNG/contact sheet 后做视觉 QA。
