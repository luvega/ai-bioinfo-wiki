---
type: source
title: An Introduction to Statistical Learning, with Applications in Python (ISLP)
authors: [Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, Jonathan Taylor]
year: 2023
raw_path:
  - materials/raw/pdf_originals/An Introduction to Statistical Learning_ with Applications Python.pdf
  - materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python/book.mineru.md
  - materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python/book.course.md
ingested: 2026-05-21
language: en
kind: textbook
pages: 613
status: stable
tags: [statistical-learning, machine-learning, python, regression, classification, resampling, deep-learning, survival]
---

# ISLP · An Introduction to Statistical Learning · Python 版

## 一句话定位

**本课程统计学习与机器学习部分的首选教材**——
偏应用、不重数学推导，配 Python lab。
与 R 版 [ISLR](ISLR.md) 同结构，差异仅在实验代码语言。

## 谁写的、面向谁

- 作者：ISLR 原班人马（James / Witten / Hastie / Tibshirani）+ 新增 Jonathan Taylor 写 Python labs。
- 面向：高年级本科 / 硕士 / 想用统计学习工具的非统计专业人员。
- 数学要求：弱（高于 Khan-academy 级，远低于 ESL）。
- 配套：`ISLP` Python 包（CRAN 名义上对应 R 的 `ISLR2`）。

## 章节结构（13 章）

| Ch | 内容 | 课程中的位置 |
|---:|---|---|
| 1 | Introduction | 第 1 周可引一段“统计学习的工作链”示意图 |
| 2 | Statistical Learning（监督/无监督/偏差-方差） | 第 10 周（分类入门）/ 第 13 周（ML 入门） |
| 3 | Linear Regression | 第 9 周（相关与回归） |
| 4 | Classification（logistic / LDA / QDA / Naive Bayes / KNN） | 第 10 周 |
| 5 | Resampling Methods（CV / bootstrap） | 第 13 周 |
| 6 | Linear Model Selection & Regularization（Lasso/Ridge） | 第 13 周扩展 |
| 7 | Moving Beyond Linearity（splines / GAM） | 选讲 |
| 8 | Tree-Based Methods（CART / RF / Boosting） | 第 13 周 |
| 9 | SVM | 第 13 周扩展 |
| 10 | Deep Learning（PyTorch lab） | 选讲（药学课程不展开） |
| 11 | Survival Analysis & Censored Data | 第 16 周扩展（医药数据高相关） |
| 12 | Unsupervised Learning（PCA / clustering） | 第 12、13 周 |
| 13 | Multiple Testing（Bonferroni / Benjamini-Hochberg） | **第 8、15 周必讲**（差异表达里 FDR） |

## 在本课程中的重点用法

- **第 8 周（假设检验）**：Ch.13 提供"为什么需要 FDR、Bonferroni vs BH"的最简明讲法。
- **第 9 周（相关与回归）**：Ch.3 是教科书级的回归说明，可直接做 PPT 素材来源。
- **第 10 周（多元统计与分类入门）**：Ch.4 KNN/logistic + Ch.2 偏差-方差权衡是核心。
- **第 15 周（差异表达 + DESeq2）**：Ch.13 多重检验，配合 [DESeq2](../entities/DESeq2.md) 的 BH 校正。
- **第 12 周（高维可视化）**：Ch.12 PCA、K-means、Hierarchical clustering，配合表达矩阵案例。
- **第 13 周（机器学习入门）**：Ch.2 / Ch.5 / Ch.8（树/RF）是骨架。
- **第 16 周（生存分析）**：Ch.11，医药数据中极常用，需补例。

## 与 AIDD 的互补

AIDD 在第 9 章直接进入 DESeq2 调用，缺“为什么是负二项分布、多重检验怎么校正、
模型评估指标怎么读”这一层。**ISLP 的 Ch.2、Ch.4、Ch.13 正好补上**。
两者搭配：ISLP 给理论与图，AIDD 给命令与数据。

## 关键概念地图（待展开）

> 待 ingest 到具体的 concepts 页：
>
> - `concepts/偏差_方差权衡.md`
> - `concepts/正则化_Lasso_Ridge.md`
> - `concepts/交叉验证.md`
> - `concepts/PCA与聚类.md`
> - `concepts/多重检验校正.md`
> - `concepts/生存分析.md`

## 相关页面

- 姊妹版：[ISLR](ISLR.md)
- 三本 Python 书对比：[synthesis/三本Python书定位对比](../synthesis/三本Python书定位对比.md)
- 课程总线：[36 课时讲稿](36课时讲稿.md)

## 勘误 / 注意

- MinerU 转换结果以 `book.mineru.md` 为完整解析层，`book.course.md` 为备课整理层；旧版轻量转换已退役。
- 引用具体公式或图表时，请回到 `materials/raw/pdf_originals/An Introduction to Statistical Learning_ with Applications Python.pdf` 找页码。
