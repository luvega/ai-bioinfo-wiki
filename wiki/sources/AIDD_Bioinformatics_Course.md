---
type: source
title: AIDD Bioinformatics 视频课程（11 章 71 节）
raw_path:
  - raw/AIDD_Bioinformatics/
  - sources/AIDD_Bioinformatics/
ingested: 2026-05-21
language: zh-CN (机翻字幕，已术语校正)
kind: course-video-subtitles
status: stable
tags: [bioinformatics, python, r, bash, rna-seq, variant-calling, scrna-seq, microarray, github]
---

# AIDD Bioinformatics 课程

## 一句话定位

这套课的全名是 **"Bioinformatics Data Analysis Crash Course Python R and Linux"**，
是一门面向生信初学者的跨工具入门课。在本课程中，它的角色是
**“给特定周次提供具体案例与命令行示例”的素材池**，不能照搬。

## 基本统计

- 章节：11 章（实际编号 1-10、12，缺第 11 章）
- 课程数：71 节
- 累计时长：约 773 分钟（≈ 12.9 小时）
- 字幕字符数：约 193,493
- 字幕语言：中文机翻（WEBVTT 格式，扩展名 `.srt`/`.vtt` 互为镜像）
- 清理脚本：[`scripts/clean_aidd_subtitles.py`](../../scripts/clean_aidd_subtitles.py)
- 术语校正词典：[`raw/AIDD_Bioinformatics/TERMS.md`](../../raw/AIDD_Bioinformatics/TERMS.md)
- 章节索引：[`raw/AIDD_Bioinformatics/INDEX.md`](../../raw/AIDD_Bioinformatics/INDEX.md)

## 主线（按章节）

| Ch | 主题 | 课数 | 时长 | 课程中嵌入位置 |
|---:|---|---:|---:|---|
| 1 | 生物编程总览（PY/R/Linux） | 2 | 21' | 第 1 周 |
| 2 | Biopython（序列/格式/数据库/系统发育/蛋白/ML） | 10 | 152' | 第 3 周 + 后续选用 |
| 3 | Tkinter 生信桌面工具开发（4 个项目） | 15 | 133' | 选修 / 第 17-18 周项目实战 |
| 4 | Bash 生信基础（命令/E-utilities/BLAST/比对/系统发育） | 7 | 93' | 第 2、5 周（命令行 + pipeline 思维） |
| 5 | Linux for Windows（WSL） | 1 | 5' | 第 2 周 |
| 6 | Bioinformatics Pipeline 概念 | 1 | 8' | 第 2 周 |
| 7 | NGS / RNA-seq 命令行流程（SRA→FastQC→trim→align→count） | 7 | 55' | 第 11、16 周 |
| 8 | Variant Calling（SRA→QC→align→samtools/bcftools→VCF→IGV） | 9 | 60' | 第 16 周 / 项目 |
| 9 | R for Bioinformatics（DESeq2 / ggplot2 / scRNA-seq） | 9 | 101' | 第 4、11、14 周 |
| 10 | Microarray Analysis（GEO2R / R） | 4 | 84' | 第 15 周 |
| 12 | GitHub Guide | 6 | 51' | 第 2、17、18 周 |

详细章节-周次对应见 [AIDD 与 36 课时映射](../synthesis/AIDD与36课时映射.md)。

## 课程的核心价值（在本课程语境下）

- **跨语言对照**：同一类任务（如序列处理、差异表达）在 Python、R、Bash 三种工具下分别如何完成。
- **真实命令行流程**：RNA-seq、Variant Calling 都给出从下载到可视化的完整命令序列。
- **生信特有的格式直觉**：FASTA / FASTQ / SAM / BAM / VCF 的文件特征 → 可类比迁移到医药数据的 CSV/Excel/长宽表。
- **GEO2R / DESeq2 的“开盒即用”用例**：第 11、15 周直接借用。

## 课程的局限（避免被它带偏）

- **字幕机翻**：DESeq2 被译为“DSEC2”、bash 被译为“贝叶斯”等，需依赖术语词典与人工核对。
- **生信本位**：课程对象是生信初学者，本课程对象是药学学生，**临床/药学数据的特征**它没讲，需要由 36 课时讲稿补齐。
- **缺少统计基础**：差异表达直接进入 DESeq2 调用，没有讲“为什么是负二项分布”——这需要 [ISLP/ISLR](ISLP.md) 与 36 课时第 8-10 周补。
- **章节缺口**：第 11 章不存在；第 3、7、8 章存在课程序号缺口（详见 `raw/.../INDEX.md`）。
- **Tkinter 桌面工具部分**对当前课程价值有限，仅作为“工具开发意识”的展示素材。

## 衍生页（在本 wiki 中已建）

### 概念
- [生物编程](../concepts/生物编程.md)（Ch.1）
- [工具分工_Python_R_Bash](../concepts/工具分工_Python_R_Bash.md)（Ch.1, Ch.4, Ch.9）
- [RNA-seq 上游流程](../concepts/RNA-seq上游流程.md)（Ch.7）
- [Variant Calling 流程](../concepts/Variant_Calling流程.md)（Ch.8）
- [差异表达分析](../concepts/差异表达分析.md)（Ch.9 §4-7）

### 实体
- [Python](../entities/Python.md) · [R](../entities/R.md) · [Bash](../entities/Bash.md)
- [Biopython](../entities/Biopython.md) · [DESeq2](../entities/DESeq2.md) · [ggplot2](../entities/ggplot2.md)
- [samtools](../entities/samtools.md) · [BLAST](../entities/BLAST.md) · [GitHub](../entities/GitHub.md)

### 待建（按需 ingest 时再展开）
- `concepts/scRNA-seq.md`（Ch.9 §8-9）
- `concepts/Microarray分析.md`（Ch.10）
- `concepts/系统发育树.md`（Ch.2 §8 + Ch.4 §7）
- `concepts/蛋白质组学入门.md`（Ch.2 §9）
- `concepts/机器学习在生信中.md`（Ch.2 §10）
- `entities/Seurat.md`、`entities/GEO2R.md`、`entities/bcftools.md`、`entities/FastQC.md`、`entities/SRA_Toolkit.md`、`entities/IGV.md`、`entities/Tkinter.md`、`entities/PyInstaller.md`

## 相关页面

- 同源（人写综述）：[AIDD 课程结构整理](AIDD课程结构整理.md)
- 课程总线：[36 课时讲稿](36课时讲稿.md)
- 映射：[AIDD 与 36 课时映射](../synthesis/AIDD与36课时映射.md)

## 勘误 / 注意

- AIDD 字幕中常见机翻错误已在 [TERMS.md](../../raw/AIDD_Bioinformatics/TERMS.md) 列出。
  典型例：`DSEC2` → `DESeq2`；`RNA-SEC` → `RNA-seq`；`氧化铝平台` → `Illumina 平台`；
  `贝叶斯入门` 实为 `bash 入门`。
- 引用 AIDD 任何一句话之前请回到对应 `.txt` 校对一次。
