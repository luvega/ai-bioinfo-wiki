---
type: concept
title: 富集分析（GO / KEGG / GSEA）
status: stable
tags: [enrichment, go, kego, kegg, gsea, dge, week-11]
---

# 富集分析 · GO / KEGG / GSEA

## 一句话

**当差异基因列表太长无法逐个看时，富集分析帮我们回答："这些基因主要落在哪些通路 / 功能类别上？"**
本课程**第 15 周**作为 [差异表达分析](差异表达分析.md) 的下游功能解读一节。

## 三种主流方法

| 方法 | 输入 | 输出 | 数学本质 | R 实现 |
|---|---|---|---|---|
| **ORA**（Over-Representation Analysis） | 一个 DE 基因列表 + 背景基因集 | 每个通路一个 p-value | 超几何检验（Fisher's exact） | `clusterProfiler::enrichGO/enrichKEGG` |
| **GSEA**（Gene Set Enrichment Analysis） | 全部基因的有序列表（按 log2FC 排序） | 每个通路一个 NES + p-value | Kolmogorov-Smirnov 风格的 running ES | `clusterProfiler::gseGO/gseKEGG` |
| **SPIA**（Signaling Pathway Impact Analysis） | DE 基因 + 通路拓扑结构 | 每个通路 pPERT + pNDE | 考虑通路网络结构 | `SPIA::spia` |

本课程**主用 ORA + GSEA**，SPIA 作为进阶选讲。

## 三个基因集数据库

| 数据库 | 内容 | 大小 | 用途 |
|---|---|---|---:|
| **GO**（Gene Ontology） | 生物过程 BP / 分子功能 MF / 细胞组分 CC 三大类 | ~50,000 term | 概念性功能注释 |
| **KEGG**（Kyoto Encyclopedia of Genes and Genomes） | 信号通路 / 代谢通路 | ~500 通路 | 通路级解读 |
| **MSigDB**（Molecular Signatures Database） | Hallmark / C2 / C5 等多个 collection | 大量 | GSEA 标配 |

医药数据课程**优先用 KEGG + GO BP**，因为药学学生对 KEGG 通路图（如 "Apoptosis"、"PI3K-Akt"）有更直观的理解。

## 最小工作示例（R · clusterProfiler）

```r
library(clusterProfiler)
library(org.Hs.eg.db)
library(enrichplot)

# 假设 res 来自 DESeq2，sig_genes 是显著差异基因的 Ensembl ID 向量
sig_entrez <- bitr(sig_genes,
                   fromType = "ENSEMBL",
                   toType   = "ENTREZID",
                   OrgDb    = org.Hs.eg.db)$ENTREZID

# 1. GO 富集（BP）
ego <- enrichGO(gene          = sig_entrez,
                OrgDb         = org.Hs.eg.db,
                ont           = "BP",
                pAdjustMethod = "BH",
                qvalueCutoff  = 0.05,
                readable      = TRUE)
dotplot(ego, showCategory = 15)

# 2. KEGG 富集
ekegg <- enrichKEGG(gene = sig_entrez, organism = "hsa", pvalueCutoff = 0.05)
dotplot(ekegg, showCategory = 15)

# 3. GSEA（用全部基因，按 log2FC 排序）
gene_list <- res$log2FoldChange
names(gene_list) <- res$entrezid
gene_list <- sort(gene_list, decreasing = TRUE)

gsea_res <- gseKEGG(geneList = gene_list,
                    organism = "hsa",
                    pvalueCutoff = 0.05)
gseaplot2(gsea_res, geneSetID = 1)
```

## 常见可视化

| 图 | 函数 | 看什么 |
|---|---|---|
| Dot plot | `dotplot(ego)` | 各通路富集度 + 基因数 |
| Bar plot | `barplot(ego)` | 各通路 -log10(padj) |
| Cnet plot | `cnetplot(ego)` | 基因 ↔ 通路网络 |
| Emap plot | `emapplot(ego)` | 通路相似性聚类 |
| GSEA running plot | `gseaplot2(gsea_res)` | 单通路 running enrichment score |
| KEGG 通路图 | `pathview::pathview()` | 把 log2FC 上色到 KEGG 通路图 |

## 统计前提与坑

- **背景基因集要正确**：默认是"全基因组"，但若你的实验只能检出某子集（如低表达基因被过滤），
  背景应是"实际检出的基因"，否则会假富集。`clusterProfiler::enrichXXX(universe=...)` 显式指定。
- **多重检验校正**：默认 BH，与 [DESeq2](../entities/DESeq2.md) 的 padj 一致。
  → 理论支撑见 [ISLP Ch.13](../sources/ISLP.md)。
- **ORA vs GSEA 不要混用**：ORA 需要先定义"显著差异"阈值（如 padj<0.05 & |log2FC|>1），
  GSEA 不需要阈值，直接看全分布。两者**各有应用场景**：
  - 用 ORA 当差异显著且数量适中（几十到几百个基因）
  - 用 GSEA 当差异小但一致（基因集层面的微弱信号）
- **物种 OrgDb 选对**：人类用 `org.Hs.eg.db`，小鼠 `org.Mm.eg.db`，
  KEGG 用 `organism = "hsa" / "mmu"`。
- **解释要谨慎**：富集 ≠ 因果。"这条通路富集"只说明 DE 基因集中在该通路标注，
  **不能**直接推断"这条通路被激活/抑制"——后者需要看通路内基因的方向一致性 + 生物学验证。

## 在本课程中的位置

- **第 15 周**：差异表达分析与功能解读的下游一节（建议占 30-45 分钟）
- **第 11 周**：可把 dotplot、barplot、volcano、heatmap 作为科研图表规范案例，但不展开统计流程
- **第 17-18 周项目**：富集分析是医药相关项目（药物作用机制、疾病通路对比）的常见环节

## 教学路径建议（45 分钟一节）

| 时长 | 内容 |
|---:|---|
| 5' | 问题导入："上节课我们有 2,000 个 DE 基因，怎么读？" |
| 10' | ORA 直觉：Fisher 检验 + 一个最小例子 |
| 10' | GO / KEGG 数据库结构介绍 |
| 10' | R 代码 demo（不让学生现场跑，演示即可） |
| 5' | GSEA 直觉：为什么有时候 ORA 不够用 |
| 5' | 解释陷阱 + 常见错读 |

## AI 协作典型用法

```text
我用 DESeq2 跑出 2,300 个 padj<0.05 的 DE 基因。
我打算用 clusterProfiler 做 GO BP + KEGG 富集。
请帮我检查：
1. 我的背景基因集设置是否合理？
2. 看到结果时哪些列我应该先看？
3. 哪些常见误读我应该提防？
请不要直接给代码，先列检查清单。
```

## 与 AIDD 的关系

- AIDD [Ch.9](../sources/AIDD_Bioinformatics_Course.md) **没有讲富集分析**，
  这是本课程相对 AIDD 的明确加项，需要从 clusterProfiler vignette 等外部素材补。
- 后续可考虑 ingest 一份 `sources/clusterProfiler_vignette.md`。

## 相关页面

- 概念：[差异表达分析](差异表达分析.md)（上游）· [RNA-seq 上游流程](RNA-seq上游流程.md)（再上游）
- 实体：[R](../entities/R.md) · [DESeq2](../entities/DESeq2.md) · [ggplot2](../entities/ggplot2.md)
- 理论：[ISLP Ch.13 多重检验](../sources/ISLP.md)
- 来源：[36 课时讲稿第 15 周](../sources/36课时讲稿.md)

## 待办

> [!todo] 待 ingest：clusterProfiler 官方 vignette / Y 叔《生信菜鸟团》富集分析合集，
> 建一份 source 摘要页。
