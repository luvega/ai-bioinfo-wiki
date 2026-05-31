---
type: entity
name: Python
category: language
domain: [general, data-science, machine-learning, bioinformatics, app-dev]
status: stable
tags: [language, python, data-analysis, ai-assisted]
---

# Python

## 定位

通用编程语言，本课程的**第一语言**（第 3 周开始）。
用作：数据清洗、整形、可视化、机器学习、AI 协作示例、应用开发。

## 在本课程中的使用范围

| 周 | 用 Python 干什么 |
|---:|---|
| 3 | 入门（变量、列表、字典、条件、循环） |
| 5-6 | 数据读取、清洗、整形（pandas） |
| 7 | 描述统计、分布可视化（pandas / matplotlib / seaborn） |
| 8-10 | 假设检验、回归、分类（scipy / statsmodels / scikit-learn） |
| 13 | 机器学习入门（scikit-learn） |
| 17-18 | 项目实战 |

## 关键库（按上手顺序）

| 库 | 用途 | 引入周次 |
|---|---|---:|
| `pandas` | 数据框 | 5 |
| `numpy` | 数组 / 数学 | 5 |
| `matplotlib` | 基础绘图 | 7 |
| `seaborn` | 统计图风格 | 7 |
| `scipy.stats` | 假设检验 | 8 |
| `statsmodels` | 回归 / 时间序列 | 9 |
| `scikit-learn` | ML | 13 |
| `Biopython` | 生信（选讲） | — 见 [Biopython](Biopython.md) |
| `pytorch` | 深度学习（不展开） | — |

## 在 AIDD 中

- AIDD Ch.2 / Ch.3 用 Python + Biopython 实现序列处理与 Tkinter 应用；
- 与本课程的 Python 部分**没有重叠**——AIDD 偏序列与 GUI，本课程偏数据框与统计。

## 与 AI 协作

- AI 给的 Python 代码相对易读，但**注意版本差异**：
  - pandas 1.x ↔ 2.x（`pd.read_csv` 默认参数）
  - sklearn 0.x ↔ 1.x（API 命名空间）
- 推荐固定一个 venv，并把版本写入 `requirements.txt`。

## 课程中的安装建议

- 使用 [uv](https://github.com/astral-sh/uv) 或 `python -m venv` + `pip`。
- 不推荐 Anaconda（学生体积太大、网络问题多）。
- 教学服务器可考虑 JupyterHub 或 Codespaces。

## 相关页面

- 概念：[工具分工_Python_R_Bash](../concepts/工具分工_Python_R_Bash.md) · [AI 协作边界](../concepts/AI协作边界.md)
- 实体：[R](R.md) · [Bash](Bash.md) · [Biopython](Biopython.md)
- 来源：[ISLP](../sources/ISLP.md) · [Learn AI-Assisted Python Programming](../sources/Learn_AI_Assisted_Python_Programming.md) · [Starting Data Analytics with GenAI](../sources/Starting_Data_Analytics_GenAI.md)
