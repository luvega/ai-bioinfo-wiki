---
type: course-week
week: 12
title: 高维数据与数学直觉
hours: 2
status: pilot_candidate
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 12 周：高维数据与数学直觉 · PPT 大纲

## 教学目标

- 解释临床表格、样本 x 指标矩阵、表达矩阵之间的关系。
- 识别矩阵中的观测单位、变量、metadata、缺失值和尺度差异。
- 说明标准化、距离和高维图形之间的联系。
- 为 Week 13 的 PCA、聚类和热图建立输入输出直觉。

## PPT 结构

1. 导入问题：为什么一张普通临床表格会变成矩阵？
2. 数据桥接：临床表格数据 -> 样本 x 指标矩阵 -> 表达矩阵 -> PCA/cluster/heatmap。
3. 核心概念：matrix、metadata、sample、feature、scaling、distance。
4. 课堂示例：6 samples x 5 genes 教学矩阵。
5. 标准化前后距离为什么改变。
6. AI 协作边界：解释矩阵可以，解释机制不行。
7. 小结与作业：为 Week 13 准备矩阵读图卡。

## 已对齐素材

- 课程主讲稿：[课程教学讲稿](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)
- AIDD count matrix / metadata 相关材料。
- ISLP/ISLR 中矩阵、标准化、距离、高维数据直觉素材。
- SCBP/OSCA 的 AnnData/SCE 只作为教师备课，不展开对象 API。

## 课堂任务

学生用一个 6 samples x 5 genes 的教学矩阵，手工识别行、列、分组变量、缺失值、尺度差异，再解释为什么热图颜色不是原始医学结论。

可直接使用 [Week 11-13 连续微项目课堂表格](../week_11_13_classroom_tables.md) 中的“临床表格 -> 样本 x 指标矩阵 -> metadata”表。学生必须能把 `group`、`batch` 与表达矩阵分开说明，并指出 metadata 对齐错误会怎样影响后续 PCA、聚类和热图。

## 连续微项目接口

本周是 [Week 11-13 连续微项目](../week_11_13_micro_project.md) 的矩阵桥接环节。Week 11 的图表边界表在本周转为样本 x 指标矩阵，Week 13 将继续使用同一矩阵解释 PCA、聚类、热图和 UMAP。

## AI协作边界

- 允许：把矩阵结构解释成表格语言，生成检查清单。
- 禁止：把标准化后的颜色差异写成药效机制或疾病机制。

## 课后练习

给出一张小型表达矩阵和 metadata，写出三句话：数据结构、可视化前处理、不能过度解释的地方。
