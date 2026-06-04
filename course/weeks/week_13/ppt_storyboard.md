---
week: 13
title: PCA、聚类与热图
ppt_status: storyboard
review_status: evidence_review_pending
---

# Week 13 PPT Storyboard：PCA、聚类与热图

本 storyboard 只作为审查稿，不表示 PPTX 已生成。它服务 Week 13 在线教材样章候选，重点是把 Week 11 的图表证据边界和 Week 12 的矩阵结构直觉迁移到高维图形阅读。

| Slide | Action title | Visual intent | Teacher note | Student action | Evidence/source note | Risk note |
|---:|---|---|---|---|---|---|
| 1 | 高维图形先回答“看到了什么”，不是“证明了什么” | Week 11-13 微项目链条图 | 回顾图表证据边界和矩阵桥接 | 说出本周输入、输出和边界 | `course/weeks/week_11_13_micro_project.md` | 不把 PCA/UMAP 分离写成机制 |
| 2 | 同一张矩阵可以进入不同图形 | 6 samples x 5 features 教学矩阵 | 说明样本、变量、metadata | 标出观测单位和分组 | Week 12 教学矩阵 | 教学模拟不能写成真实实验 |
| 3 | PCA 把主要变异方向压缩到少数坐标 | PCA 坐标示意和 explained variance 表 | 强调 PC1/PC2 是数学方向 | 判断 PC1/PC2 能说明什么 | ISLP/ISLR 高维直觉，课堂模拟 | PC 不是天然医学指标 |
| 4 | 聚类标签依赖距离和参数 | 距离矩阵、树状图或 cluster 表 | 比较不同距离或参数可能改变分组 | 写出聚类前要记录的参数 | SCBP clustering 作为教师备课 | cluster 不是最终诊断或细胞类型 |
| 5 | 热图颜色显示模式，但受标准化和排序影响 | 标准化前后热图对照 | 解释颜色、尺度、行列排序 | 找出图注中必须说明的处理 | Week 12 标准化桥接 | 颜色不等于药效大小 |
| 6 | UMAP 适合探索结构，不代表真实生物距离 | UMAP 点图示意 | 说明点、颜色、cluster 和参数敏感性 | 改写一条过度解释的 UMAP 图注 | SCBP/OSCA/OSTA 作为拓展来源 | UMAP 邻近不等于真实距离 |
| 7 | bulk、single-cell、spatial 的观测单位不同 | 三类矩阵对比表 | 对比 sample、cell、spot | 填写三类图形能回答的问题 | `knowledge/sources/Single_Cell_Best_Practices.md`、`OSCA.md`、`OSTA.md` | 不混写三类 workflow 结论 |
| 8 | AI 只能检查解释是否越界 | AI 输出审查表 | 展示 Prompt 和人工修改 | 标记 AI 过度结论并改写 | `course/templates/ai_use_statement_template.md` | AI 不编造基因功能或机制 |
| 9 | 高维图形四栏表是本周出口证据 | 输入、观察、候选解释、待核验点表 | 用同一教学矩阵完成出口卡 | 提交四栏表和 AI 审计记录 | `course/evaluation/learning_outcome_matrix.md` | 缺少待核验点则不得进入 PPTX |

## Evidence Checklist

- 教学矩阵为 generated teaching example，不作为真实药物实验结果。
- SCBP/OSCA/OSTA 只作为教师备课和现代组学拓展来源，不要求学生运行完整 workflow。
- PCA、cluster、heatmap、UMAP 的解释必须包含输入、参数或标准化说明。
- 进入 PPTX 前需补齐可公开展示图形或保留为课程自生成示意图。
- 本周仍为 `sample_candidate`，不是 `pilot_ready` 或 PPT 完成状态。
