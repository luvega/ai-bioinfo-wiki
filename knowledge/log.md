# Wiki 变更日志

> Append-only 时间线，所有 ingest / query 落档 / lint / refactor 都要在此留痕。
> 条目格式：`## [YYYY-MM-DD] <op> | <对象>`，便于 `grep "^## \[" log.md` 检索。

## [2026-05-21] bootstrap | 知识库初始化

- 新增：`AGENTS.md`（schema/工作流）、`README.md`（顶层说明）
- 新增：`knowledge/` 骨架（`sources/`、`entities/`、`concepts/`、`topics/`、`synthesis/`、`queries/`、`assets/`）
- 新增：`knowledge/overview.md`、`knowledge/index.md`、`knowledge/log.md`
- 备注：Raw 层保留原状（`materials/raw/pdf_originals/`、`course/syllabus/`、`raw/`、`sources/`），脚本目录不动。

## [2026-05-21] ingest | 36 课时教学讲稿（course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md）

- 新增：`knowledge/sources/36课时讲稿.md`、`knowledge/sources/36课时大纲docx.md`
- 新增：`knowledge/topics/课程主页_36课时.md`、`knowledge/topics/week_01_课程导论.md`、`knowledge/topics/week_02_数据分析流程与复现规范.md`
- 新增：`knowledge/concepts/医药数据特征.md`、`knowledge/concepts/AI协作边界.md`、`knowledge/concepts/项目目录结构与可复现.md`
- 新增：`knowledge/concepts/工具分工_Python_R_Bash.md`
- 更新：`knowledge/overview.md`、`knowledge/index.md`

## [2026-05-21] ingest | AIDD Bioinformatics 课程（materials/raw/aidd_bioinformatics + materials/markdown/aidd_bioinformatics）

- 新增：`knowledge/sources/AIDD_Bioinformatics_Course.md`、`knowledge/sources/AIDD课程结构整理.md`
- 新增：`knowledge/concepts/生物编程.md`、`knowledge/concepts/RNA-seq上游流程.md`、`knowledge/concepts/Variant_Calling流程.md`、`knowledge/concepts/差异表达分析.md`
- 新增：`knowledge/entities/Python.md`、`knowledge/entities/R.md`、`knowledge/entities/Bash.md`、`knowledge/entities/Biopython.md`、`knowledge/entities/DESeq2.md`、`knowledge/entities/ggplot2.md`、`knowledge/entities/samtools.md`、`knowledge/entities/BLAST.md`、`knowledge/entities/GitHub.md`
- 备注：原始字幕为中文机翻，已通过 `scripts/convert/clean_aidd_subtitles.py` 校正主要术语（详见 `materials/raw/aidd_bioinformatics/TERMS.md`）。

## [2026-05-21] ingest | PDF 书库（materials/markdown/pdf_library_legacy/*.md）

- 新增：`knowledge/sources/ISLP.md`、`knowledge/sources/ISLR.md`、`knowledge/sources/Starting_Data_Analytics_GenAI.md`、`knowledge/sources/Learn_AI_Assisted_Python_Programming.md`
- 新增：`knowledge/entities/ChatGPT.md`、`knowledge/entities/GitHub_Copilot.md`
- 备注：4 本 PDF 已由 `scripts/convert/pdf_to_markdown.py` 转为 markdown，但仅做轻量摘要，未逐章展开。

## [2026-05-21] synthesis | 首批合成页

- 新增：`knowledge/synthesis/AIDD与36课时映射.md`、`knowledge/synthesis/三本Python书定位对比.md`、`knowledge/synthesis/知识缺口与后续素材.md`
- 更新：`knowledge/index.md`

## [2026-05-21] schema | 引入 memory.md

- 新增：`memory.md`（跨会话记忆：偏好 / 决策 / 阻塞 / 共识词汇 / 元反馈 / 反向规则）
- 更新：`AGENTS.md` —— 新会话开机三件事、4 个文件角色边界表、§3.5 Memorize 操作
- 更新：`README.md` —— 顶层目录与"4 个核心操作"前置三件事
- 触发：用户提议"是不是还应该有一个 memory.md 文件"。
- 备注：本文件记录"事实时间线"；偏好/决策/状态卡演化记录已迁移到 `memory.md`，两者各司其职。

## [2026-05-21] ingest | 富集分析 GO/KEGG/GSEA

- 新增：`knowledge/concepts/富集分析_GO_KEGG.md`（ORA / GSEA / clusterProfiler + 45 分钟教学路径 + 5 个常见坑）
- 更新：`knowledge/concepts/差异表达分析.md`（Week 11 位置补充富集链接）
- 更新：`knowledge/topics/课程主页_36课时.md`（Week 11 行）
- 更新：`knowledge/synthesis/AIDD与36课时映射.md`（标注 AIDD 未涉及此节）
- 更新：`knowledge/synthesis/知识缺口与后续素材.md`（划掉条目）
- 更新：`knowledge/index.md`（concept 计数 8→9）
- 触发：用户决定 Week 11 必须含富集分析（memory.md D-009）。

## [2026-05-21] infra | git 初始化

- 新增：`.gitignore`（排除 materials/raw/pdf_originals/、ai_logs/、projects/、.obsidian/workspace.json、Python/R 缓存等）
- 执行：`git init -b main` + 首次 commit（196 files, 41,064 insertions）
- commit 哈希：`8c971bf`
- 触发：用户同意加 git（memory.md D-007）。

## [2026-05-21] infra | Obsidian Vault 配置

- 新增：`.obsidian/`（app/appearance/core-plugins/community-plugins/graph/hotkeys）
- 新增：`knowledge/assets/obsidian_setup.md`（vault 边界、推荐插件、Graph 分色说明）
- 更新：`knowledge/index.md`（assets 区新增条目）
- 更新：`README.md`（Obsidian 入口指引）
- 配置要点：vault 根 = `F:\AI_Course\`；userIgnoreFilters 排除 raw 层重量级目录；Graph View 5 色分组。
- 触发：用户同意配 .obsidian（memory.md D-008）。

## [2026-05-21] infra | 推送 GitHub + 改为 Private

- 远端：`https://github.com/luvega/ai-bioinfo-wiki`（**Private**）
- 推送：commit `8c971bf` + `e512bc5` 已 push 到 origin/main
- 配置：本地仓库 `--local` 配 `http.proxy=http://127.0.0.1:10080`（仅本仓库，不污染全局；用户的 Clash/v2rayN 监听端口）
- 重要事件：push 完成后用户立即说"先不要 push 了"——push 已成功，
  随后用户决定保留远端但改为 Private，AI 用 `gh repo edit --visibility private` 完成切换。
- 教训记入 `memory.md` D-010 与 §5、§6（**后续推送/远端可见性/删除动作必须二次确认**）。

## [2026-05-22] infra | MinerU PDF 结构化转换流程

- 新增：`scripts/convert/mineru_pdf_pipeline.py`（PDF 清单、环境检查、本地 MinerU 批处理、主 Markdown 提升）
- 新增：`knowledge/synthesis/MinerU_PDF结构化转换方案.md`
- 新增：`docs/superpowers/plans/2026-05-22-mineru-pdf-structuring.md`
- 更新：`README.md`、`.gitignore`、`.obsidian/app.json`、`memory.md`、`knowledge/index.md`
- 生成目标：`materials/markdown/pdf_library_mineru/`；旧 `materials/markdown/pdf_library_legacy/` 暂不覆盖。
- 备注：已创建 `.venv-mineru`（Python 3.10.19）并安装 MinerU 3.1.15；烟测完成：
  `materials/markdown/pdf_library_mineru/R240_Learn_AI_Assisted_Python_Programming_With_GitHub_Copilot_and_ChatGPT_2023_Leo_Porter_Daniel_Zingaro/book.pages_0000_0002.mineru.md`。
  整本转换未在本次会话启动，预计耗时较长，后续按单本书运行。

## [2026-05-22] refactor | MinerU API-only 管线与本地环境清理

- 更新：`scripts/convert/mineru_pdf_pipeline.py` 改为 MinerU Precision API-only；使用 `page_ranges` 生成任务，不再调用本地 `mineru` CLI。
- 更新：`README.md`、`memory.md`、`knowledge/synthesis/MinerU_PDF结构化转换方案.md`、`docs/superpowers/plans/2026-05-22-mineru-pdf-structuring.md`。
- 清理：删除本地 `.venv-mineru`、CLI 烟测输出目录、失败的本地 PDF 分片缓存。
- 保留：`materials/markdown/pdf_library_mineru/INDEX.md`、`manifest.json`；后续 `api_parts.json`、`api_submissions.json`、`api_results.json` 可追踪，`api_zips/` 与 `api_raw/` 忽略。
- 备注：MinerU token 只允许通过 `MINERU_API_TOKEN` 环境变量传入；chat 中贴出的旧 token 视为已暴露，应重新生成。

## [2026-05-24] refactor | 课程备课优先目录重构

- 决策：wiki 不删除，但从主工作台降级为 `knowledge/`；课程产物主线改为 `course/weeks/` 与 `outputs/`。
- 迁移：`doc/` → `course/syllabus/`，`wiki/` → `knowledge/`，`pdf_originals/` → `materials/raw/pdf_originals/`，`raw/AIDD_Bioinformatics/` → `materials/raw/aidd_bioinformatics/`，`sources/` → `materials/markdown/`。
- 迁移：`嵩天Python/Pythonppt.pdf` → `materials/raw/external_ppt/嵩天Python/Pythonppt.pdf`，并登记为 `knowledge/sources/嵩天PythonPPT.md`。
- 新增：`course/weeks/week_01` 至 `week_18`，每周包含 `outline.md`、`script.md`、`materials.md`。
- 新增：`docs/superpowers/specs/2026-05-24-courseware-restructure-design.md` 与 `docs/superpowers/plans/2026-05-24-courseware-restructure.md`。
- 更新：`AGENTS.md`、`README.md`、`memory.md`、`.gitignore`、`.obsidian/app.json`、`scripts/convert/*`、`knowledge/index.md`、`knowledge/topics/课程主页_36课时.md`、`knowledge/sources/36课时讲稿.md`、`knowledge/synthesis/AIDD与36课时映射.md`。
- 备注：当前 36 课时主线以 `course/weeks/` 为准；第 11 周是科研图表规范，第 15 周是差异表达与功能解读。

## [2026-05-24] install | 项目本地 skills

- 输入：根目录 `skills.zip`。
- 安装：解压到 `skills/`，共 27 个 skill 目录，全部含 `SKILL.md`。
- 过滤：未安装 `__pycache__/` 与 `.pyc` 缓存文件。
- 备注：这是项目本地安装，不写入全局 `$CODEX_HOME/skills`；后续任务按需读取 `skills/<name>/SKILL.md`。

## [2026-05-24] query | MinerU 转换 materials PDF 的评估

- 复核：`https://mineru.net/apiManage/docs` 与 `https://mineru.net/`。
- 结论：本项目应继续使用 MinerU Precision API，而不是 Agent 轻量 API；轻量 API 页数/大小限制过低，不适合 5 个长 PDF。
- 更新：`scripts/convert/mineru_pdf_pipeline.py` 支持扫描 `materials/raw/pdf_originals/` 与 `materials/raw/external_ppt/`，并按当前文档将默认 `--max-pages` 改为 200，上传链接上限改为 50。
- 更新：`knowledge/synthesis/MinerU_PDF结构化转换方案.md` 与 `memory.md`，记录当前 API 限制、5 个 PDF 清单、课程化 Markdown 二次整理目标。
- 备注：未提交 API 任务，未写入 token。

## [2026-05-24] convert | MinerU Precision API 全量转换 materials PDF

- 烟测：`Learn_AI --max-pages 20 --limit 1` 跑通提交、轮询、下载、提升 Markdown。
- 修复：上传 OSS 签名 URL 时不能带 `Content-Type`；已将 `scripts/convert/mineru_pdf_pipeline.py` 的上传函数改为 `http.client` 直接 PUT。
- 全量：按 200 页分段提交 18 个任务，`api_results.json` 显示全部 `done`。
- 输出：5 个 `book.mineru.md` 已生成于 `materials/markdown/pdf_library_mineru/<slug>/`。
- 质量备注：复杂流程图存在 Mermaid/OCR 噪声，后续课程化整理应生成 `book.course.md` 与 `structure_report.md`。
- 安全备注：用户在 chat 中贴出的 token 已视为暴露；本次仅作为环境变量传入命令，未写入项目文件。建议后续在 MinerU 控制台轮换 token。

## [2026-05-24] generate | PDF 与 AIDD 课程化 Markdown

- 新增/更新：`scripts/courseware/mineru_course_markdown.py`，生成 PDF 课程化素材层并纳入 AIDD txt 讲义索引。
- PDF 输出：5 个 `book.course.md` 与 5 个 `structure_report.md`，位于 `materials/markdown/pdf_library_mineru/<slug>/`。
- AIDD 输出：`materials/markdown/aidd_bioinformatics/aidd.course_index.md`、`aidd.structure_report.md`，以及 11 个章节目录下的 `chapter.course.md`。
- 覆盖素材：5 本 PDF 的 MinerU Markdown + `materials/markdown/aidd_bioinformatics/` 下 71 个 txt 讲义。
- 备注：这些文件是备课索引/教学卡片，不替代原始 `book.mineru.md` 或 txt；进入 PPT 前仍需核对术语、公式、代码和图表。

## [2026-05-24] draft | 第一轮课程内容包

- 新增：`course/first_round_content.md`，作为第一轮内容审阅入口。
- 更新：`course/weeks/week_03/{materials,outline,script}.md`，形成 AI 辅助编程与 Python 快速入门首轮底稿。
- 更新：`course/weeks/week_14/{materials,outline,script}.md`，形成转录组数据分析基础首轮底稿。
- 更新：`course/weeks/week_15/{materials,outline,script}.md`，形成差异表达分析与功能解读首轮底稿。
- 更新：`course/weeks/week_16/{materials,outline,script}.md`，形成单细胞转录组可视化首轮底稿。
- 更新：`knowledge/index.md`，加入第一轮课程内容包入口。
- 备注：本轮内容是 PPT 生成前的可审稿底稿，后续需补 Week 03 代码练习、Week 15 示例表/火山图、Week 16 单细胞示例图。

## [2026-05-25] refactor | 项目根目录迁移到 E:\Codex_Projects

- 决策：当前有效项目根目录迁移为 `E:\Codex_Projects\AI_Course\`。
- 更新：`AGENTS.md`、`README.md`、`memory.md`、`knowledge/assets/obsidian_setup.md` 和 `docs/superpowers/plans/2026-05-25-project-root-migration.md`。
- 执行原则：先复制完整项目并校验，暂不删除旧 `F:\AI_Course\`，将其作为短期回退点。
