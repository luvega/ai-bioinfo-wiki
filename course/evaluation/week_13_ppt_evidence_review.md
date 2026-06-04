---
type: evidence-review
week: 13
title: Week 13 PPT Storyboard Evidence Review
status: pilot_ready_evidence_pass
updated: 2026-06-04
---

# Week 13 PPT Storyboard Evidence Review

## Verdict

pass-for-pilot-ready

Week 13 storyboard 已具备进入可授课试点的教学条件：教学矩阵、PCA 坐标表、聚类参数表、热图说明、UMAP 误读边界和可复现 SVG 生成脚本均已落到 [Week 13 教学矩阵与高维图形资产](../weeks/week_13/teaching_assets.md) 与 [Week 13 教学图形生成脚本](../../scripts/courseware/build_week13_teaching_figures.py)。当前结论支持 `pilot_ready` 和 `storyboard_reviewed`，仍不支持宣称 PPTX 完成。

## Findings

| Severity | Location | Issue | Fix |
|---|---|---|---|
| P1 | `course/weeks/week_13/ppt_storyboard.md` | PCA、cluster、heatmap 和 UMAP 都容易被学生读成机制结论 | 每页保留“图上观察、候选解释、待核验点”语言 |
| P1 | `course/weeks/week_13/teaching_assets.md` | PCA 坐标表为教学示意，不是真实计算输出 | 图注必须写明 generated teaching example；正式 PPT 若保留数值，应由脚本重新生成 |
| P1 | UMAP 讲解 | UMAP 点距、cluster 和 spatial domain 容易被写成真实生物距离或病理区域 | 只作为现代组学图形阅读预告，保留参数敏感性和候选状态 |
| P2 | 聚类参数 | 聚类输出依赖距离、标准化和 linkage | 在 storyboard 与后续 PPT 图注中固定显示参数表 |
| P2 | AI 审查 | AI 可改写图注但可能编造机制 | 使用固定 Prompt 要求 AI 只做越界检查和待核验清单 |
| P2 | 图形生成 | 教学图需避免外部版权和不可复现截图 | 使用标准库脚本生成 SVG 到 `outputs/teaching_figures/week_13/` |

## Claim-Evidence Gate

| Claim | Evidence status | Action |
|---|---|---|
| 教学矩阵可用于解释 PCA、聚类和热图的输入输出 | supported by generated teaching asset and script | 可进入试讲 |
| PCA 分离提示主要变异方向 | supported as visualization observation | 必须写成观察，不写成药效机制 |
| cluster 标签依赖标准化、距离和参数 | supported by storyboard and parameter table | 可进入 PPT storyboard |
| 热图颜色显示模式但受标准化和排序影响 | supported as visualization caution | 可进入 PPT storyboard |
| UMAP 用于探索结构，不代表真实生物距离 | supported as course caution | 必须进入风险提示 |
| SCBP/OSCA/OSTA 可作为学生必跑 workflow | not supported | 禁止；只保留教师备课和图形阅读拓展 |

## Next Checks

1. 若生成 PPTX，使用脚本重新生成 SVG 或从 SVG 转入正式模板，避免手写坐标被误解为真实分析。
2. PPT 图注必须标注 generated teaching example，并显示标准化、距离或参数。
3. PPTX 生成后仍需导出 PNG/contact sheet，检查文字溢出、图形可读性和状态标签。

## Pilot-Ready Boundary

- 支持：Week 13 `materials.md` 与 `outline.md` 升为 `pilot_ready`。
- 支持：Coursebook 显示 Week 13 为样章可读和试讲就绪。
- 不支持：宣称 Week 13 已有 PPTX、PNG/contact sheet QA 或真实组学分析结果。
