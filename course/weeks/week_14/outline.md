---
type: course-week
week: 14
title: 转录组数据分析基础
hours: 2
status: pilot_ready
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 14 周：转录组数据分析基础 · PPT 大纲

## 教学目标

- 说明 RNA-seq 的目标是测量基因表达水平。
- 描述从 FASTQ 到 count matrix 的基本流程。
- 区分 FASTQ、SAM/BAM、count matrix 和 metadata 的角色。
- 理解为什么原始 counts 不能直接跨样本比较。
- 能用 AI 辅助梳理流程，但知道哪些步骤需要人工核验。

## PPT 结构（试点版 12 页）

1. 标题页：转录组数据分析基础
2. 导入问题：表达矩阵是从哪里来的
3. RNA-seq 要回答什么问题
4. 从样本到 reads：测序数据不是表格
5. 核心流程总览：FASTQ 到 count matrix
6. 文件角色：FASTQ、SAM/BAM、count matrix、metadata
7. 质量控制与 trimming：为什么先看 reads 质量
8. Alignment 与 feature extraction：reads 如何变成基因计数
9. Count matrix 与 metadata：后续统计的输入
10. 标准化直觉：测序深度不同导致不可直接比较
11. 课堂练习：检查样本名、总 counts 和分组
12. 小结：理解数据链条，才谈得上差异表达

## 试点版 12 页页级大纲

| 页码 | 标题 | 核心图/表/代码意图 | 讲授重点 | 学生活动/核验 |
|---:|---|---|---|---|
| 1 | 转录组数据分析基础 | 标题与 Week 15 链路 | 本周解释 Week 15 结果表的上游来源 | 说出本周和差异表达的关系 |
| 2 | 表达矩阵从哪里来 | 文章中的表达矩阵截图意图 | 表达矩阵不是天然存在的表格 | 写出“reads 到矩阵”的疑问 |
| 3 | RNA-seq 回答什么问题 | 药物处理组 vs 对照组示意 | 目标是测量基因表达并比较条件差异 | 说出样本、分组、基因三要素 |
| 4 | 测序数据不是表格 | FASTQ 片段示意 | FASTQ 是 reads 和质量信息，不是统计表 | 区分原始数据与分析表 |
| 5 | FASTQ 到 count matrix | 流程图 | 先建立输入、处理、输出链条 | 在流程图圈出质量风险点 |
| 6 | 文件角色对照 | FASTQ/SAM/BAM/count matrix/metadata 表 | 每类文件解决不同问题 | 给每个文件写一句用途 |
| 7 | QC 与 trimming | 质量分布和低质量 reads 示意 | 低质量 reads 会影响后续比对和计数 | 写出两个可能质量问题 |
| 8 | Alignment 与 feature extraction | reads 到基因计数示意 | 比对结果经过计数才形成基因层面矩阵 | 说明 reads 和 gene count 的差别 |
| 9 | Count matrix 与 metadata | 3 基因 x 4 样本矩阵 + metadata | 样本名必须一一对应 | 检查 `Ctrl_1` 到 `Drug_2` 是否对齐 |
| 10 | 为什么不能直接比较原始 counts | 每列总 counts 表 | 测序深度差异会造成比较偏差 | 计算四个样本总 counts |
| 11 | AI 协作与课堂练习 | 四列表提示词 | AI 可整理流程，人工核验输入输出和质量问题 | 审计 AI 是否遗漏 metadata |
| 12 | 小结：理解数据链条 | Week 14 到 Week 15 过渡图 | 懂来源，才有资格解释差异表达 | 完成出口卡 |

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
## 本轮素材升级说明（2026-06-04）

- 教学定位：Week 14 的核心问题是“表达矩阵从哪里来”，课堂不要求跑通完整 RNA-seq、single-cell 或 spatial workflow。
- 新增支撑：AIDD RNA-seq 流程作为学生入口；SCBP raw processing / data structures、OSCA SingleCellExperiment/QC/normalization、OSTA reads-to-counts/QC 作为现代组学补充。
- 药学场景：用药物处理前后样本的 count matrix 和 metadata 说明分组、批次和总 counts 核验。
- PPT storyboard 入口：后续 storyboard 应加入一页“bulk、single-cell、spatial 都要先回答输入、QC、矩阵和 metadata”。
