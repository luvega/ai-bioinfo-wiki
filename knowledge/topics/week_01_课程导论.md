---
type: topic
title: 第 1 周 · 课程导论与医药数据特征
week: 1
hours: 2
status: stable
tags: [intro, course-design, ai-boundary, week-01]
---

# 第 1 周 · 课程导论与医药数据特征（2 学时）

> 来源：[36 课时讲稿 §第 1 周](../sources/36课时讲稿.md)

## 大纲定位

- 主要教学内容：医药数据类型、多源性、高维性、异质性；课程目标、项目任务、AI 使用边界。
- 育人元素：科学问题导向与责任。
- 重点难点：建立课程整体框架，理解数据驱动与人机协作边界。
- 备注：**本周完全不上手代码**，只讲思想框架。

## 教学目标

学完本周学生应该能够：
1. 用 2-3 句话回答"医药数据有什么特点"。
2. 用 1 句话说清楚"AI 在我们这门课里能做什么、不能做什么"。
3. 列出 3 种不同形态的医药数据，并指出它们各自需要什么类型的分析。

## 课堂组织（90 分钟）

| 时长 | 内容 |
|---:|---|
| 10' | 展示典型医药数据：临床指标表、表达矩阵、药物反应表、单细胞 metadata |
| 20' | 讲 [工具分工_Python_R_Bash](../concepts/工具分工_Python_R_Bash.md)（引用 AIDD Ch.1） |
| 20' | 讨论 [AI 协作边界](../concepts/AI协作边界.md)：能做 / 不能做 / 三条红线 |
| 30' | 学生写下一个**自己感兴趣的医药数据问题**，并说明可能需要哪些数据 |
| 10' | 布置作业 + 答疑 |

## 可抽取的 AIDD 素材

- AIDD [Ch.1 §1 Introduction To Biological Programming](../sources/AIDD_Bioinformatics_Course.md)
  → 引入"用编程解决生命科学问题"的视角。
- AIDD [Ch.1 §2 Powerhouse Trio of Bioinformatics](../sources/AIDD_Bioinformatics_Course.md)
  → 直接做成一页 PPT 讲 Python/R/Bash 分工。

## 引用的概念页

- [医药数据特征](../concepts/医药数据特征.md)
- [工具分工_Python_R_Bash](../concepts/工具分工_Python_R_Bash.md)
- [AI 协作边界](../concepts/AI协作边界.md)
- [生物编程](../concepts/生物编程.md)

## AI 协作提示词示例（本周课堂上演示）

```text
我正在学习医药数据处理与可视化。请帮我把"某药物治疗前后某指标是否下降"
这个问题拆成：研究问题、数据字段、可能的统计方法、可视化方式和需要注意的伦理问题。
请不要直接给结论，而是列出我需要自己核验的地方。
```

## 上机任务

**本周不做上机**。课后作业：

1. 写一份不超过一页的小报告，回答："如果让我用一份数据回答一个药学问题，
   这份数据应该长什么样？我打算用什么工具？AI 在哪些环节能帮我，哪些环节不能？"
2. 创建本课程的个人项目根目录（按 [项目目录结构与可复现](../concepts/项目目录结构与可复现.md) 推荐结构），
   提交目录截图。

## 评估要点

- 学生是否能用自己的语言复述"医药数据 4 特征"。
- 学生是否能区分"AI 解释" vs "AI 替我做"。
- 提交的目录是否包含 `data_raw / data_processed / scripts / results / docs / ai_logs`。

## 风险与坑

- **学生易把课程理解成"AI 工具课"**：要反复强调"AI 是辅助手段，统计判断与医学解释才是核心"。
- **学生易回到"我来学一遍 Python/R 语法"的思维**：本周要扭转这个预设，
  让他们意识到课程目标是"问题导向 + AI 协作 + 可复现"，语法只是路径。

## 相关页面

- 概念：[医药数据特征](../concepts/医药数据特征.md) · [AI 协作边界](../concepts/AI协作边界.md) · [工具分工_Python_R_Bash](../concepts/工具分工_Python_R_Bash.md)
- 来源：[36 课时讲稿](../sources/36课时讲稿.md) · [AIDD Ch.1](../sources/AIDD_Bioinformatics_Course.md)
- 下一周：[第 2 周 · 数据分析流程与复现规范](week_02_数据分析流程与复现规范.md)
