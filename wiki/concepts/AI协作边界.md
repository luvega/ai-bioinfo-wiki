---
type: concept
title: AI 协作边界与协作规范
status: stable
tags: [ai-assisted, prompt-engineering, course-design, ethics]
---

# AI 协作边界与协作规范

## 一句话原则

**AI 帮助你思考，但不能替你思考。**

## 三阶段边界（来自 36 课时讲稿）

| 阶段 | 周次 | AI 能做 | AI 不能做 |
|---|---|---|---|
| ① 基础与边界 | 1-2 | 解释概念、解释报错 | 写完整代码、给统计结论 |
| ② 工具与流程 | 3-11 | 解释代码、生成局部代码、改写函数 | 替学生选择统计方法、判断变量类型 |
| ③ 组学与项目 | 12-18 | 流程梳理、代码重构、报告修改、结果复核 | 替学生判断医学意义、决定是否发布结果 |

## 协作记录模板（必修）

每次重要 AI 使用都要留下 6 个字段：

```
1. 问题（自然语言，1-2 句）
2. Prompt（实际输入给 AI 的完整提示词）
3. AI 输出（关键部分，不必全文）
4. 人工核验（运行结果 / 公式 / 文献 / 数据集对照）
5. 修改说明（最终用了什么，做了哪些改动）
6. 反思（这次 AI 是否帮上忙？哪里需要谨慎？）
```

这个模板存入项目目录 `ai_logs/` 子文件夹（见 [项目目录结构与可复现](项目目录结构与可复现.md)）。

## 通用提示词骨架

```text
[场景] 我正在学习 …
[输入] 我有 数据 / 代码 / 报错：…
[请求] 请帮我 [解释 | 列检查清单 | 局部改写 | 找潜在问题]
[约束] 不要直接给完整代码 / 不要替我做判断
[输出] 列出我需要自己核验的地方
```

## 三本相关书的位置

- [Learn AI-Assisted Python Programming](../sources/Learn_AI_Assisted_Python_Programming.md)：
  函数级 + Copilot 行内补全的协作循环。
- [Starting Data Analytics with GenAI](../sources/Starting_Data_Analytics_GenAI.md)：
  项目级 + ChatGPT 对话的协作循环。
- 36 课时讲稿：综合两者，并加入"医药数据"的强解释性约束。

## 三个红线

1. **不要把 AI 输出当作"权威结论"**——尤其是医学结论、用药建议、统计显著性。
2. **不要直接复制运行未读懂的代码**——尤其是 `rm`、`drop_duplicates`、`fillna(0)` 这类。
3. **不要把患者级数据/真实临床数据贴给 AI**——伦理与法规问题，本课程明确禁止。

## 容易踩的坑

- AI 会**自信地编造**——函数名、库名、参数名、文献引用都可能是幻觉。
- AI 对**版本敏感**——R/Python 不同版本的 API 不同，AI 给的代码可能用了旧 API。
- AI **不会判断数据的合理性**——它看到 `glucose = -3.2` 不会觉得奇怪，但你应该觉得奇怪。

## 相关页面

- 概念：[医药数据特征](医药数据特征.md) · [项目目录结构与可复现](项目目录结构与可复现.md)
- 实体：[GitHub Copilot](../entities/GitHub_Copilot.md) · [ChatGPT](../entities/ChatGPT.md)
- 来源：[36 课时讲稿](../sources/36课时讲稿.md) · [Learn AI-Assisted Python Programming](../sources/Learn_AI_Assisted_Python_Programming.md) · [Starting Data Analytics with GenAI](../sources/Starting_Data_Analytics_GenAI.md)
