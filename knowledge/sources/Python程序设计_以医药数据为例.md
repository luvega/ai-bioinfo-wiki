---
type: source
title: Python程序设计-以医药数据为例
authors: [赵鸿萍, 张艳敏]
publisher: 清华大学出版社
year: 2022
isbn: 978-7-302-61858-4
raw_path:
  - materials/raw/pdf_originals/Python程序设计-以医药数据为例.pdf
  - materials/markdown/pdf_library_local_text/Python_Programming_Medical_Data/book.fulltext.md
  - materials/markdown/pdf_library_local_text/Python_Programming_Medical_Data/extraction_report.md
ingested: 2026-06-05
language: zh
kind: textbook
pages: 335
status: source_ingested
tags: [python, pharmacy-data, data-processing, visualization, pubchem, pandas, matplotlib, ocr]
---

# Python程序设计-以医药数据为例

## 一句话定位

中文 Python 入门与医药数据处理案例教材，适合作为本课程第 3 周 Python 入门、第 5-7 周数据处理与可视化，以及第 17 周综合项目的本土化案例来源。

## 入库结果

- 原始 PDF：`materials/raw/pdf_originals/Python程序设计-以医药数据为例.pdf`
- OCR 全文：`materials/markdown/pdf_library_local_text/Python_Programming_Medical_Data/book.fulltext.md`
- 提取报告：`materials/markdown/pdf_library_local_text/Python_Programming_Medical_Data/extraction_report.md`
- 方法：Tesseract 本地 OCR，`chi_sim+eng`，220 DPI，PSM 3，335/335 页，约 35.7 万字符。

## 内容结构

本书分为 Python 入门、Python 进阶和 Python 实战医药数据处理专题三部分。前两部分覆盖 Python 基础语法、控制结构、函数、字符串、文件、异常、标准库和第三方库；实战部分围绕 PubChem 药物结构数据采集、药物相似度、基因表达数据聚类热图、化合物水溶性预测、心脏病风险识别、黑色素瘤图像识别和电子病历实体识别等案例。

## 在本课程中的重点用法

- **Week 03**：中文 Python 基础语法、变量、条件、循环和函数示例。
- **Week 05-06**：数据采集、清洗、字符串、文件和表格处理的医药场景。
- **Week 07**：matplotlib、词云和药品销售数据可视化等案例。
- **Week 09-10**：回归、随机森林、神经网络和分类案例可作为概念引入，不作为算法细节主教材。
- **Week 13-15**：基因表达数据聚类热图可作为高维数据和组学数据的桥接案例。
- **Week 17**：可作为学生综合项目的中文案例池，尤其适合“从网页或表格得到可视化结果”的项目链路。

## OCR 核验边界

- 该 PDF 无文本层，全文来自 OCR；用于检索和备课定位是可用的，但代码、表格、公式和专有名词需要回原始 PDF 人工核验。
- OCR 中可能存在形近字、标点、代码字符、英文函数名和页眉页脚误识别；进入课件或教材正文前不得直接照搬。
- 若与 `course/syllabus/` 或周次文件冲突，以课程主线为准。
