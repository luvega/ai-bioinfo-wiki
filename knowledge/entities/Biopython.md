---
type: entity
name: Biopython
category: python-package
domain: [bioinformatics, sequence-analysis, file-formats, database]
status: stable
tags: [python, biopython, sequence, fasta, fastq, ncbi]
---

# Biopython

## 定位

Python 的生信瑞士军刀。本课程**非核心**，但在第 3 周演示
"Python 不止能算 glucose 均值，还能读 FASTA、查 NCBI"时拿出来当作扩展案例。

## 主要模块

| 模块 | 用途 | 示例 |
|---|---|---|
| `Bio.SeqIO` | 读写序列文件 | FASTA / FASTQ / GenBank / EMBL |
| `Bio.Seq` | 序列对象（DNA/RNA/蛋白） | 反向互补、翻译、长度 |
| `Bio.SeqUtils` | 序列属性 | GC 含量、分子量 |
| `Bio.Entrez` | NCBI 数据库 | esearch / efetch / einfo |
| `Bio.Blast` | BLAST 接口 | 本地 / 远程 |
| `Bio.AlignIO` | 多序列比对 | Clustal / MSA |
| `Bio.Phylo` | 系统发育树 | 读取 / 绘制 / 操作 |

## 在 AIDD 中

AIDD [Ch.2 Python Language for Bioinformatics](../sources/AIDD_Bioinformatics_Course.md) 共 10 节，
全部围绕 Biopython 展开。重点章节：
- §1 BioPython Introduction
- §4 Advance File Formats
- §5 Sequence Analysis
- §6 Database Retrieval (Entrez)
- §7 Working with Genomes
- §8 Phylogenetic Trees
- §9 Proteomics

## 在本课程中的位置

- **第 3 周**：作为"Python 不只是数据分析工具"的扩展案例。**只展示，不要求**。
- **第 17-18 周项目**：若有学生项目方向是序列分析（罕见），可作核心库使用。

## 与医药数据课程的关系

- 直接相关性：低（本课程不分析序列）
- 间接相关性：作为"Python 在生命科学中能做什么"的认知扩展。
- 教学价值：把 Python 从"算均值"提升到"调数据库 + 处理结构化生物数据"。

## 安装

```bash
pip install biopython
```

或在 R 用户视野下，作为 R `Biostrings` 包的 Python 对应物理解。

## 机翻陷阱

AIDD 字幕里 Biopython 模块名常被误识别：
- `SeqIO` → `sec.io`
- `Bio.SeqUtils` → `biosec.utils`
- `Bio.Seq` → `biosec`

详见 [TERMS.md](../../materials/raw/aidd_bioinformatics/TERMS.md)。

## 相关页面

- 概念：[生物编程](../concepts/生物编程.md)
- 实体：[Python](Python.md) · [BLAST](BLAST.md)
- 来源：[AIDD Ch.2](../sources/AIDD_Bioinformatics_Course.md)
