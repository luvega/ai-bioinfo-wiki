---
type: source
title: Starting Data Analytics with Generative AI and Python
authors: [Artur Guja, Marlena Siwiak, Marian Siwiak]
year: 2024
publisher: Manning
isbn: 9781633437210
raw_path:
  - materials/raw/pdf_originals/Starting Data Analytics with Generative AI and Python 9781633437210.pdf
  - materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210/book.mineru.md
  - materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210/book.course.md
ingested: 2026-05-21
language: en
kind: textbook
pages: 362
status: stable
tags: [generative-ai, data-analytics, python, prompt-engineering, eda]
---

# Starting Data Analytics with Generative AI and Python（Manning, 2024）

## 一句话定位

**“数据分析项目中如何系统地使用 LLM”** 的方法论书。
它最强的部分不是教 Python 或统计，而是给出
"问题陈述 → 目标 → 提示 → AI 输出 → 评估 → 实施"的循环图（Recommended GenAI Data Analysis Flow）。
直接对接本课程**第 2、3、5、6 周**对 AI 协作规范的要求。

## 核心循环（书前页插图）

> User Prompts ←→ Generative AI activities
> Problem statement → Goals of analysis → Guidance / suggestions →
> Implementation / code → Evaluation & decision-making → Iteratively
> Initial results → Analysis & augmentation → Interpretive results →
> Iteratively → Final synthesis and decision-making

这张图可以直接做成 PPT 一页，用于第 2 周"AI 协作规范"导入。

## 在本课程中的重点用法

- **第 1-2 周**：AI 边界与 AI 协作循环图。
- **第 3 周**：Python 入门时套用书中的 prompt 模板（解释代码、定位错误）。
- **第 5-6 周**：数据清洗 + 描述性统计阶段，书里给了大量"如何让 AI 帮你处理 messy data"的实战例。
- **第 17-18 周项目实战**：书中“flow”可以作为学生项目报告的结构模板。

## 与 [Learn AI-Assisted Python Programming](Learn_AI_Assisted_Python_Programming.md) 的差异

| 项 | 本书 | Learn AI-Assisted Python Programming |
|---|---|---|
| 主线 | 数据分析项目流程中的 AI 用法 | 编程教学中如何与 Copilot/ChatGPT 协作 |
| 工具 | ChatGPT 类对话 | GitHub Copilot 行内补全 + ChatGPT |
| 阶段 | 完整数据分析项目 | 函数级编程 |
| 在课程的位置 | 项目实战阶段 | 编程入门阶段 |

详见 [synthesis/三本Python书定位对比](../synthesis/三本Python书定位对比.md)。

## 待展开（按需 ingest 时）

- `concepts/AI协作循环.md`（书的核心图）
- `concepts/Prompt模板_数据分析.md`
- `queries/2026-xx-xx_用本书改写第N周AI协作规范.md`

## 相关页面

- 同类书：[Learn AI-Assisted Python Programming](Learn_AI_Assisted_Python_Programming.md)
- 概念：[AI 协作边界](../concepts/AI协作边界.md)
- 课程总线：[36 课时讲稿](36课时讲稿.md)

## 勘误 / 注意

- MinerU 转换结果以 `book.mineru.md` 为完整解析层，`book.course.md` 为备课整理层；旧版轻量转换已退役。
