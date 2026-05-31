# 2026-05-25 项目根目录迁移计划

## 目标

将当前 `AI_Course` 项目从 `F:\AI_Course` 迁移到 `E:\Codex_Projects\AI_Course`，并把后续工作基准切换到新路径。

## 范围

- 复制完整项目目录，包括 `.git/`、课程文件、知识层、素材层、项目本地 `skills/`、脚本和站点文件。
- 更新当前说明文件中的有效项目根目录：`AGENTS.md`、`README.md`、`memory.md`、`knowledge/assets/obsidian_setup.md`。
- 保留历史 spec/plan 中对旧路径的记录，不回写历史上下文。

## 执行步骤

1. 确认 `E:\Codex_Projects` 可用且目标 `AI_Course` 不会覆盖已有项目。
2. 先在源目录更新迁移计划和当前路径说明。
3. 使用 `robocopy` 将完整目录复制到 `E:\Codex_Projects\AI_Course`。
4. 在目标目录校验关键文件、Git 状态和旧路径残留。
5. 暂不删除 `F:\AI_Course`，将其作为短期回退点。

## 校验清单

- `AGENTS.md`、`memory.md`、`knowledge/index.md` 可读。
- `course/syllabus/36课时-AI前置调整版.docx` 与主讲稿 Markdown 存在。
- `.git/` 已复制，`git status --short --branch` 可运行。
- 当前说明文件不再把 `F:\AI_Course` 作为有效项目根目录。
