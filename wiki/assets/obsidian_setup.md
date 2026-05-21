---
type: asset
title: Obsidian Vault 配置说明
status: stable
tags: [obsidian, setup, workspace]
---

# Obsidian Vault 配置说明

## Vault 根目录

**整个 `e:\AI_Course\` 是 vault 根**。这样既能浏览 `wiki/`，也能跳回 `doc/` 与 `raw/` 看原文。

> 不要把 vault 设成 `e:\AI_Course\wiki\`——这会让 wiki 里指向 `../sources/` `../doc/` 的链接全失效。

## 首次打开步骤

1. Obsidian → **Open another vault** → **Open folder as vault** → 选 `e:\AI_Course\`。
2. 因为已有 `.obsidian/`，Obsidian 会**直接使用现有配置**，不会重置。
3. 首次启动会扫描索引，约 10-30 秒（看机器）。
4. 打开 [wiki/overview.md](../overview.md) 作为入口。

## 已预配的设置（开箱即用）

### Editor & Files
- 默认视图：preview
- Live Preview：开
- 链接格式：相对路径（`useMarkdownLinks: true`, `newLinkFormat: relative`）
- 附件目录：`wiki/assets/`
- Tab 大小：2 空格
- 删除：进入系统回收站

### 索引排除（`userIgnoreFilters`）
- `pdf_originals/` — 大 PDF
- `sources/PDF_Library/` — PDF 转的大 markdown（最大 1.4 MB）
- `sources/AIDD_Bioinformatics/` — AIDD txt 镜像
- `raw/AIDD_Bioinformatics/` — AIDD 字幕 txt（主目录）
- `.git/`、`__pycache__/`

> 排除后 Obsidian 仍能用相对路径**链接**到这些文件（如 `sources/PDF_Library` 下的 markdown），
> 但不会出现在 Quick Switcher、Search、Graph View 中——保持工作面板干净。
>
> 如果想临时找 AIDD 原文，可去掉 `userIgnoreFilters` 中对应条目，或者用文件系统打开。

### Core Plugins 已启用
- File Explorer、Search、Quick Switcher、Graph View、Backlinks、Outline、Outgoing Links、Tag Pane、Properties、Page Preview、Bookmarks、Templates、Word Count

### Graph View 颜色分组（已配）

| 文件夹 | 颜色 | 用途 |
|---|---|---|
| `wiki/sources/` | 蓝 | 原始素材摘要 |
| `wiki/entities/` | 橙 | 实体（库/工具） |
| `wiki/concepts/` | 绿 | 抽象概念 |
| `wiki/topics/` | 金 | 教学单元 |
| `wiki/synthesis/` | 紫 | 综合页 |

打开 Graph View（左侧第三个图标）即可看到分色图。

## 推荐手动安装的社区插件

> Obsidian Settings → Community plugins → Turn on community plugins → Browse → 搜索安装。
> 装完后会自动写入 `.obsidian/community-plugins.json` 和 `.obsidian/plugins/`。

### 强烈推荐（教学场景刚需）

| 插件 | 解决什么问题 |
|---|---|
| **Dataview** | 查询 YAML front matter，自动生成"全部 status:in_progress 的页"等表格 |
| **Templater** | 新建 source / entity / concept 页时一键套模板 |
| **Excalidraw** | 画流程图、概念图，与 markdown 并存 |
| **Tag Wrangler** | 批量改 tag（早期 tag 命名不统一时） |

### 可选

| 插件 | 解决什么问题 |
|---|---|
| **Iconize** | 给文件夹加 emoji 图标（让 sources/entities 等更直观） |
| **Linter** | 自动整理 front matter / 标题 / 空行 |
| **Advanced Tables** | 表格编辑（DESeq2 / ggplot2 页有不少表） |
| **Mind Map** | 把任何 markdown 渲染为脑图 |
| **Marp slides** | 用 markdown 直接做 PPT，**强烈适合本课程**（每周一份 marp 讲稿） |
| **Pandoc Plugin** | 导出为 docx / pdf，给学生发讲义 |

### 不推荐 / 注意

- **Spaced Repetition、Anki Sync 等学习卡片**：不要用——本 wiki 不是闪卡库。
- **Sync（官方付费）**：项目已用 git，没必要再付费同步。
- **任何 AI 插件**：与本项目"AI 写 wiki"的工作流冲突，AI 维护通过 Cursor/Claude/Codex 进行，
  Obsidian 只用于**人浏览**。

## 已添加到 .gitignore 的 Obsidian 状态文件

下面这些是**本机状态**，不入 git（避免不同电脑互覆盖）：
- `.obsidian/workspace.json`
- `.obsidian/workspace-mobile.json`
- `.obsidian/cache`

入 git 的（团队级配置，跨机器共享）：
- `.obsidian/app.json`
- `.obsidian/appearance.json`
- `.obsidian/core-plugins.json`
- `.obsidian/community-plugins.json`
- `.obsidian/graph.json`
- `.obsidian/hotkeys.json`

## 常见问题

### Q: 我装了社区插件后，git 想不想 commit 整个 `.obsidian/plugins/`？

不建议。插件代码很大，且不同人偏好不同。已建议在 `.gitignore` 加 `.obsidian/plugins/`（如果你想加的话）。
**只 commit 已启用插件的 id 列表**（即 `community-plugins.json`）就够了——
克隆仓库后，让 Obsidian 自动重新下载这些插件。

如果你要这么做，把这行加到 `.gitignore`：

```
.obsidian/plugins/
```

### Q: Graph View 太乱怎么办？

打开右上角 Filters → 勾上 "Existing files only" 与 "Orphans" 复选框（按需），
并调小 "Line thickness"。本 vault 颜色分组已配好，蓝/橙/绿/金/紫五色对应 5 类页。

### Q: 想全文搜索 raw/AIDD_Bioinformatics 字幕怎么办？

临时去掉 `.obsidian/app.json` 中 `userIgnoreFilters` 的对应行；或者直接在 VS Code / 命令行用 `rg` 搜——
搜字幕这种"零散查询"用 ripgrep 比 Obsidian 全文索引快很多。

## 相关页面

- [overview](../overview.md)
- [index](../index.md)
- [README（项目根）](../../README.md)
