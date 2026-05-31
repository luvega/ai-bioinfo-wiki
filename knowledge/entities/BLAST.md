---
type: entity
name: BLAST
aka: [Basic Local Alignment Search Tool]
category: bioinformatics-tool
domain: [sequence-homology, alignment]
status: stable
tags: [bioinformatics, alignment, homology, ncbi]
---

# BLAST

## 定位

**Basic Local Alignment Search Tool**，NCBI 提供的同源序列检索工具。
本课程**非核心**，作为"生信工具的代表性例子"在第 5 周（数据读取与整形）或选修中提及。

## 程序家族

| 程序 | query | db | 用途 |
|---|---|---|---|
| `blastn` | DNA | DNA | 找 DNA 同源序列 |
| `blastp` | protein | protein | 找蛋白同源 |
| `blastx` | DNA → 6 框翻译 | protein | 找未知 ORF 的蛋白同源 |
| `tblastn` | protein | DNA → 6 框翻译 | 在基因组中找蛋白同源区 |
| `tblastx` | DNA → 6 框翻译 | DNA → 6 框翻译 | 远缘相似性 |

## 在线 vs 本地

- 在线：https://blast.ncbi.nlm.nih.gov/Blast.cgi
- 本地：`makeblastdb` + `blastn` 等命令，AIDD [Ch.4 §5](../sources/AIDD_Bioinformatics_Course.md) 演示。

## 典型命令

```bash
# 建库
makeblastdb -in ref.fasta -dbtype nucl -out ref_db

# 比对
blastn -query query.fa -db ref_db -outfmt 6 -evalue 1e-5 > hits.tsv

# tabular outfmt 6 列：
# qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore
```

## 课程中的位置

- 不是必学。仅在演示"NCBI 工具生态"或"如何确认未知序列来源"时举例。
- 若有学生项目方向涉及 PCR 引物设计、序列鉴定，BLAST 可作为核心工具。

## 相关页面

- 概念：[生物编程](../concepts/生物编程.md)
- 实体：[Bash](Bash.md) · [Biopython](Biopython.md)（`Bio.Blast`）
- 来源：[AIDD Ch.4](../sources/AIDD_Bioinformatics_Course.md)
