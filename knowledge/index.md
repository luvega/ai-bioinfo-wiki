# Knowledge 内容目录（index.md）

> **knowledge 的轻量级 RAG 索引**。回答项目问题前，先 grep 这里；写课件时以 `course/` 为主线，回到本目录取素材、实体和概念。
> 每次 ingest / refactor 都要同步更新本页。
> 条目格式：`[<标题>](<相对路径>) — <一句话摘要> · <status> · <tags>`

---

## 顶层

- [overview](overview.md) — 知识地图与导读 · stable · `overview, map`
- [index](index.md) — 本目录 · stable · `index`
- [log](log.md) — 时间线（append-only） · stable · `log, timeline`

## Courseware（授课产物主线）

- [course/weeks](../course/weeks/) — 18 周课件工作区；每周含 `outline.md`、`script.md`、`materials.md` · draft · `courseware, ppt`
- [course/first_round_content](../course/first_round_content.md) — 第一轮课程内容包，覆盖 Week 03、14、15、16 的素材映射、PPT 大纲与授课脚本 · first_round · `courseware, ppt-outline`
- [course/syllabus](../course/syllabus/) — 36 课时 docx / 讲稿 / AIDD 人写整理 · stable · `syllabus, source-of-truth`
- [course/templates](../course/templates/) — 后续 PPT / 讲稿模板目录 · draft · `templates`
- [outputs](../outputs/) — 生成的 PPT、讲稿、讲义输出目录 · generated · `outputs`

## Sources（原始素材摘要页）

- [36课时讲稿](sources/36课时讲稿.md) — 18 周教学讲稿（人写），课程事实主大纲 · stable · `course, syllabus, lecture-notes`
- [36课时大纲docx](sources/36课时大纲docx.md) — Word 原件，正式报备版本 · stable · `course, source-of-truth`
- [AIDD_Bioinformatics_Course](sources/AIDD_Bioinformatics_Course.md) — AIDD 生信入门字幕与章节索引 · stable · `bioinformatics, course-video`
- [AIDD课程结构整理](sources/AIDD课程结构整理.md) — AIDD 课程的人写二手综述 · stable · `aidd, course-structure`
- [ISLP](sources/ISLP.md) — ISLP《Statistical Learning with Python》 · stable · `statistical-learning, python`
- [ISLR](sources/ISLR.md) — ISLR《Statistical Learning with R》 · stable · `statistical-learning, r`
- [Single_Cell_Best_Practices](sources/Single_Cell_Best_Practices.md) — scRNA-seq / multimodal single-cell Jupyter Book，含 notebook、代码、输出和数据入口清单 · generated_draft · `single-cell, scRNA-seq`
- [OWF_Learn_Git](sources/OWF_Learn_Git.md) — Open Water Foundation Git 教程，固定 commit 入库，服务 Week 02/03/17 的版本控制与复现规范 · source_ingested · `git, version-control`
- [OWF_Learn_Windows_Shell](sources/OWF_Learn_Windows_Shell.md) — Open Water Foundation Windows shell 教程，服务 Week 02/03/17 的命令行、批处理和故障排查 · source_ingested · `windows-shell, reproducibility`
- [OWF_Learn_Linux_Shell](sources/OWF_Learn_Linux_Shell.md) — Open Water Foundation Linux shell 教程，服务 Week 02/03/17 的 Bash、脚本和日志参考 · source_ingested · `linux-shell, bash`
- [Starting_Data_Analytics_GenAI](sources/Starting_Data_Analytics_GenAI.md) — Manning GenAI 数据分析工作流 · stable · `generative-ai, data-analytics`
- [Learn_AI_Assisted_Python_Programming](sources/Learn_AI_Assisted_Python_Programming.md) — Manning Copilot / ChatGPT 编程教学法 · stable · `copilot, chatgpt, python`
- [嵩天 Python PPT](sources/嵩天PythonPPT.md) — 中文 Python PPT 外部参考源，待结构化抽取 · draft · `python, slides`

## Entities（具体实体）

### 语言 / Shell

- [Python](entities/Python.md) — 通用语言，本课程第一语言 · stable · `language, python`
- [R](entities/R.md) — 统计与生信主导语言 · stable · `language, r, statistics`
- [Bash](entities/Bash.md) — 命令行 / 流程胶水 · stable · `bash, pipeline`

### Python 库

- [Biopython](entities/Biopython.md) — Python 生信基础库 · stable · `python, sequence, ncbi`

### R 包

- [DESeq2](entities/DESeq2.md) — RNA-seq 差异表达分析事实标准，当前课程主位置为第 15 周 · stable · `r, bioconductor, dge`
- [ggplot2](entities/ggplot2.md) — R 科研绘图事实标准，可服务第 11 周图表规范 · stable · `r, visualization`

### 命令行工具

- [samtools](entities/samtools.md) — SAM/BAM 处理事实标准 · stable · `bash, ngs`
- [BLAST](entities/BLAST.md) — NCBI 同源检索工具 · stable · `bioinformatics, alignment`

### 平台 / AI 工具

- [GitHub](entities/GitHub.md) — 代码托管与版本控制平台 · stable · `git, github, version-control`
- [GitHub Copilot](entities/GitHub_Copilot.md) — IDE 内 AI 行内补全 · stable · `ai, copilot`
- [ChatGPT](entities/ChatGPT.md) — 通用对话式 LLM · stable · `ai, chatgpt, llm`

## Concepts（抽象概念）

### 课程框架级

- [医药数据特征](concepts/医药数据特征.md) — 多源 / 高维 / 异质 / 强解释 · stable · `pharmacy-data`
- [工具分工_Python_R_Bash](concepts/工具分工_Python_R_Bash.md) — 三类工具的角色与边界 · stable · `tooling`
- [AI 协作边界](concepts/AI协作边界.md) — 三阶段边界、记录字段与红线 · stable · `ai-assisted`
- [项目目录结构与可复现](concepts/项目目录结构与可复现.md) — 项目目录、命名与复现边界 · stable · `reproducibility`
- [生物编程](concepts/生物编程.md) — 用编程解决生命科学问题 · stable · `bioinformatics`

### 生信流程

- [RNA-seq 上游流程](concepts/RNA-seq上游流程.md) — SRA→FASTQ→QC→align→count · in_progress · `rna-seq, pipeline`
- [Variant Calling 流程](concepts/Variant_Calling流程.md) — SRA→FASTQ→align→VCF · in_progress · `variant-calling, pipeline`
- [差异表达分析](concepts/差异表达分析.md) — DESeq2 / edgeR / limma 比较与统计前提；课程主位置为第 15 周 · in_progress · `dge`
- [富集分析 GO/KEGG](concepts/富集分析_GO_KEGG.md) — ORA / GSEA / clusterProfiler 与解释陷阱 · stable · `enrichment, go, kegg, gsea`

## Topics（knowledge 层教学主题页）

- [课程主页_36课时](topics/课程主页_36课时.md) — 36 课时 hub，指向 `course/weeks/` 的 18 周主线 · in_progress · `course, hub`
- [week_01_课程导论](topics/week_01_课程导论.md) — 第 1 周旧版主题页，后续并入 `course/weeks/week_01/` · stable · `intro, week-01`
- [week_02_数据分析流程与复现规范](topics/week_02_数据分析流程与复现规范.md) — 第 2 周旧版主题页，后续并入 `course/weeks/week_02/` · stable · `reproducibility, week-02`

## Synthesis（综合 / 对比 / 思考）

- [AIDD 与 36 课时映射](synthesis/AIDD与36课时映射.md) — AIDD 章节如何嵌入 36 课时 · stable · `mapping`
- [三本 Python 书定位对比](synthesis/三本Python书定位对比.md) — ISLP / GenAI / Copilot 三本书的角色 · stable · `book-compare`
- [知识缺口与后续素材](synthesis/知识缺口与后续素材.md) — 缺口清单与后续 ingest 候选 · in_progress · `gap-analysis, todo`
- [MinerU PDF 结构化转换方案](synthesis/MinerU_PDF结构化转换方案.md) — 参考书 PDF 的 MinerU 转换路线、目录边界与质量检查 · in_progress · `mineru, pdf, course-ops`

## Queries（历史问答归档）

- *暂无*

## Assets（模板 / 图表 / 共享资源）

- [obsidian_setup](assets/obsidian_setup.md) — Vault 配置、推荐插件、Graph View 分色 · stable · `obsidian, setup`

---

## 当前规模

- Knowledge 页：46（含顶层 3、sources 15、entities 11、concepts 9、topics 3、synthesis 4、assets 1）
- Courseware 周目录：18（每周 `outline.md` / `script.md` / `materials.md`）
- 当前主线：先从 `course/weeks/` 产出 PPT 大纲与脚本，再按需回填 `knowledge/`。

## 维护提示

- 新增素材 → 先放入 `materials/raw/` 或 `materials/markdown/`，再在 `knowledge/sources/` 登记。
- 课程结构变化 → 先改 `course/weeks/`，再同步 `knowledge/topics/课程主页_36课时.md` 与本页。
- 生成文件 → 统一写入 `outputs/`，不要混入 raw / knowledge / syllabus。
