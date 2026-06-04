---
type: course-week
week: 12
title: 高维数据与数学直觉
hours: 2
status: draft
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 12 周：高维数据与数学直觉 · 素材映射

## 课程源文件

- [正式 docx](../../syllabus/36课时-AI前置调整版.docx)
- [主讲稿 Markdown](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)

## AIDD 候选素材

- 从 [AIDD 课程索引](../../../materials/markdown/aidd_bioinformatics/aidd.course_index.md) 和相关 `chapter.course.md` 选取；字幕原文只作术语核验，不直接进入课堂。

## PDF / 外部 PPT 候选素材

- 从 `materials/markdown/pdf_library_mineru/` 和 `materials/markdown/pdf_library_skill_extract/` 选取已转换 Markdown；原始 PDF/PPT 不直接进入课程引用。

## 素材分层使用原则（2026-06-04）

- 课堂主素材：矩阵、标准化、距离和高维数据直觉。
- 支撑素材：AIDD count matrix、DESeq2 metadata、ISLP/ISLR 高维和矩阵背景。
- 拓展素材：AnnData/SCE 只作高维数据容器预告，不展开对象 API。
- 教师备课素材：准备临床矩阵到表达矩阵的桥接图。
- 教材 / PPT 边界：可进 PPT：样本 x 变量矩阵、标准化前后距离对比。

## 可进 PPT 的元素

- 概念图：临床表格数据 -> 样本 x 指标矩阵 -> 表达矩阵 -> PCA/cluster/heatmap。
- 示例表格：6 samples x 5 genes 教学矩阵，配套 metadata、缺失值和尺度差异。
- 代码片段：只保留矩阵转置、标准化前后比较或距离计算的最小伪代码。
- AI 提示词：要求 AI 解释矩阵、标准化和距离，不得把热图颜色解释为药效机制。

## 本轮升级重点（2026-06-04）

- Week 12 是从普通医药表格进入表达矩阵和高维图形的桥接周。
- AIDD count matrix、DESeq2 metadata、ISLP/ISLR 高维直觉作为支撑素材；AnnData/SCE 只作数据容器预告。
- 学生需要能指出：行是什么观测单位，列是什么变量，metadata 如何与矩阵对齐，为什么标准化会改变距离和热图颜色。
- 待核验：任何真实表达矩阵示例进入课堂前必须确认来源、单位、是否 log/normalized、样本分组含义。

## 连续微项目接口

- 本周是 [Week 11-13 连续微项目](../week_11_13_micro_project.md) 的第 2 步。
- 课堂交付物：矩阵结构说明表，至少包含观测单位、变量、metadata、缺失/尺度问题和标准化必要性。
- 与 Week 13 的衔接：同一个教学矩阵进入 PCA、聚类和热图解释，避免学生每周重新理解一个新案例。
