---
type: course-week
week: 14
title: 转录组数据分析基础
hours: 2
status: first_round
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 14 周：转录组数据分析基础 · PPT 大纲

## 教学目标

- 说明 RNA-seq 的目标是测量基因表达水平。
- 描述从 FASTQ 到 count matrix 的基本流程。
- 区分 FASTQ、SAM/BAM、count matrix 和 metadata 的角色。
- 理解为什么原始 counts 不能直接跨样本比较。
- 能用 AI 辅助梳理流程，但知道哪些步骤需要人工核验。

## PPT 结构

1. 标题页：转录组数据分析基础
2. 导入问题：表达矩阵是从哪里来的
3. RNA-seq 要回答什么问题
4. 从样本到 reads：测序数据不是表格
5. 核心流程总览：FASTQ 到 count matrix
6. FASTQ 与质量控制：为什么先看质量
7. Trimming：为什么要修剪低质量 reads
8. Alignment：reads 如何回到参考基因组
9. SAM/BAM：比对结果为什么需要排序和索引
10. Feature extraction：从 reads 到基因计数
11. Count matrix 与 metadata：后续统计的输入
12. 标准化直觉：测序深度不同导致不可直接比较
13. 课堂练习：检查样本名、总 counts 和分组
14. AI 协作：让 AI 按输入、步骤、输出、质量问题整理流程
15. 小结：理解数据链条，才谈得上差异表达

## 流程板书

```text
SRA / FASTQ
  -> quality control
  -> trimming
  -> alignment to reference genome
  -> SAM / BAM
  -> sorting and indexing
  -> feature extraction
  -> count matrix + metadata
  -> normalization and statistical analysis
```

## 课堂练习

给定一个小型 count matrix 和 metadata，要求学生：

1. 判断行和列分别代表什么。
2. 检查样本名是否与 metadata 对齐。
3. 计算每个样本总 counts。
4. 解释总 counts 差异为什么会影响组间比较。

## 推荐提示词

```text
请帮我解释 RNA-seq 从 FASTQ 到 count matrix 的流程。请按“输入文件、处理步骤、输出文件、可能质量问题”四列说明，并标出哪些环节需要人工核验。
```

## 待补强

- 增补 1 张 FASTQ/SAM/BAM/count matrix 的文件角色对照图。
- 从 AIDD txt 中回查 feature extraction 相关命令，决定是否进入 PPT 附录。
## 样板周质量区块

### 药学问题入口
药学研究常从“处理组是否改变基因表达”开始，本周先解释表达矩阵从何而来。

### 核心数据结构
FASTQ、SAM/BAM、count matrix、metadata、样本总 counts、基因 x 样本矩阵。

### 课堂任务
读取小型 count matrix，检查 metadata 对齐，计算样本总 counts，并解释为什么原始 counts 不能直接比较。

### AI协作边界
AI 可以把流程整理成表格；不能替代对数据来源、质量控制和样本对应关系的人工核验。

### 课后练习
给出一个 3 基因 x 4 样本矩阵，写出每列含义、每行含义和至少两个需要标准化的理由。

### 待核验
上游流程图中的每个软件和文件格式名称进入 PPT 前需核对。
