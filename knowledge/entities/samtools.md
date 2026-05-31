---
type: entity
name: samtools
aka: [SAM 工具-机翻误识]
category: cli-tool
domain: [ngs, sam, bam, alignment]
status: stable
tags: [bash, ngs, samtools, sam, bam]
---

# samtools

## 定位

处理 SAM/BAM/CRAM 文件的**事实标准命令行工具**。
RNA-seq 和 Variant Calling 流程都依赖它做 sort/index/view/fixmate。

## 常用命令

| 命令 | 用途 | 例 |
|---|---|---|
| `samtools view` | 查看 / 过滤 | `samtools view -b -q 30 in.bam > hq.bam` |
| `samtools sort` | 排序 | `samtools sort -o sorted.bam in.bam` |
| `samtools index` | 建索引（.bai） | `samtools index sorted.bam` |
| `samtools flagstat` | 统计比对率 | `samtools flagstat in.bam` |
| `samtools depth` | 覆盖度 | `samtools depth -a in.bam` |
| `samtools fixmate` | 修复配对信息 | `samtools fixmate -m in.bam out.bam` |
| `samtools merge` | 合并多 BAM | `samtools merge out.bam a.bam b.bam` |

## 典型使用片段

```bash
# RNA-seq / 一般场景
samtools sort -@ 4 -o sorted.bam aln.sam
samtools index sorted.bam
samtools flagstat sorted.bam

# Variant Calling 前的准备
samtools sort -n in.bam | samtools fixmate -m - - | \
  samtools sort -o fixed_sorted.bam - && samtools index fixed_sorted.bam
```

## 与 bcftools 的关系

- samtools 处理**比对结果**（SAM/BAM）
- [bcftools](#)（暂未建页）处理**变异结果**（VCF/BCF）
- 两者来源于同一开发团队（htslib），共享底层 API

## 课程中的位置

- **第 11 周**：作为 RNA-seq pipeline 的中间步骤一笔带过。
- **第 16 周 Variant Calling 选讲**：核心工具。
- **不要求学生上机跑**，作为命令行示范即可。

## 机翻陷阱

AIDD 字幕里被译为 "SAM 工具" / "sam tools"，请理解为 `samtools`。
详见 [TERMS.md](../../materials/raw/aidd_bioinformatics/TERMS.md)。

## 相关页面

- 概念：[RNA-seq 上游流程](../concepts/RNA-seq上游流程.md) · [Variant Calling 流程](../concepts/Variant_Calling流程.md)
- 实体：[Bash](Bash.md)
- 来源：[AIDD Ch.7, Ch.8](../sources/AIDD_Bioinformatics_Course.md)
- 官方：[samtools.github.io](http://www.htslib.org/)
