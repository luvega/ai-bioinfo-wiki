---
type: entity
name: GitHub Copilot
category: ai-tool
domain: [ai-assisted-programming, ide-extension]
status: stable
tags: [ai, copilot, code-completion, vscode]
---

# GitHub Copilot

## 定位

IDE 内的 **AI 行内补全** 工具（VS Code / JetBrains / Neovim 等）。
本课程**第 3 周**作为"AI 辅助编程"的核心案例介绍。

## 与 [ChatGPT](ChatGPT.md) 的差异

| 项 | Copilot | ChatGPT |
|---|---|---|
| 形态 | IDE 内行内补全 + Chat 面板 | 浏览器/桌面对话 |
| 上下文 | 当前文件 + 项目摘要 | 用户主动粘贴 |
| 协作粒度 | 函数级 / 行级 | 项目级 / 多轮 |
| 适合阶段 | 写代码时 | 设计、调试、阅读 |
| 课程对应 | 第 3-13 周编程 | 第 5-18 周分析 |

## 教育用法（来自 [Learn AI-Assisted Python Programming](../sources/Learn_AI_Assisted_Python_Programming.md)）

书中的 **function design cycle**：

```
1. 用注释/docstring 写出函数意图（自然语言）
2. 让 Copilot 生成函数体
3. 读懂代码（不读懂就不接收）
4. 写测试，验证
5. 失败 → 改注释或改代码 → 回到 2
```

**红线**：永远不接收没读懂的代码。

## 学生使用建议

- 学校账号 / GitHub Education Pack 可免费使用 Pro。
- 第 1-2 周**不要开**，强制学生学会读基本 Python/R 代码。
- 第 3 周起逐步引入，**配合协作记录（[AI 协作边界](../concepts/AI协作边界.md)）**。
- 教师可考虑在课堂演示开关 Copilot 的差异。

## 风险

- **代码版权 / 训练数据来源**问题：避免商用项目无审查接收输出。
- **隐私**：不要在含敏感数据的文件中开 Copilot，可能上传上下文。
- **过度依赖**：CS Education 研究显示，初学者过早依赖会损害基础能力——这正是本课程"AI 前置但仍设阶段边界"的理论基础。

## 相关页面

- 概念：[AI 协作边界](../concepts/AI协作边界.md)
- 实体：[ChatGPT](ChatGPT.md) · [GitHub](GitHub.md)
- 来源：[Learn AI-Assisted Python Programming](../sources/Learn_AI_Assisted_Python_Programming.md)
