---
type: topic
title: 第 2 周 · 数据分析流程、复现规范与人机协作规范
week: 2
hours: 2
status: stable
tags: [reproducibility, pipeline, ai-boundary, project-structure, week-02]
---

# 第 2 周 · 数据分析流程、复现规范与人机协作规范（2 学时）

> 来源：[36 课时讲稿 §第 2 周](../sources/36课时讲稿.md)

## 大纲定位

- 主要教学内容：数据分析流程，文件组织、命名规范、结果留痕、Prompt 记录与复现基础。
- 育人元素：规范意识与科研责任。
- 重点难点：理解可复现、可追溯和 AI 协作透明度。
- 备注：AI 仅用于解释概念/报错。

## 教学目标

学完本周学生应该能够：
1. 解释什么是"可复现的数据分析"。
2. 描述推荐的项目目录结构，并说明每个子目录的作用。
3. 写出符合规范的文件名（日期 + 任务 + 版本 + 含义）。
4. 用本课程的"6 字段 AI 协作记录模板"写一份记录。

## 课堂组织（90 分钟）

| 时长 | 内容 |
|---:|---|
| 15' | 对比展示：不规范项目目录 vs 规范项目目录 |
| 15' | 讲 [项目目录结构与可复现](../concepts/项目目录结构与可复现.md)（6 个子目录） |
| 15' | 文件命名规则、版本意识 |
| 15' | 引入 [GitHub](../entities/GitHub.md) 与 git 基础（5 个命令） |
| 15' | 演示 6 字段 AI 协作记录模板 |
| 15' | 学生练习：把上周作业的目录整理为规范结构，做一次 commit |

## 可抽取的 AIDD 素材

- AIDD [Ch.6 Bioinformatics Pipeline](../sources/AIDD_Bioinformatics_Course.md)
  → "pipeline = 输入 + 工具 + 参数 + 输出 + 日志"思维框架。
- AIDD [Ch.12 §1, §3 GitHub Profile and Repository Setup](../sources/AIDD_Bioinformatics_Course.md)
  → 演示如何在 GitHub 上创建仓库 + 第一个 commit。
- AIDD [Ch.5 §2 WSL Setup](../sources/AIDD_Bioinformatics_Course.md)
  → 5 分钟演示 Windows 装 WSL（学生不要求装）。

## 引用的概念页

- [项目目录结构与可复现](../concepts/项目目录结构与可复现.md)
- [AI 协作边界](../concepts/AI协作边界.md)
- [医药数据特征](../concepts/医药数据特征.md)

## AI 协作提示词示例

```text
请解释下面这个报错可能是什么意思，并列出我应当逐步检查的项目。
不要直接改代码。
报错信息：FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
```

## 上机任务

1. 在个人项目根目录初始化 git（`git init`）。
2. 按 6 子目录结构创建空目录 + 占位 `.gitkeep`。
3. 写一份顶层 `README.md`，说明项目名、目标、数据来源、AI 使用约定。
4. 提交一次 commit，commit message 格式：`init: 项目初始化`。
5. （可选）推送到 GitHub Private Repo。
6. 写一份 AI 协作记录（即使本周只让 AI 解释了一个报错），存到 `ai_logs/2026-xx-xx_<topic>.md`。

## 评估要点

- 目录结构是否完整且无错放。
- 文件命名是否符合规范。
- git 是否有 commit（不强求 push）。
- AI 协作记录是否包含全部 6 字段。

## 风险与坑

- **学生第一次用 git 容易在 commit 里塞大文件或敏感数据**：演示时强调 `.gitignore`，
  尤其要忽略 `data_raw/`（数据不入 git）和 `ai_logs/*` 中含个人信息的部分。
- **学生可能直接拷贝示范目录而不理解每个子目录的作用**：用提问的方式让他们解释每个目录。

## 相关页面

- 概念：[项目目录结构与可复现](../concepts/项目目录结构与可复现.md) · [AI 协作边界](../concepts/AI协作边界.md)
- 实体：[GitHub](../entities/GitHub.md) · [Bash](../entities/Bash.md)
- 来源：[36 课时讲稿](../sources/36课时讲稿.md) · [AIDD Ch.5, Ch.6, Ch.12](../sources/AIDD_Bioinformatics_Course.md)
- 上一周：[第 1 周 · 课程导论](week_01_课程导论.md)
- 下一周：第 3 周 · AI 辅助编程与 Python 快速入门（待建）
