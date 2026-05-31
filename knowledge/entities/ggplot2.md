---
type: entity
name: ggplot2
category: r-cran-package
domain: [visualization, grammar-of-graphics]
status: stable
tags: [r, visualization, plot, grammar-of-graphics, tidyverse]
---

# ggplot2

## 定位

R 的**科研绘图事实标准**。本课程**第 7、11、12 周**反复使用。
风格基于 "Grammar of Graphics"：图 = 数据 + 映射 + 几何对象 + 统计变换 + 坐标系 + 主题。

## 最小可工作示例

```r
library(ggplot2)
ggplot(data = iris,
       mapping = aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(size = 2, alpha = 0.7) +
  theme_minimal() +
  labs(title = "Iris", x = "Sepal length (cm)", y = "Sepal width (cm)")
```

## 关键概念

| 概念 | 函数 | 角色 |
|---|---|---|
| 数据 | `data =` | 数据框 |
| 映射 | `aes()` | 列名 → 视觉通道 |
| 几何 | `geom_*` | 点 / 线 / 柱 / 箱 / 等 |
| 统计变换 | `stat_*` / `geom_*(stat=)` | 在几何前对数据做聚合 |
| 分面 | `facet_wrap()` / `facet_grid()` | 多面板 |
| 比例 | `scale_*` | x/y 轴刻度、颜色 |
| 主题 | `theme_*` + `theme()` | 排版细节 |
| 标注 | `labs()` / `annotate()` | 标题 / 标签 |

## 课程中典型用法

| 周 | 图类型 | geom |
|---:|---|---|
| 7 | 直方图 / 散点 / 箱图 / 折线 | `geom_histogram`、`geom_point`、`geom_boxplot`、`geom_line` |
| 9 | 拟合线 | `geom_smooth(method = "lm")` |
| 11 | 火山图 | `geom_point` + `geom_text_repel` |
| 12 | PCA scatter | `geom_point` + `stat_ellipse` |
| 12 | 热图 | 不用 ggplot2，用 `pheatmap` / `ComplexHeatmap` |

## 与 DESeq2 结果对接

```r
library(ggplot2); library(ggrepel)

res_df <- as.data.frame(res) |>
  dplyr::mutate(sig = padj < 0.05 & abs(log2FoldChange) > 1)

ggplot(res_df, aes(x = log2FoldChange, y = -log10(padj), color = sig)) +
  geom_point(alpha = 0.5) +
  geom_vline(xintercept = c(-1, 1), linetype = "dashed") +
  geom_hline(yintercept = -log10(0.05), linetype = "dashed") +
  scale_color_manual(values = c("grey70", "firebrick")) +
  theme_classic()
```

## 与 AI 协作

- AI 写 ggplot2 代码出错率较低，但**配色、字体、主题**经常不符合期刊审稿要求。
- 推荐 prompt：明确"投稿期刊样式"（Cell / Nature / NEJM 各有偏好）。

## 与 AIDD 的关系

AIDD [Ch.9 §7](../sources/AIDD_Bioinformatics_Course.md) 简要介绍 ggplot2，
但**没有讲 grammar of graphics 的哲学**。本课程第 7 周应补这部分（一页 PPT 即可）。

## 相关页面

- 概念：[差异表达分析](../concepts/差异表达分析.md)
- 实体：[R](R.md) · [DESeq2](DESeq2.md)
- 来源：[AIDD Ch.9](../sources/AIDD_Bioinformatics_Course.md)
