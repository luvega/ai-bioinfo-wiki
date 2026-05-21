---
type: concept
title: RNA-seq 上游流程（命令行 / Bash）
status: in_progress
tags: [rna-seq, ngs, pipeline, bash]
---

# RNA-seq 上游流程

## 流程图

```mermaid
flowchart LR
  A[SRA accession] -->|prefetch / fasterq-dump| B[FASTQ]
  B -->|FastQC| C[QC 报告]
  C -->|fastp / trim_galore| D[Trimmed FASTQ]
  D -->|HISAT2 / STAR| E[SAM]
  E -->|samtools sort / index| F[sorted.bam + .bai]
  F -->|featureCounts / HTSeq| G[count matrix]
  G --> H[DESeq2 / edgeR / limma]
```

来源：AIDD [Ch.7 NGS data Analysis on Bash](../sources/AIDD_Bioinformatics_Course.md)。

## 步骤详解

| 步骤 | 工具 | 输入 | 输出 | 关键参数 |
|---|---|---|---|---|
| 1. 获取数据 | SRA Toolkit (`prefetch`, `fasterq-dump`) | SRA accession | FASTQ | `--split-files` |
| 2. 质控 | FastQC / MultiQC | FASTQ | HTML 报告 | — |
| 3. 修剪 | fastp / Trim Galore / cutadapt | FASTQ | Trimmed FASTQ | quality threshold、adapter |
| 4. 比对 | HISAT2 / STAR / Bowtie2 | Trimmed FASTQ + reference | SAM | index 选择、`--quantMode` |
| 5. 排序索引 | [samtools](../entities/samtools.md) | SAM | sorted.bam + bam.bai | `sort`, `index` |
| 6. 计数 | featureCounts / HTSeq | sorted.bam + GTF | count matrix | `-s` strand 设定 |
| 7. 下游分析 | [DESeq2](../entities/DESeq2.md) / edgeR / limma | count matrix + metadata | DE 结果 | 见 [差异表达分析](差异表达分析.md) |

## 与本课程的关系

- **第 11 周**：差异表达分析必须前置说明 count matrix 是怎么来的。本流程提供一页 PPT
  概述（不要求学生上机跑），让学生理解输入数据的来历。
- **第 16 周**：组学数据综合分析时，可以让学生**用真实下游数据**（去 GEO 下载已发表的 count matrix），
  避免在课堂上跑完整 pipeline（资源/时间不允许）。

## 数据来源建议

- 公共数据：[GEO](https://www.ncbi.nlm.nih.gov/geo/)、[SRA](https://www.ncbi.nlm.nih.gov/sra)、ArrayExpress、ENCODE
- 教学数据：DESeq2 vignette 自带的 `airway`、`pasilla` 数据集
- 不推荐：未脱敏的临床转录组数据（伦理）

## 常见坑

- **strand 设置错误** → counts 全是 0。务必查测序文库说明。
- **GTF 与参考基因组版本不一致** → 比对成功但计数失败。
- **memory 限制**：STAR 需要 30+GB 内存，本课程不推荐在普通笔记本上跑。
- **机翻陷阱**：AIDD 字幕里 "bash 入门" 被译为 "贝叶斯入门"，看到时不要困惑。

## 相关页面

- 概念：[Variant Calling 流程](Variant_Calling流程.md)（结构相似，目标不同）· [差异表达分析](差异表达分析.md)
- 实体：[Bash](../entities/Bash.md) · [samtools](../entities/samtools.md) · [DESeq2](../entities/DESeq2.md)
- 来源：[AIDD Ch.7](../sources/AIDD_Bioinformatics_Course.md)

## 待办

> [!todo] 待 ingest：FastQC / fastp / HISAT2 / STAR / featureCounts 各建一份 entity 页。
