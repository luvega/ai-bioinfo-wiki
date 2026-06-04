---
type: course-week
week: 13
title: PCA、聚类与热图
hours: 2
status: sample_candidate
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 13 周：PCA、聚类与热图 · PPT 大纲

## 教学目标

- 说明高维数据为什么需要降维、聚类和热图辅助观察。
- 解释 PCA、聚类和热图分别需要什么输入、输出什么结果。
- 区分表格矩阵、bulk expression matrix、single-cell cell x gene matrix 和 spatial spot x gene matrix。
- 识别 PCA/UMAP/cluster/heatmap 的常见误读风险，并记录参数和待核验点。

## PPT 结构

1. 导入问题：为什么同一批表达数据需要 PCA、聚类和热图来辅助理解？
2. 高维数据为什么需要降维。
3. PCA、聚类和热图的输入输出。
4. 从 bulk 到 single-cell 的数据结构差异。
5. 现代组学拓展：SCBP/OSCA/OSTA 只作为图形和流程阅读。
6. AI 协作边界与待核验点。
7. 出口卡：一张图能说什么，不能说什么？

## 待抽取素材

- 课程主讲稿：[课程教学讲稿](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)
- [SCBP 降维章节](../../../materials/markdown/sc_best_practices/analysis_project/chapters/11_preprocessing_visualization_dimensionality_reduction/chapter.source.md)
- [SCBP 聚类章节](../../../materials/markdown/sc_best_practices/analysis_project/chapters/12_cellular_structure_clustering/chapter.source.md)
- [OSCA](../../../knowledge/sources/OSCA.md) 和 [OSTA](../../../knowledge/sources/OSTA.md) 作为教师备课和现代组学拓展。

## 课堂任务

学生填写“高维图形四栏表”：输入矩阵是什么、图上观察是什么、可能解释是什么、必须核验什么。课堂样例使用教学矩阵，不把 UMAP/cluster 直接写成细胞类型事实。

## 连续微项目接口

本周完成 [Week 11-13 连续微项目](../week_11_13_micro_project.md) 的高维图形判读环节。学生必须能把 Week 11 的图表证据边界、Week 12 的矩阵结构说明，迁移到 PCA、聚类、热图和 UMAP 的输入输出解释。

## AI协作边界

- 允许：检查解释是否遗漏标准化、距离、参数和不确定性。
- 禁止：把热图颜色写成药效机制，把 cluster/UMAP 写成最终细胞类型或空间病理区域。

## 课后练习

从 PCA、热图、UMAP 三类图中任选一种，写一段不超过 150 字的图形解释，并列出 3 个待核验点。
