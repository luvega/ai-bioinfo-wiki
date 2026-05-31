---
type: entity
name: GitHub
category: platform
domain: [version-control, collaboration, code-hosting]
status: stable
tags: [git, github, version-control, collaboration]
---

# GitHub

## 定位

代码托管 + 版本控制 + 协作平台。本课程**第 2、17、18 周**用到：
- 第 2 周：版本控制基础、`git init`/`commit`/`push`、项目结构
- 第 17-18 周：项目实战的代码提交与协作

## 在 AIDD 中

AIDD [Ch.12 GitHub Guide for Students](../sources/AIDD_Bioinformatics_Course.md) 共 6 节，
覆盖：Profile 设置、仓库创建、搜索生信项目、Fork/Clone、协作 PR、项目管理。

## 本课程要求学生掌握的最小集

| 操作 | 命令 |
|---|---|
| 初始化仓库 | `git init` / GitHub 网页 New Repo |
| 克隆 | `git clone <url>` |
| 添加变更 | `git add .` |
| 提交 | `git commit -m "..."` |
| 推送 | `git push` |
| 拉取 | `git pull` |
| 查看状态 | `git status` / `git log --oneline` |
| 分支 | `git branch <name>` / `git checkout <name>` |
| PR | GitHub 网页 |

## 与本课程"可复现"原则的关系

- 项目目录用 git 跟踪，所有 commit 都是一次"分析快照"。
- 教学项目鼓励学生**用 commit message 记录 AI 协作**：例如 `commit: 修复 NA 处理（AI 建议 + 人工验证）`。
- 与 [项目目录结构与可复现](../concepts/项目目录结构与可复现.md) 紧密结合。

## GitHub Copilot

GitHub 还提供 [GitHub Copilot](GitHub_Copilot.md)，
属于 AI 辅助编程工具。**本课程在第 3 周引入**，但与 GitHub 平台是两件事，注意区分。

## 隐私与伦理

- 公开仓库 = 公开数据 + 公开代码。
- **绝不要把真实临床数据 / 未脱敏患者信息 / 含密钥的 config 文件**推到公开仓库。
- 学生作业仓库可以设为 Private，但教学评估时需要授权教师访问。

## 相关页面

- 概念：[项目目录结构与可复现](../concepts/项目目录结构与可复现.md) · [AI 协作边界](../concepts/AI协作边界.md)
- 实体：[GitHub Copilot](GitHub_Copilot.md)
- 来源：[AIDD Ch.12](../sources/AIDD_Bioinformatics_Course.md)
