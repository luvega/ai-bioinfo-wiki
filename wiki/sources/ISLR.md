---
type: source
title: An Introduction to Statistical Learning, with Applications in R (ISLR)
authors: [Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani]
year: 2013 (1e) / 2021 (2e)
raw_path:
  - pdf_originals/An Introduction to Statistical Learning_ with Applications R--.pdf
  - sources/PDF_Library/An_Introduction_to_Statistical_Learning_with_Applications_R.md
ingested: 2026-05-21
language: en
kind: textbook
pages: 436
status: stable
tags: [statistical-learning, machine-learning, r, regression, classification]
---

# ISLR · An Introduction to Statistical Learning · R 版

## 一句话定位

[ISLP](ISLP.md) 的 R 版前身，**当课程进入 R 主导环节（第 4、11、12 周）时优先用它**，
labs 直接对应 R 语言风格，与 AIDD 第 9 章的 R 学习习惯一致。

## 与 ISLP 的差异

| 项 | ISLR | ISLP |
|---|---|---|
| Lab 语言 | R | Python |
| 章节 | 10 章（1e）/ 13 章（2e） | 13 章 |
| 与 AIDD Ch.9 配合 | ★★★ 直接对接 | ★ |
| 与 DESeq2 / 生信工作流 | ★★★ R 包风格相近 | ★★ |
| 与 scikit-learn / PyTorch 工作流 | ★ | ★★★ |

## 章节结构（与 ISLP 同步，仅 lab 不同）

略，详见 [ISLP](ISLP.md) 第 §"章节结构"。

## 在本课程中的重点用法

- **第 4 周（R 基础 + 数据框）**：ISLR Ch.2 §2.3 是经典 R 入门一节，配 `Auto`、`Boston` 数据集，
  可作上机示例。
- **第 9 周（相关与回归）**：用 R 的 `lm()` 给学生展示回归输出，配 ISLR Ch.3。
- **第 10 周（分类）**：`glm()`、`MASS::lda()`、`class::knn()`，对应 ISLR Ch.4。
- **第 13 周（机器学习入门）**：`tree`、`randomForest`、`gbm`、`xgboost`，对应 ISLR Ch.8。

## 适合的学生路径

- **如果学生 R 更熟悉**（药学 / 生统背景常见）→ 先看 ISLR labs，再看 ISLP 对照。
- **如果学生 Python 更熟悉** → 先看 ISLP，再用 ISLR 验证统计直觉与生信语境对接。

## 相关页面

- 姊妹版：[ISLP](ISLP.md)
- 配合学习：[AIDD 第 9 章 R for Bioinformatics](AIDD_Bioinformatics_Course.md)
- 课程总线：[36 课时讲稿](36课时讲稿.md)
