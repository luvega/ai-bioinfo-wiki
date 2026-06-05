---
type: skill-install-report
title: skills.zip 项目本地安装核对报告
status: verified
date: 2026-06-05
---

# skills.zip 项目本地安装核对报告

本报告记录 `E:\Codex_Projects\AI_Course\skills.zip` 与项目本地 `skills/` 的核对结果。安装边界沿用项目规则：只安装到本项目，不写入全局 `$CODEX_HOME/skills`，不覆盖 `course-*` workflow skills。

## 核对结果

| 项目 | 结果 |
|---|---:|
| zip 中普通文件数 | 402 |
| zip 中 skill 目录数 | 27 |
| 项目本地 skill 目录数 | 32 |
| 需补装的非缓存文件 | 1 |
| 已忽略的缓存文件 | 3 |
| 内容 hash 不一致文件 | 0 |

## 本轮补装

- 已从 `skills.zip` 补装：`skills/md-to-docx/快速使用指南.md`

## 明确忽略

以下缺失项是 Python 编译缓存，不安装、不入库：

- `skills/ui-ux-pro-max/scripts/__pycache__/core.cpython-311.pyc`
- `skills/ui-ux-pro-max/scripts/__pycache__/design_system.cpython-311.pyc`
- `skills/md-to-docx/__pycache__/convert_md_to_docx.cpython-311.pyc`

## 边界说明

- `skills.zip` 不包含项目本地 `course-skill-router`、`course-lecture-expand`、`course-ppt-storyboard`、`course-evidence-review`、`course-update-vault`。
- 这 5 个 `course-*` workflow skills 继续作为 AI_Course 的课程主线 wrapper，不被 zip 安装流程覆盖。
- 后续若再次更新 `skills.zip`，先运行 `python scripts/maintenance/course_skill_inventory.py --check`，确认没有缺失的非缓存 zip 文件，再决定是否补装。
