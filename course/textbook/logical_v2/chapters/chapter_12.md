---
type: textbook-logical-v2-chapter
title: 第 12 章 单细胞、空间组学与综合项目
chapter: 12
status: review_ready
review_status: review_ready
version: 2
created: 2026-06-05
core_question: 单细胞/空间图形如何解读，并怎样转成学生项目交付？
source_weeks:
  - course/weeks/week_16
  - course/weeks/week_17
  - course/weeks/week_18
source_chapters:
  - course/textbook/chapters/chapter_16.md
  - course/textbook/chapters/chapter_17.md
  - course/textbook/chapters/chapter_18.md
knowledge_sources:
  - knowledge/sources/Single_Cell_Best_Practices.md
  - knowledge/sources/OSCA.md
  - knowledge/sources/OSTA.md
  - knowledge/sources/生物医药大数据与智能分析.md
  - knowledge/concepts/AI协作边界.md
material_sources:
  - materials/markdown/sc_best_practices/scbp.course_index.md
  - materials/markdown/bioconductor_books/README.md
  - course/evaluation/student_project_rubric.md
  - course/templates/ai_use_statement_template.md
  - course/templates/project_readme_template.md
  - course/templates/data_sources_template.md
asset_sources:
  - course/textbook/assets/datasets/week16_single_cell_figures.csv
  - course/textbook/assets/code/week16_single_cell_audit.py
  - course/textbook/assets/diagrams/week16_single_cell_spatial.mmd
  - course/textbook/assets/datasets/week17_project_package_check.csv
  - course/textbook/assets/datasets/week18_presentation_rubric.csv
learning_evidence:
  - 单细胞/空间图形四栏解读表
  - README、data_sources、ai_use_statement 和 6-8 页项目 storyboard
tags: [course, textbook, logical-v2, review-ready, single-cell-spatial-project]
---

# 第 12 章 单细胞、空间组学与综合项目

## 导入问题

单细胞和空间组学图形很容易让学生兴奋，也很容易让学生误读。UMAP 上的点云、cluster 标签、marker gene 热图、空间 spot 和组织区域都具有强烈视觉吸引力。第 12 章的问题是：单细胞/空间图形如何解读，并怎样转成学生项目交付？

本章是 v2 第一轮审查样章的收束章。它不要求药学本科生完整复现 SCBP、OSCA 或 OSTA workflow，也不要求学生掌握所有单细胞算法。它要求学生能识别图形输入、观测单位、视觉编码、参数敏感性和结论边界，并把这些理解转成综合项目交付包：README、data_sources、ai_use_statement、图表证据边界和 6-8 页项目 storyboard。

## 本章知识链

第一步是区分观测单位。bulk RNA-seq 的一列通常是样本，单细胞矩阵的一行或一列可能代表细胞，空间组学还引入 spot、坐标和组织区域。观测单位变化后，图形解释也会变化。学生不能把 bulk 差异表达的读法直接套到单细胞 cluster 或空间 domain 上。

第二步是理解常见图形。QC 图用于发现低质量细胞、空液滴或测序质量问题；UMAP 或 t-SNE 用于观察细胞状态结构；cluster 图显示算法分群；marker gene 图提供候选注释线索；空间图显示表达或类别在组织坐标中的分布。每张图都必须说明点、颜色、坐标、标签和参数。

第三步是参数敏感性。过滤阈值、标准化、PCA 维度、邻居数、resolution、marker 筛选和空间平滑都会影响图形。学生不需要调完所有参数，但必须知道图形不是客观照片，而是数据和算法共同生成的视图。参数不记录，图形解释就不完整。

第四步是边界表达。UMAP 上两个簇分开，不等于真实生物距离很远；marker 高表达，不等于细胞类型已经确认；空间区域不同，不等于病理机制已经证明。图形只能提供候选观察，后续需要数据库、文献、实验设计、样本信息和专家判断。

第五步是项目交付。综合项目不是把所有章节内容堆在一起，而是把一个小问题沿着证据链走完：数据来源、质量检查、图表表达、AI 使用、人工核验和结论边界。第 12 章把现代组学图形作为高级案例，把第 2 章的可复现规范作为交付底座。

## 核心概念

**cell x gene matrix** 是单细胞数据结构的入口。它比 bulk 表达矩阵更细，但也更稀疏、更依赖 QC 和参数。学生需要理解每个细胞是观测单位，而不是把所有点当作独立患者。

**UMAP/t-SNE** 是可视化方法，用于展示局部结构和状态相似性。它不保证全局距离可直接解释，也不自动给出细胞类型。教材要求学生写“图上观察”而不是“机制事实”。

**marker gene** 是候选注释证据。marker 表达可以支持某种细胞类型猜测，但需要组合多个 marker、数据库、文献和上下文。AI 可以列出候选 marker 的常见解释，但不能直接确认注释。

**spatial domain** 是空间组学中的候选空间结构。它可能与组织区域、细胞状态或技术因素有关。没有组织学、样本来源和分析参数支持时，不能写成确定病理区域。

**综合项目包** 是课程收尾交付。它不以复杂度取胜，而以可审查取胜。学生需要用有限图表讲清楚一个问题，并明确哪些内容是已核验观察，哪些是候选解释。

## 最小工具与流程

本章使用 `week16_single_cell_figures.csv` 和 `week16_single_cell_audit.py` 训练图形审计。数据表记录图形类型、视觉元素、可能观察、过度解释风险和待核验点。脚本可以检查是否遗漏图形输入、参数或边界，但不能判断真实细胞类型。

最小图形解读流程是四栏表：图上看到什么，可能解释是什么，不确定性在哪里，下一步核验什么。对于 UMAP，学生可以写“某些点形成相对分离区域”，可能解释为“候选细胞状态或批次结构”，不确定性包括“过滤阈值、PCA 维度、resolution、样本来源”，下一步核验包括“marker 组合、metadata、文献或公开数据库”。这个读法比直接命名细胞类型更适合本科层。

综合项目流程则回到第 2 章。学生选一个小问题，准备 README、data_sources、ai_use_statement 和 6-8 页 storyboard。storyboard 不要求生成正式 PPTX，但必须包含问题、数据、方法、图表、边界、AI 审计和待核验点。第 12 章的目标是让学生把现代组学图形看懂到能审查，而不是看到图就写强结论。

## 案例与素材来源

本章主要来自 Week 16、Week 17 和 Week 18。SCBP、OSCA 和 OSTA 是重要教师备课来源，帮助教材覆盖单细胞和空间组学的现代数据结构、QC、降维、聚类、注释、空间坐标和多模态趋势。但这些素材进入本科正文时必须降级：只训练图形判读、参数意识和证据边界，不要求完整 workflow。

《生物医药大数据与智能分析》提供大数据和智能分析背景，用于解释为什么现代医药数据越来越多尺度、图形越来越复杂。学生项目 rubric 和模板则把前沿图形拉回课程交付：无论图形多前沿，都必须说明数据来源、AI 使用、人工核验和结论边界。

## AI 协作与核验

AI 可以帮助学生整理单细胞流程、解释图形元素、列出参数敏感点、生成四栏解读表框架、润色项目 storyboard。合格提示词应写明：“请只解释图形元素和可能风险，不要直接给最终细胞类型或疾病机制结论。”

AI 不能替代细胞类型注释、空间区域判断、marker 证据核验或项目评分。它尤其容易根据常见 marker 名称编造看似合理的细胞功能，也容易把空间模式写成病理机制。学生必须把 AI 输出拆成“可作为候选”“需要来源核验”“应删除”三类。任何涉及真实细胞类型、疾病机制、药效解释的句子都要保留待核验。

## 学习证据

本章的学习证据有两类。第一类是单细胞/空间图形四栏解读表。每张图至少填写图上观察、可能解释、不确定性和待核验点。第二类是综合项目包，包括 README、data_sources、ai_use_statement 和 6-8 页项目 storyboard。项目 storyboard 至少包含一个图表证据边界页和一个 AI 审计页。

评价时教师不要求学生给出真实细胞注释或空间机制，而要求学生证明自己知道何时停止。一个优秀项目会把 UMAP、marker、空间图和项目结论都写成层级化证据：哪些是图上可观察，哪些是候选解释，哪些需要文献或数据库核验，哪些超出课程范围。

## 教材写作口径

第 12 章是 v2 第一轮最能暴露教材边界的章节。它必须让读者看到：本教材承认现代组学重要，但不会把本科课程升级成完整生信 workflow。SCBP、OSCA 和 OSTA 可以提供结构、术语和图形来源，却不能把学生任务变成复现 notebook。正文要反复把任务降级为“看懂结构、图形、参数和证据边界”。

教材应把单细胞和空间组学写成综合项目中的高级图形素材，而不是单独的技术终点。学生项目可以选择一张 UMAP、一张 marker 图或一张空间示意图作为练习对象，但必须说明它是教学模拟、课程化改写或公开素材，并写清输入、图形元素、参数、候选解释和待核验点。这样才能把前沿素材纳入可审查项目。

本章还要把第 2 章的可复现规范重新带回来。单细胞图形越复杂，越需要 README、data_sources、ai_use_statement 和 storyboard。没有这些文件，学生很容易只展示一张炫目的图，却说不清图从哪里来、颜色代表什么、AI 改了哪些句子、哪些结论还没有来源支持。综合项目包是抵抗这种误读的工具。

写作时要避免两种极端。第一种极端是过度简化，把单细胞图只说成“点越近越相似”，这会误导学生。第二种极端是过度展开，把 QC、标准化、邻域图、聚类、轨迹、速度、空间域、多模态全部写成必学流程。正确做法是选择少数图形，围绕观测单位、视觉编码、参数敏感性和结论边界展开。

## 审查重点

审查第 12 章时，首先看它是否明确“不要求完整复现高级 workflow”。若正文要求学生跑完整 SCBP、OSCA 或 OSTA 分析，已经超出计划假设。合格正文应让学生能读懂图形和审查证据，而不是复制专业分析流程。

第二，看细胞类型和空间区域语言是否降级。任何“这个 cluster 是某细胞类型”“这个 spatial domain 代表某病理区域”的句子，都必须有候选、需要核验或来源支持。AI 生成的 marker 解释尤其要小心，不能因为常识上看似合理就进入教材结论。

第三，看综合项目交付是否足够具体。README、data_sources、ai_use_statement 和 6-8 页 storyboard 必须作为学习证据，而不是可选建议。项目 storyboard 应至少包含问题页、数据来源页、图表页、证据边界页、AI 审计页和待核验页。这样上线审查时才能判断 v2 是否真的把前沿内容转成了学生可交付任务。

第四，看第 12 章是否完成全书收束。它应回扣第 1 章的证据链、第 2 章的可复现规范、第 4 章的数据质量、第 8 章的图表边界和第 11 章的候选解释降级。如果这些连接清楚，v2 的逻辑结构就成立；如果第 12 章只是单细胞专题，说明全书结构仍需调整。

## 上线审查提示

线上审查第 12 章时，建议把它当作全书闭环测试。审查者应能在同一页看到前沿图形、证据边界和项目交付三件事。如果页面只像单细胞简介，说明综合项目没有收束；如果页面只像项目 rubric，说明现代组学素材没有被充分课程化。

审查者可以用一张 UMAP 或空间示意图测试章节：学生能否说明点或 spot 代表什么，颜色代表什么，参数可能如何影响图形，哪些解释需要 marker、metadata、数据库或文献核验。若章节能支持这四个问题，说明它达到了本科判读层目标。

项目交付也需要线上检查。页面应让学生清楚看到 README、data_sources、ai_use_statement 和 6-8 页 storyboard 是必需证据，而不是扩展作业。若这些交付项只在段落中一带而过，建议后续在站点页面增加“项目包检查卡”。

最后，本章要接受边界压力测试。审查者可以寻找任何强结论词，如“证明”“确认”“导致”“靶点”“机制成立”。除非有明确来源和核验状态，这些词都应降级。第 12 章如果能把最前沿、最容易误读的图形写得克制，v2 教材的风格就基本成立。

本章上线后还应检查项目交付是否真正闭环。审查者可以要求学生从图形解读表进入 storyboard，再从 storyboard 回到 README 和 AI 使用声明。如果这几个文件之间互相断开，说明学生只是完成了多个任务；如果它们能共同说明同一个问题、同一组数据和同一条证据边界，说明综合项目训练已经形成闭环。

教师还可以检查学生是否能识别“图形参数也是证据的一部分”。过滤阈值、PCA 维度、邻居数和 resolution 不只是软件设置，它们会影响图形形态和解释。若学生项目只展示最终 UMAP 或空间图，却没有记录这些参数，结论就缺少复现基础。第 12 章应让学生把参数记录写入项目包，而不是只放在代码里。

最后，页面上线后应检查移动端长列表是否可读。第 12 章来源多、术语多、交付项多，如果移动端无法清楚区分图形解读、AI 边界和项目包，就会影响人工审查。第一轮不必做复杂交互，但要确保基本排版稳定。

## 18 周反向映射

本章整合 Week 16“单细胞转录组可视化”、Week 17“综合项目工作坊”和 Week 18“综合项目汇报与课程总结”。旧教材 `chapter_16.md` 支持现代组学图形判读，`chapter_17.md` 和 `chapter_18.md` 支持项目交付与汇报验收。v2 第 12 章把前沿图形和项目规范放在一起，作为全书收束。

## 待核验点

- SCBP、OSCA 和 OSTA 图形若进入正式教材，需要核对来源、授权和图形参数。
- 单细胞和空间组学术语应保持本科可理解，不扩展为完整 workflow 教程。
- 所有细胞类型、marker、空间区域和机制句都必须保留候选或待核验语言。
- 综合项目页面上线前应检查来源列表、AI 使用声明和图表边界是否完整。
