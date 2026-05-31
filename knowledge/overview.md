---
type: overview
title: AI_Course 知识库主页
status: stable
updated: 2026-05-21
tags: [overview, map]
---

# AI_Course 知识库主页

本知识库服务于一门具体的课程：**“医药数据处理与可视化（36 课时·AI 前置版）”**。
它不是一个生信百科，也不是一份课程讲义的备份——
它是“**为这门课准备教学/研究的、活的、可生长的笔记网络**”。

> 不知道该看什么的时候，从这里开始。

---

## 1. 课程一句话

面向药学专业本科生，36 学时，**把 AI 辅助编程前置**，让学生在医药数据分析的全链条
（数据→清洗→统计→可视化→解释）里学会使用 AI 同时保持判断力。

> 详细大纲：[课程主页_36课时](topics/课程主页_36课时.md)
>
> 来源文档：[36 课时讲稿](sources/36课时讲稿.md) · [36 课时 docx 大纲](sources/36课时大纲docx.md)

---

## 2. 现有材料地图

```
课程主大纲（course/syllabus/课程教学讲稿*.md）   ←—— 36 周教学骨架
        │
        ├── AIDD Bioinformatics（raw/sources）—— 11 章 71 节字幕，生信入门
        │       ├── Python / Biopython
        │       ├── Linux / Bash / NGS pipeline
        │       ├── R / DESeq2 / scRNA-seq / Microarray
        │       └── GitHub
        │
        └── PDF 书库（materials/raw/pdf_originals / materials/markdown/pdf_library_legacy）
                ├── ISLP《An Introduction to Statistical Learning, Python》
                ├── ISLR《An Introduction to Statistical Learning, R》
                ├── Starting Data Analytics with Generative AI and Python
                └── Learn AI-Assisted Python Programming（Copilot + ChatGPT）
```

四个素材池分别覆盖：

| 素材 | 覆盖能力 | 在课程中的位置 |
|---|---|---|
| 36 课时讲稿 | 大纲、讲法、上机任务、AI 提示词 | 全部 18 周 |
| AIDD 课程 | 生信入门（Python/R/Bash/NGS/RNA-seq/scRNA-seq/Microarray/GitHub） | 第 3-4、9、11、14-18 周 |
| ISLP / ISLR | 统计学习与机器学习理论与代码 | 第 6-13 周（统计与建模） |
| GenAI + Copilot 书 | AI 辅助编程模式、Prompt 习惯 | 第 1-3、17、18 周（AI 前置 + 项目复盘） |

---

## 3. 怎么在这个 wiki 里找东西

按"我现在想干嘛"分几条路径：

### 🗓️ 我要备某一周的课

→ [课程主页_36课时](topics/课程主页_36课时.md) → 选周次 → 顺着页里的 source 链接回到原始素材。

### 🧪 我要查某个工具/库怎么用

→ [entities/](entities/)。例如 [DESeq2](entities/DESeq2.md)、[Biopython](entities/Biopython.md)、
[samtools](entities/samtools.md)、[ggplot2](entities/ggplot2.md)。

### 📚 我要理解某个生信概念/流程

→ [concepts/](concepts/)。例如 [RNA-seq 上游流程](concepts/RNA-seq上游流程.md)、
[Variant Calling 流程](concepts/Variant_Calling流程.md)、[差异表达分析](concepts/差异表达分析.md)。

### 🤖 我在思考 AI 用法

→ [AI 协作边界](concepts/AI协作边界.md) · [Learn AI-Assisted Python Programming](sources/Learn_AI_Assisted_Python_Programming.md)
· [Starting Data Analytics with GenAI](sources/Starting_Data_Analytics_GenAI.md)

### 🔭 我想看全局对比/思考

→ [synthesis/](synthesis/)。其中：
- [AIDD 与 36 课时映射](synthesis/AIDD与36课时映射.md)
- [三本 Python 书定位对比](synthesis/三本Python书定位对比.md)
- [知识缺口与后续素材](synthesis/知识缺口与后续素材.md)

### 📜 我想看完整目录

→ [knowledge/index.md](index.md)（全表）

### ⏱️ 我想看 knowledge 最近发生了什么

→ [knowledge/log.md](log.md)（时间线）

---

## 4. 给未来 AI agent 的提醒

- 阅读 `AGENTS.md` 后再开始工作，它定义了**所有规则**。
- 不要重复造页：写 entity / concept 前先 grep。
- 每次 ingest **必须**更新 `index.md` 与 `log.md`。
- 当用户问问题时，先扫 `index.md` 找候选页，不要直接去 raw 层翻全文。
- Raw 层只读：不要改写 `materials/raw/pdf_originals/`、`materials/raw/aidd_bioinformatics/`、`materials/raw/external_ppt/` 或 `course/syllabus/`。

---

## 5. 当前状态

- 初始化日期：2026-05-21
- 已 ingest 素材：36 课时讲稿/大纲、AIDD（11 章 71 节）、4 本 PDF（轻量摘要）
- 已建页面（当前）：knowledge 40 页；course/weeks 已有 18 周骨架。
- 下一步建议：
  1. 从 `course/weeks/week_01` 开始逐周细化 PPT 大纲与授课脚本。
  2. 将 AIDD 71 节按主题继续展开到 concept 页（特别是 microarray、scRNA-seq、proteomics）。
  3. 对嵩天 Python PPT 完成结构化抽取，补入第 3-6 周素材。
