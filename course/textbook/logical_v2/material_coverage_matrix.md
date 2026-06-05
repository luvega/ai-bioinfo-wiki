---
type: textbook-logical-coverage
title: 教材 v2 素材覆盖矩阵
status: source_mapped
version: 2
mode: logical
created: 2026-06-05
tags: [course, textbook, logical-v2, material-coverage, source-mapped]
---

# 教材 v2 素材覆盖矩阵

本矩阵用于反查所有主要素材池是否已进入 12 章逻辑教材规划。它只记录课程化使用位置，不改变任何原始素材、旧 18 周教材或周次状态。

## 按素材源反查

| 素材源 | v2 章节 | 使用方式 | 边界 |
|---|---|---|---|
| `course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md` | 1-12 | 课程事实边界、主题覆盖、学生任务和 AI 边界 | 不被外部素材覆盖 |
| `course/weeks/week_01` 到 `course/weeks/week_18` | 1-12 | 反向映射到课堂任务、teaching plan、storyboard 和学习证据 | 不按周次切章 |
| `course/textbook/chapters/chapter_01.md` 到 `chapter_18.md` | 1-12 | 旧 18 章扩写稿作为素材池 | 第一轮不替换现有 Coursebook |
| `knowledge/concepts/医药数据特征.md` | 1, 9 | 医药数据多源、高维、异质和强解释性 | 不外推为真实研究结论 |
| `knowledge/concepts/工具分工_Python_R_Bash.md` | 1, 3 | Python/R/Shell 工具边界 | 工具服务问题，不做命令清单 |
| `knowledge/concepts/AI协作边界.md` | 1, 2, 8, 12 | AI 可辅助、不可替代和可审计要求 | AI 不替代医学、统计和生物学判断 |
| `knowledge/concepts/项目目录结构与可复现.md` | 2, 4 | 项目目录、来源、处理日志和复现边界 | 不把形式化目录当作真正复现 |
| `knowledge/sources/AIDD_Bioinformatics_Course.md` | 1, 8, 10 | 生信工具分工、RNA-seq、GitHub 和可视化素材 | 只做课程案例，不替代主线 |
| `materials/markdown/aidd_bioinformatics/aidd.course_index.md` 及章节文件 | 1, 3, 4, 5, 8, 10, 11 | Python/R/Bash、文件格式、NGS、DESeq2、GitHub、图形表达 | 字幕素材需课程化改写 |
| `knowledge/sources/Python程序设计_以医药数据为例.md` | 3, 4, 5 | 中文医药数据 Python 案例 | 只取小数据和课堂节奏 |
| `knowledge/sources/Learn_AI_Assisted_Python_Programming.md` | 3 | AI 辅助编程教学法、读代码、测试和调试 | 不让 AI 代写不可核验代码 |
| `knowledge/sources/嵩天PythonPPT.md` | 3 | 中文 Python 入门节奏和基础概念讲法 | 需改写为医药数据场景 |
| `knowledge/sources/Starting_Data_Analytics_GenAI.md` | 2, 4, 5, 7 | 数据分析项目中的 LLM 协作、质量检查和解释风险 | 不替代字段来源和统计前提 |
| `knowledge/sources/OWF_Learn_Git.md` | 2 | Git、GitHub、版本记录和协作规范 | 服务项目复现，不变成 Git 专题课 |
| `knowledge/sources/OWF_Learn_Windows_Shell.md` | 2 | Windows shell 和脚本化故障排查 | 只讲课程项目所需最小命令 |
| `knowledge/sources/OWF_Learn_Linux_Shell.md` | 2 | Bash、日志和流程记录 | 只讲复现与组学案例需要的概念 |
| `knowledge/sources/ISLP.md` | 6, 7 | 统计推断、回归、分类、模型评价 | 取本科可解释层，不扩展高级 ML |
| `knowledge/sources/ISLR.md` | 6, 7 | R 版统计学习和 lab 风格 | 只支撑 R 解释和模型直觉 |
| `knowledge/entities/ggplot2.md` | 5, 8 | R 图层、图表规范和图注表达 | 不把美观当证据 |
| `knowledge/entities/DESeq2.md` | 6, 11 | DESeq2 字段、FDR 和结果解释 | 结果表不是基因功能结论表 |
| `knowledge/concepts/RNA-seq上游流程.md` | 10 | FASTQ、QC、alignment、count matrix 和 metadata | 不要求学生完整运行上游 pipeline |
| `knowledge/concepts/差异表达分析.md` | 6, 11 | 差异表达输入、输出、统计前提和边界 | 不编造基因功能 |
| `knowledge/concepts/富集分析_GO_KEGG.md` | 11 | ORA/GSEA、通路图和解释陷阱 | 富集结果只给候选解释 |
| `knowledge/sources/Single_Cell_Best_Practices.md` | 9, 10, 11, 12 | 单细胞数据结构、QC、降维、聚类、差异、GSEA、空间和多模态 | 只训练图形判读和边界 |
| `materials/markdown/sc_best_practices/scbp.course_index.md` | 9, 10, 11, 12 | SCBP notebook 索引和课程化取材入口 | notebook 输出不直接当结论 |
| `knowledge/sources/OSCA.md` | 9, 10, 11, 12 | Bioconductor 单细胞 workflow、SCE、QC、降维和多样本案例 | 教师备课素材优先 |
| `knowledge/sources/OSTA.md` | 9, 12 | 空间转录组坐标、空间域和空间图形解释 | 只作拓展图形判读 |
| `materials/markdown/bioconductor_books/README.md` | 9, 10, 11, 12 | OSCA/OSTA 页面、代码、图像和 workflow 索引 | 不引用 raw 目录 |
| `knowledge/sources/生物医药大数据与智能分析.md` | 1, 12 | 生物医药大数据和智能分析案例背景 | 只作课程案例池 |
| `course/evaluation/learning_outcome_matrix.md` | 8, 12 | 每章学习证据和 AI 边界检查 | 不替代周次评价 |
| `course/evaluation/student_project_rubric.md` | 2, 7, 12 | 综合项目最低交付包和评分标准 | 评价学生项目，不评价教师课件 |

## 按 v2 章节反查

| v2 章 | 核心来源周次 | 旧教材素材池 | 重点外部素材 | 学习证据 |
|---:|---|---|---|---|
| 1 | W01, W11 | chapter_01, chapter_11 | AIDD 总览、生物医药大数据、医药数据特征 | 问题-数据-方法-图表-边界五栏草表 |
| 2 | W02, W17, W18 | chapter_02, chapter_17, chapter_18 | OWF Git/Shell、AIDD GitHub、GenAI 数据分析 | README、data_sources、ai_use_statement |
| 3 | W03, W04, W17 | chapter_03, chapter_04, chapter_17 | AI-assisted Python、Python 医药案例、AIDD Python/R/Bash | 代码运行输出和手工核验 |
| 4 | W05, W06 | chapter_05, chapter_06 | GenAI 数据分析、AIDD 文件格式、Python 医药案例 | 数据字典、清洗日志、汇总规则 |
| 5 | W07, W11 | chapter_07, chapter_11 | ggplot2、Python/R 绘图素材 | 描述统计表和分布图图注 |
| 6 | W08, W15 | chapter_08, chapter_15 | ISLP/ISLR、DESeq2/FDR | 检验前提和解释边界表 |
| 7 | W09, W10 | chapter_09, chapter_10 | ISLP/ISLR、项目 rubric | 回归图注和阈值-性能-解释表 |
| 8 | W11, W18 | chapter_11, chapter_18 | ggplot2、AIDD 可视化、评价矩阵 | 图表证据边界表 |
| 9 | W12, W13, W16 | chapter_12, chapter_13, chapter_16 | SCBP、OSCA、OSTA | 高维图形四栏表 |
| 10 | W14, W15 | chapter_14, chapter_15 | AIDD RNA-seq、OSCA workflow、SCBP raw processing | count matrix 与 metadata 对齐表 |
| 11 | W15, W16 | chapter_15, chapter_16 | DESeq2、富集分析、SCBP conditions/GSEA | DE 字段解释和 overclaim 降级清单 |
| 12 | W16, W17, W18 | chapter_16, chapter_17, chapter_18 | SCBP、OSCA/OSTA、学生项目 rubric | 单细胞图形四栏表和综合项目包 |

## 覆盖风险

- AIDD 变异分析和 BLAST/系统发育素材不进入主章，只在第 1、3、8、10、12 章作为扩展示例或教师备课材料。
- SCBP 的 trajectory、RNA velocity、ATAC、AIR、多模态等内容不作为本科必学主线，只在第 12 章作为“前沿图形和证据边界”补充。
- OSCA/OSTA 的完整 workflow 不要求学生复现；进入正文时必须降级为数据结构、图形元素、参数敏感性或解释边界。
- 任何真实基因、通路、细胞类型、空间区域或临床意义都必须保留待核验语言，不能由 AI 直接写成结论。
