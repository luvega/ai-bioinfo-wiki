---
type: concept
title: 工具分工 · Python / R / Bash
status: stable
tags: [tooling, python, r, bash, course-design]
---

# 工具分工：Python / R / Bash

## 一句话

**Python 是通用工具箱、R 是统计工作台、Bash 是流水线胶水**。
本课程不要求学生一次掌握全部，但要求理解"哪类任务用哪类工具"。

## 三张牌一句话

| 工具 | 强项 | 弱项 | 课程中的位置 |
|---|---|---|---|
| **Python** | 通用脚本、应用开发、机器学习、文本处理 | 统计绘图风格不如 ggplot2 | 第 3、5-7、10、13、17-18 周 |
| **R** | 统计建模、统计图、生信包（DESeq2 / ggplot2 / Seurat） | 工程化、应用开发 | 第 4、8-12、14-16 周 |
| **Bash** | 批量文件处理、流水线、生信命令行工具串联 | 不适合做复杂逻辑 | 第 2、5 周（导论）+ 第 16 周（pipeline） |

## 在 AIDD 中的体现

来源：[AIDD Ch.1 Powerhouse Trio of Bioinformatics](../sources/AIDD_Bioinformatics_Course.md)。
课程明确把这三者称作"Powerhouse Trio"：

- Python → Biopython、数据库访问、应用开发、机器学习入门（[Biopython](../entities/Biopython.md)、Ch.2、Ch.3）
- R → 包管理、DESeq2、ggplot2、scRNA-seq、Microarray（Ch.9、Ch.10）
- Bash → 命令行流程、NCBI E-utilities、BLAST、RNA-seq、Variant Calling（Ch.4、Ch.6、Ch.7、Ch.8）

## 在 36 课时课程中的体现

来源：[36 课时讲稿](../sources/36课时讲稿.md)。

- 第 3 周：Python 入门（变量、列表、字典、条件、循环）
- 第 4 周：R 入门（向量、矩阵、数据框、因子）
- 第 5-6 周：以 Python 主导数据清洗、整形（pandas）
- 第 7-10 周：Python 和 R 并行讲统计与可视化
- 第 11 周起：差异表达进入 **R 主导**（DESeq2 + ggplot2）
- 第 16 周：组学分析可以选择 R 或 Python，但若涉及 NGS pipeline，建议引入 Bash 概念

## 教师注意

- **不要在第 1-3 周就让学生选边站**：让学生先了解三者各自擅长什么，再根据上机案例选用。
- **R/Python 数据结构对应**：第 4 周必须强调
  - Python list ↔ R vector（同类型 vs 弱类型）
  - Python pandas.DataFrame ↔ R data.frame
  - Python dict ↔ R named list
- **Bash 不要硬讲**：本课程不是生信课，**Bash 只做"流程思维"的载体**，把命令行示例
  放到 WSL 演示中，不要求学生记住 grep/awk 细节。

## 与 AI 协作

- Python 代码：AI 生成的代码相对易读，但需检查类型与边界（None、NaN、空字符串）。
- R 代码：AI 生成的 R 代码常见错误是把分类变量当连续变量、把数据框列名拼错，参见 36 课时第 4 周。
- Bash：AI 给的命令行流程可能版本不匹配，**永远不要直接复制粘贴跑 rm -rf**，至少用 `--dry-run` 或在 docker/WSL 中先试。

## 相关页面

- 概念：[生物编程](生物编程.md) · [AI 协作边界](AI协作边界.md)
- 实体：[Python](../entities/Python.md) · [R](../entities/R.md) · [Bash](../entities/Bash.md)
- 来源：[AIDD Ch.1](../sources/AIDD_Bioinformatics_Course.md) · [36 课时讲稿](../sources/36课时讲稿.md)
