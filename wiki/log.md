# Wiki 变更日志

> Append-only 时间线，所有 ingest / query 落档 / lint / refactor 都要在此留痕。
> 条目格式：`## [YYYY-MM-DD] <op> | <对象>`，便于 `grep "^## \[" log.md` 检索。

## [2026-05-21] bootstrap | 知识库初始化

- 新增：`AGENTS.md`（schema/工作流）、`README.md`（顶层说明）
- 新增：`wiki/` 骨架（`sources/`、`entities/`、`concepts/`、`topics/`、`synthesis/`、`queries/`、`assets/`）
- 新增：`wiki/overview.md`、`wiki/index.md`、`wiki/log.md`
- 备注：Raw 层保留原状（`pdf_originals/`、`doc/`、`raw/`、`sources/`），脚本目录不动。

## [2026-05-21] ingest | 36 课时教学讲稿（doc/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md）

- 新增：`wiki/sources/36课时讲稿.md`、`wiki/sources/36课时大纲docx.md`
- 新增：`wiki/topics/课程主页_36课时.md`、`wiki/topics/week_01_课程导论.md`、`wiki/topics/week_02_数据分析流程与复现规范.md`
- 新增：`wiki/concepts/医药数据特征.md`、`wiki/concepts/AI协作边界.md`、`wiki/concepts/项目目录结构与可复现.md`
- 新增：`wiki/concepts/工具分工_Python_R_Bash.md`
- 更新：`wiki/overview.md`、`wiki/index.md`

## [2026-05-21] ingest | AIDD Bioinformatics 课程（raw/AIDD_Bioinformatics + sources/AIDD_Bioinformatics）

- 新增：`wiki/sources/AIDD_Bioinformatics_Course.md`、`wiki/sources/AIDD课程结构整理.md`
- 新增：`wiki/concepts/生物编程.md`、`wiki/concepts/RNA-seq上游流程.md`、`wiki/concepts/Variant_Calling流程.md`、`wiki/concepts/差异表达分析.md`
- 新增：`wiki/entities/Python.md`、`wiki/entities/R.md`、`wiki/entities/Bash.md`、`wiki/entities/Biopython.md`、`wiki/entities/DESeq2.md`、`wiki/entities/ggplot2.md`、`wiki/entities/samtools.md`、`wiki/entities/BLAST.md`、`wiki/entities/GitHub.md`
- 备注：原始字幕为中文机翻，已通过 `scripts/clean_aidd_subtitles.py` 校正主要术语（详见 `raw/AIDD_Bioinformatics/TERMS.md`）。

## [2026-05-21] ingest | PDF 书库（sources/PDF_Library/*.md）

- 新增：`wiki/sources/ISLP.md`、`wiki/sources/ISLR.md`、`wiki/sources/Starting_Data_Analytics_GenAI.md`、`wiki/sources/Learn_AI_Assisted_Python_Programming.md`
- 新增：`wiki/entities/ChatGPT.md`、`wiki/entities/GitHub_Copilot.md`
- 备注：4 本 PDF 已由 `scripts/pdf_to_markdown.py` 转为 markdown，但仅做轻量摘要，未逐章展开。

## [2026-05-21] synthesis | 首批合成页

- 新增：`wiki/synthesis/AIDD与36课时映射.md`、`wiki/synthesis/三本Python书定位对比.md`、`wiki/synthesis/知识缺口与后续素材.md`
- 更新：`wiki/index.md`

## [2026-05-21] schema | 引入 memory.md

- 新增：`memory.md`（跨会话记忆：偏好 / 决策 / 阻塞 / 共识词汇 / 元反馈 / 反向规则）
- 更新：`AGENTS.md` —— 新会话开机三件事、4 个文件角色边界表、§3.5 Memorize 操作
- 更新：`README.md` —— 顶层目录与"4 个核心操作"前置三件事
- 触发：用户提议"是不是还应该有一个 memory.md 文件"。
- 备注：本文件记录"事实时间线"；偏好/决策/状态卡演化记录已迁移到 `memory.md`，两者各司其职。

## [2026-05-21] ingest | 富集分析 GO/KEGG/GSEA

- 新增：`wiki/concepts/富集分析_GO_KEGG.md`（ORA / GSEA / clusterProfiler + 45 分钟教学路径 + 5 个常见坑）
- 更新：`wiki/concepts/差异表达分析.md`（Week 11 位置补充富集链接）
- 更新：`wiki/topics/课程主页_36课时.md`（Week 11 行）
- 更新：`wiki/synthesis/AIDD与36课时映射.md`（标注 AIDD 未涉及此节）
- 更新：`wiki/synthesis/知识缺口与后续素材.md`（划掉条目）
- 更新：`wiki/index.md`（concept 计数 8→9）
- 触发：用户决定 Week 11 必须含富集分析（memory.md D-009）。

## [2026-05-21] infra | git 初始化

- 新增：`.gitignore`（排除 pdf_originals/、ai_logs/、projects/、.obsidian/workspace.json、Python/R 缓存等）
- 执行：`git init -b main` + 首次 commit（196 files, 41,064 insertions）
- commit 哈希：`8c971bf`
- 触发：用户同意加 git（memory.md D-007）。

## [2026-05-21] infra | Obsidian Vault 配置

- 新增：`.obsidian/`（app/appearance/core-plugins/community-plugins/graph/hotkeys）
- 新增：`wiki/assets/obsidian_setup.md`（vault 边界、推荐插件、Graph 分色说明）
- 更新：`wiki/index.md`（assets 区新增条目）
- 更新：`README.md`（Obsidian 入口指引）
- 配置要点：vault 根 = `e:\AI_Course\`；userIgnoreFilters 排除 raw 层重量级目录；Graph View 5 色分组。
- 触发：用户同意配 .obsidian（memory.md D-008）。

## [2026-05-21] infra | 推送 GitHub + 改为 Private

- 远端：`https://github.com/luvega/ai-bioinfo-wiki`（**Private**）
- 推送：commit `8c971bf` + `e512bc5` 已 push 到 origin/main
- 配置：本地仓库 `--local` 配 `http.proxy=http://127.0.0.1:10080`（仅本仓库，不污染全局；用户的 Clash/v2rayN 监听端口）
- 重要事件：push 完成后用户立即说"先不要 push 了"——push 已成功，
  随后用户决定保留远端但改为 Private，AI 用 `gh repo edit --visibility private` 完成切换。
- 教训记入 `memory.md` D-010 与 §5、§6（**后续推送/远端可见性/删除动作必须二次确认**）。
