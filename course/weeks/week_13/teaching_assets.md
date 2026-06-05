---
type: teaching-assets
week: 13
title: Week 13 教学矩阵与高维图形资产
status: pilot_ready_asset
updated: 2026-06-04
---

# Week 13 教学矩阵与高维图形资产

本文件为 Week 13 的可公开教学资产说明。所有数据均为 generated teaching example，只用于课堂解释 PCA、聚类、热图和 UMAP 的输入输出与证据边界，不代表真实药物实验结果。

## 可复现图形生成

- 脚本：[Week 13 教学图形生成脚本](../../../scripts/courseware/build_week13_teaching_figures.py)。
- 输出目录：`outputs/teaching_figures/week_13/`，不进入 Git。
- 输出文件：`week13_pca.svg`、`week13_cluster.svg`、`week13_heatmap.svg`、`week13_umap.svg`。
- 依赖：Python 标准库；固定模拟数据；无需外部图片或商业素材。
- 课堂边界：生成图只用于解释高维图形读法，不作为真实分析结果、机制结论或 PPTX 完成证据。

## 教学矩阵

| sample_id | group | batch | GeneA | GeneB | GeneC | GeneD | GeneE |
|---|---|---|---:|---:|---:|---:|---:|
| Ctrl_1 | Control | B1 | 10 | 8 | 4 | 5 | 7 |
| Ctrl_2 | Control | B1 | 11 | 7 | 5 | 4 | 6 |
| Ctrl_3 | Control | B2 | 9 | 8 | 4 | 5 | 7 |
| Drug_1 | Drug | B1 | 17 | 5 | 8 | 6 | 4 |
| Drug_2 | Drug | B2 | 16 | 4 | 9 | 7 | 5 |
| Drug_3 | Drug | B2 | 18 | 5 | 8 | 6 | 4 |

课堂使用方式：

- 行是样本，列是基因或指标。
- `group` 是教学分组，`batch` 用于提醒学生批次信息可能影响图形。
- 进入 PCA、聚类和热图前，教师必须说明是否标准化，以及标准化改变的是图形距离和颜色尺度，不是生成新的医学事实。

## PCA 坐标表

下表是教学示意坐标，用于说明 PCA 输出结构，不作为真实计算结果引用。正式 PPT 若要保留数值，应重新用脚本从教学矩阵生成并保存参数。

| sample_id | group | PC1 | PC2 | note |
|---|---|---:|---:|---|
| Ctrl_1 | Control | -1.9 | 0.2 | Control 样本在 PC1 左侧聚集 |
| Ctrl_2 | Control | -1.7 | -0.1 | 与 Ctrl_1 接近 |
| Ctrl_3 | Control | -2.0 | 0.0 | batch B2 不应被忽略 |
| Drug_1 | Drug | 1.8 | 0.1 | Drug 样本在 PC1 右侧聚集 |
| Drug_2 | Drug | 1.6 | -0.3 | 与 Drug_3 接近 |
| Drug_3 | Drug | 2.2 | 0.1 | 需要检查是否由 GeneA/GeneC 驱动 |

图注建议：

> 教学模拟 PCA 图显示 Drug 与 Control 样本在 PC1 方向上有分离趋势；该图只能提示主要变异方向，不能单独证明药效机制。

必须保留的待核验点：

- PCA 是否基于标准化矩阵。
- PC1/PC2 解释方差比例。
- batch 是否与 group 混杂。
- 分离趋势是否由少数特征主导。

## 聚类参数表

| 参数 | 教学默认值 | 课堂解释 |
|---|---|---|
| 输入矩阵 | z-score 后的 sample x gene matrix | 避免 GeneA 的数值尺度主导距离 |
| 距离度量 | Euclidean distance | 只表示当前处理后的数学距离 |
| 聚类方法 | complete linkage | 不同 linkage 可能改变树状图 |
| 切树规则 | 2 clusters | 只用于课堂分组示意 |
| 输出标签 | Cluster 1 / Cluster 2 | 不是最终诊断、细胞类型或机制标签 |

## 热图说明

热图应采用标准化后的矩阵，并在图注中说明：

- 颜色表示标准化后的相对高低，不是原始表达量或药效大小。
- 行列排序由距离和聚类方法决定。
- 同一颜色模式可以提出候选解释，但必须回到原始矩阵、metadata 和统计分析核验。

## UMAP 示意说明

Week 13 的 UMAP 只作为现代组学图形阅读预告：

- 点可以代表细胞或 spot，取决于输入矩阵。
- 点的局部邻近关系受预处理、PCA 维度、neighbors、min_dist 和随机种子影响。
- cluster 或 spatial domain 只能写成候选结构，不可写成最终细胞类型、病理区域或药物机制。

## 图形参数与风险提示

| 图形 | 输入 | 参数或处理 | 必须显示的风险提示 |
|---|---|---|---|
| PCA | 教学矩阵 | 使用脚本中固定教学坐标展示 PC1/PC2 结构 | 只提示主要变异方向，不证明机制 |
| 聚类 | z-score 后矩阵 | Euclidean distance + complete linkage | cluster 标签依赖参数，不是诊断或机制标签 |
| 热图 | 6 samples x 5 genes 矩阵 | 教学色阶；正式 PPT 需说明标准化 | 颜色显示模式，不是原始表达量或药效大小 |
| UMAP | 教学坐标 | 用于现代组学图形预告 | 点距和 cluster 不代表真实生物距离 |

## AI 审查 Prompt

```text
请审查下面这段 PCA/聚类/热图/UMAP 图注是否过度解释。
要求：
1. 标出哪些句子只是图上观察。
2. 标出哪些句子已经变成机制或医学结论。
3. 检查是否说明输入矩阵、标准化、距离或参数。
4. 生成 3 个必须人工核验的问题。
不要编造基因功能、药效机制、样本量、P 值或数据来源。
```
