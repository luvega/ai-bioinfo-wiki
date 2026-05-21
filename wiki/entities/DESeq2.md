---
type: entity
name: DESeq2
aka: [Deseq2, DSEC2-机翻误识]
category: r-bioconductor-package
domain: [rna-seq, differential-expression, statistics]
status: stable
tags: [r, bioconductor, dge, negative-binomial]
---

# DESeq2

## 定位

Bioconductor 上**最主流的 RNA-seq 差异表达分析包**，本课程第 11 周的核心工具。

## 关键 API

```r
library(DESeq2)

# 1. 构建对象
dds <- DESeqDataSetFromMatrix(countData = counts, colData = metadata, design = ~ condition)

# 2. 标准化 + 差异分析
dds <- DESeq(dds)

# 3. 提取结果
res <- results(dds, contrast = c("condition", "treated", "control"))
summary(res)

# 4. shrinkage（推荐用于 LFC 画图）
res_shrunk <- lfcShrink(dds, coef = "condition_treated_vs_control", type = "apeglm")

# 5. 转换矩阵用于可视化
vsd <- vst(dds, blind = FALSE)   # variance stabilizing transform
plotPCA(vsd, intgroup = "condition")
```

## 统计模型（一句话）

**负二项分布广义线性模型 + 分散度收缩 + log2FoldChange shrinkage + BH 多重检验校正**。

为什么是负二项？因为 RNA-seq count 数据**均值 ≠ 方差**（过分散），泊松分布不够。

## 与教材的对接

- AIDD [Ch.9 §4-7](../sources/AIDD_Bioinformatics_Course.md)：直接给命令，缺统计解释。
- [ISLP Ch.13](../sources/ISLP.md)：补"多重检验校正"理论。
- 推荐教学顺序：先讲为什么需要校正（ISLP）→ 再讲 DESeq2 怎么做（AIDD）→ 上机调参。

## 常见坑

1. **输入必须是 raw count**（整数），不要喂 TPM/FPKM/CPM。
2. `design` 设计矩阵的顺序决定参考水平。若想指定参考：
   ```r
   metadata$condition <- factor(metadata$condition, levels = c("control", "treated"))
   ```
3. **n=1/组不能做**，n=2 可以但不可信。**最小 n=3/组**。
4. **批次效应**写进 design：`~ batch + condition`，**`batch` 在 `condition` 之前**。
5. `padj = NA`：表示该基因被自动过滤（低表达），不是 bug。

## 课程中的位置

- **第 11 周**：核心案例
- **第 12 周**：用 DEA 结果做 volcano、heatmap、PCA
- **第 14 周**：scRNA-seq 中类似思路（FindMarkers），但工具不同

## 机翻陷阱

AIDD 字幕中 DESeq2 被译为：`DSEC`、`DSEC2`、`Deseq2`、"地址 2"。
脚本 [`scripts/clean_aidd_subtitles.py`](../../scripts/clean_aidd_subtitles.py) 已统一替换。

## 相关页面

- 概念：[差异表达分析](../concepts/差异表达分析.md) · [RNA-seq 上游流程](../concepts/RNA-seq上游流程.md)
- 实体：[R](R.md) · [ggplot2](ggplot2.md)
- 来源：[AIDD Ch.9](../sources/AIDD_Bioinformatics_Course.md) · [36 课时讲稿第 11 周](../sources/36课时讲稿.md)
