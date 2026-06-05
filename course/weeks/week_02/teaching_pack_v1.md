---
type: trial-teaching-pack
week: 2
title: 数据分析流程、复现规范与人机协作规范 · 试讲包 v1
status: trial_ready_pack_v1
updated: 2026-06-04
audience: 药学本科生
duration: 2 学时
---

# Week 02 试讲包 v1

## 2 学时时间切分

| 时间 | 活动 | 教师动作 | 学生可提交产物 |
|---:|---|---|---|
| 0-10 min | 复盘 Week 01 | 把课程契约草表转成项目目录需求 | 项目目标一句话 |
| 10-30 min | 目录规范 | 解释 `data/`, `scripts/`, `outputs/`, `ai_logs/` | 目录树 |
| 30-55 min | Git/Shell 最小任务 | 演示 `git status`、`git add`、`git commit` 的记录意义 | 命令记录 |
| 55-75 min | AI 使用记录 | 填写 Prompt、用途、人工修改、不采纳理由 | AI 记录表 |
| 75-90 min | 复现审计 | 同伴检查是否能追溯数据、脚本、图表和 AI 输出 | 复现检查清单 |

## 课堂任务单

创建以下目录和文件草稿：

```text
week02_project/
  README.md
  data_sources.md
  scripts/
  outputs/
  ai_logs/prompt_log.md
```

README 最少包含：研究问题、数据来源、运行顺序、输出文件、AI 使用记录位置。

## 预期输出与参考答案

- 预期输出：目录树、README 5 行草稿、1 条 Prompt 记录、1 条 Git/Shell 命令记录。
- 参考答案要点：`outputs/` 是导出物，不作为事实来源；`ai_logs/` 记录 AI 协作但不替代人工核验；Git 记录应说明“为什么改”。
- 评分点：目录完整 25%，README 可读 25%，AI 记录透明 25%，复现边界 25%。

## 常见误区

- 只交最终图，不交数据来源和处理说明。
- 把 AI 对话截图当成核验证据。
- Git 提交信息只写 “update” 而不说明修改目的。

## AI 审计提示

```text
请检查我的项目目录和 README 是否能让同学复现分析。
只指出缺失项和风险，不要替我补写分析结论。
```
