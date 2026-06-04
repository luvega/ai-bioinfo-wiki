---
week: 16
title: 单细胞与空间组学图形解读
ppt_status: storyboard
review_status: evidence_review_pass
---

# Week 16 PPT Storyboard：单细胞与空间组学图形解读

本 storyboard 只用于审查 Week 16 的图形解读路径和证据边界。当前状态是 `storyboard` 与 `evidence_review_pass`，尚未生成 PPTX，也尚未做 PNG/contact sheet 视觉 QA。

| Slide | Action title | Visual intent | Teacher note | Student action | Evidence/source note | Risk note |
|---:|---|---|---|---|---|---|
| 1 | 单细胞和空间图形帮助观察异质性，但图形不是结论 | 标题页，显示 cell、gene、spot 三个观测单位 | 先声明本周目标是读图和边界，不是跑完整 workflow | 写出“图形不是结论”的一个例子 | Week 16 `script.md` 讲义使用说明 | 不把 UMAP 或 spatial domain 写成机制证明 |
| 2 | cell x gene matrix 把观测单位从样本换成细胞 | 表格：bulk sample x gene vs cell x gene | 解释单细胞更细但更稀疏、更依赖 QC | 判断矩阵中一行代表样本还是细胞 | SCBP/OSCA data structure 备课 | 不默认学生理解 AnnData/SCE API |
| 3 | QC 图先回答细胞是否可靠 | 小型 QC 面板：nFeature、nCount、percent.mt | QC 是过滤和解释的前提 | 指出一个可能低质量细胞群 | SCBP QC、OSCA QC | 不把 QC 阈值写成通用医学标准 |
| 4 | PCA / UMAP / t-SNE 展示的是处理后结构 | UMAP 点图示意，颜色按 cluster | 解释点、颜色、cluster 标签分别代表什么 | 说出 UMAP 距离不能说明什么 | SCBP dimensionality reduction；Week 13 衔接 | 不把 UMAP 距离解释成真实生物距离 |
| 5 | cluster 与 marker gene 只能支持候选注释 | marker 表达小图 + 候选注释表 | 注释需要 marker、数据库、文献和上下文 | 给一个 cluster 写候选注释和待核验点 | SCBP annotation、OSCA marker/annotation | 不直接给最终细胞类型 |
| 6 | spatial spot / spatial domain 还多了一层空间位置 | spot 网格与 gene expression 热点示意 | 空间图回答位置模式，不自动证明病理区域 | 区分 spot、region、domain 三个词 | OSTA spatial QC/domain；SCBP spatial intro | 不把 spatial domain 写成确认病理区域 |
| 7 | 参数敏感性决定图形解释必须保留条件 | 参数卡：过滤阈值、PCA 维数、neighbors、resolution | 同一数据在不同参数下可能呈现不同结构 | 列出 3 个会影响结果的参数 | Week 16 `verificationPoints` | 不把单次参数结果写成唯一事实 |
| 8 | AI 协作只能生成解读表框架和核验清单 | Prompt + 四栏解读表 | AI 可帮整理语言，不能替代注释证据 | 修改一段过度解释为候选解释 | `knowledge/concepts/AI协作边界.md` | 不让 AI 编造 marker、细胞类型或机制 |

## Evidence Checklist

- 正式 PPT 默认使用自生成 QC、UMAP、marker、spatial 教学示意图；若改用外部图形，需重新进入 source review。
- SCBP/OSCA/OSTA workflow 不作为学生必跑任务，只作为图形阅读和教师备课素材。
- 所有 marker、cell type、spatial domain 和 mechanism 语句必须保留候选和待核验状态。
- Week 16 只进入 storyboard review，不宣称 PPTX 完成。
