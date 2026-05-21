# Wiki 内容目录（index.md）

> **wiki 的轻量级 RAG 索引**。回答用户问题前，先 grep 这里。
> 每次 ingest / refactor 都要更新本页。
> 条目格式：`[<标题>](<相对路径>) — <一句话摘要> · <status> · <tags>`

---

## 🏠 顶层

- [overview](overview.md) — wiki 主页与导读 · stable · `overview, map`
- [index](index.md) — 本目录 · stable · `index`
- [log](log.md) — 时间线（append-only） · stable · `log, timeline`

## 📚 Sources（原始素材的摘要页）

- [36课时讲稿](sources/36课时讲稿.md) — 18 周教学讲稿（人写），课程事实主大纲 · stable · `course, syllabus, lecture-notes`
- [36课时大纲docx](sources/36课时大纲docx.md) — Word 原件，正式报备版本 · stable · `course, source-of-truth`
- [AIDD_Bioinformatics_Course](sources/AIDD_Bioinformatics_Course.md) — 71 节生信入门字幕（已校正） · stable · `bioinformatics, course-video`
- [AIDD课程结构整理](sources/AIDD课程结构整理.md) — AIDD 11 章人写综述 · stable · `aidd, course-structure`
- [ISLP](sources/ISLP.md) — ISLP《Statistical Learning with Python》 · stable · `statistical-learning, python`
- [ISLR](sources/ISLR.md) — ISLR《Statistical Learning with R》 · stable · `statistical-learning, r`
- [Starting_Data_Analytics_GenAI](sources/Starting_Data_Analytics_GenAI.md) — Manning GenAI 数据分析工作流 · stable · `generative-ai, data-analytics`
- [Learn_AI_Assisted_Python_Programming](sources/Learn_AI_Assisted_Python_Programming.md) — Manning Copilot/ChatGPT 编程教学法 · stable · `copilot, chatgpt, python`

## 🧱 Entities（具体实体）

### 语言 / Shell
- [Python](entities/Python.md) — 通用语言，本课程第一语言 · stable · `language, python`
- [R](entities/R.md) — 统计与生信主导语言 · stable · `language, r, statistics`
- [Bash](entities/Bash.md) — 命令行 / 流程胶水 · stable · `bash, pipeline`

### Python 库
- [Biopython](entities/Biopython.md) — Python 生信瑞士军刀 · stable · `python, sequence, ncbi`

### R 包
- [DESeq2](entities/DESeq2.md) — RNA-seq 差异表达分析事实标准 · stable · `r, bioconductor, dge`
- [ggplot2](entities/ggplot2.md) — R 科研绘图事实标准 · stable · `r, visualization`

### 命令行工具
- [samtools](entities/samtools.md) — SAM/BAM 处理事实标准 · stable · `bash, ngs`
- [BLAST](entities/BLAST.md) — NCBI 同源检索工具 · stable · `bioinformatics, alignment`

### 平台 / AI 工具
- [GitHub](entities/GitHub.md) — 代码托管 + 版本控制 · stable · `git, github, version-control`
- [GitHub Copilot](entities/GitHub_Copilot.md) — IDE 内 AI 行内补全 · stable · `ai, copilot`
- [ChatGPT](entities/ChatGPT.md) — 通用对话式 LLM · stable · `ai, chatgpt, llm`

### 待建（参见 [synthesis/知识缺口](synthesis/知识缺口与后续素材.md)）
- Seurat / GEO2R / limma / bcftools / BWA / HISAT2 / STAR / FastQC / fastp / SRA_Toolkit / IGV / Tkinter / PyInstaller / NCBI_E-utilities / Ensembl / GEO

## 💡 Concepts（抽象概念）

### 课程框架级
- [医药数据特征](concepts/医药数据特征.md) — 多源 / 高维 / 异质 / 强解释 · stable · `pharmacy-data`
- [工具分工_Python_R_Bash](concepts/工具分工_Python_R_Bash.md) — 三类工具的角色与边界 · stable · `tooling`
- [AI 协作边界](concepts/AI协作边界.md) — 三阶段边界 + 6 字段记录 + 三红线 · stable · `ai-assisted`
- [项目目录结构与可复现](concepts/项目目录结构与可复现.md) — 6 子目录 + 命名规则 · stable · `reproducibility`
- [生物编程](concepts/生物编程.md) — 用编程解决生命科学问题 · stable · `bioinformatics`

### 生信流程
- [RNA-seq 上游流程](concepts/RNA-seq上游流程.md) — SRA→FASTQ→QC→align→count · in_progress · `rna-seq, pipeline`
- [Variant Calling 流程](concepts/Variant_Calling流程.md) — SRA→FASTQ→align→VCF · in_progress · `variant-calling, pipeline`
- [差异表达分析](concepts/差异表达分析.md) — DESeq2 / edgeR / limma 比较 + 统计前提 · in_progress · `dge`
- [富集分析 GO/KEGG](concepts/富集分析_GO_KEGG.md) — ORA / GSEA / clusterProfiler + 解释陷阱 · stable · `enrichment, go, kegg, gsea`

### 待建（参见 [synthesis/知识缺口](synthesis/知识缺口与后续素材.md)）
- pandas入门 / 假设检验决策树 / 多重检验校正 / 交叉验证 / PCA与聚类 / scRNA-seq / Microarray分析

## 📅 Topics（教学单元）

- [课程主页_36课时](topics/课程主页_36课时.md) — 36 课时 hub，含 18 周状态表 · in_progress · `course, hub`
- [week_01_课程导论](topics/week_01_课程导论.md) — 第 1 周 · stable · `intro, week-01`
- [week_02_数据分析流程与复现规范](topics/week_02_数据分析流程与复现规范.md) — 第 2 周 · stable · `reproducibility, week-02`

### 待建（参见 [课程主页_36课时](topics/课程主页_36课时.md)）
- week_03 ~ week_18

## 🔭 Synthesis（综合 / 对比 / 思考）

- [AIDD 与 36 课时映射](synthesis/AIDD与36课时映射.md) — AIDD 章节如何嵌入 36 课时 · stable · `mapping`
- [三本 Python 书定位对比](synthesis/三本Python书定位对比.md) — ISLP / GenAI / Copilot 三本书的角色 · stable · `book-compare`
- [知识缺口与后续素材](synthesis/知识缺口与后续素材.md) — 缺口清单 / wiki 购物清单 · in_progress · `gap-analysis, todo`

## 📨 Queries（历史问答归档）

- *暂无*

## 🗃 Assets（模板 / 图表 / 共享资源）

- [obsidian_setup](assets/obsidian_setup.md) — Vault 配置、推荐插件、Graph View 分色 · stable · `obsidian, setup`

---

## 当前规模

- Sources：8
- Entities：11（待建 16）
- Concepts：9（待建 7）
- Topics：3（待建 16）
- Synthesis：3
- 合计：34 页（实建）+ ~39 页（计划中）

## 维护提示

- 新增页 → 加到对应分类。
- 修改/删除页 → 同步更新本页。
- 月度 lint → 检查孤岛页、矛盾、stale 标记。
