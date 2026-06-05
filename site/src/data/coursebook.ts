import { weeks } from './weeks';

export type CoursebookChapterStatus = 'coursebook_ready';

export type CoursebookChapter = {
  chapter: number;
  slug: string;
  title: string;
  part: string;
  coreQuestion: string;
  summary: string;
  status: CoursebookChapterStatus;
  page: string;
  chapterSource: string;
  chapterFocus: string;
  knowledgeGraph: string;
  knowledgeMapImage: string;
  processDiagrams: string[];
  sourceWeeks: string[];
  sourceChapters: string[];
  knowledgeSources: string[];
  materialSources: string[];
  assetSources: string[];
  learningEvidence: string[];
};

export const textbookChapterSource = (chapter: number) =>
  `course/textbook/logical_v2/chapters/chapter_${String(chapter).padStart(2, '0')}.md`;

export const textbookStoryboardSource = (week: number) =>
  `course/weeks/week_${String(week).padStart(2, '0')}/ppt_storyboard.md`;

export const textbookTeachingPlanSource = (week: number) =>
  `course/weeks/week_${String(week).padStart(2, '0')}/teaching_plan.md`;

export const textbookAssetSources = (week: number) => {
  const prefix = 'course/textbook/assets';
  const assetMap: Record<number, string[]> = {
    1: ['datasets/week01_glucose_contract.csv', 'code/week01_glucose_contract.py', 'diagrams/week01_evidence_chain.mmd'],
    2: ['datasets/week02_project_manifest.csv', 'code/week02_project_manifest.py', 'diagrams/week02_reproducible_workflow.mmd'],
    3: ['datasets/week03_glucose_values.csv', 'code/week03_glucose_filter.py', 'diagrams/week03_python_audit_loop.mmd'],
    4: ['datasets/week04_marker_table.csv', 'code/week04_marker_summary.R', 'diagrams/week04_r_dataframe_layers.mmd'],
    5: ['datasets/week05_raw_glucose_table.csv', 'code/week05_dictionary_check.py', 'diagrams/week05_table_reshape.mmd'],
    6: ['datasets/week06_cleaning_cases.csv', 'code/week06_cleaning_log.py', 'diagrams/week06_cleaning_decision.mmd'],
    7: ['datasets/week07_concentration_distribution.csv', 'code/week07_descriptive_stats.py', 'diagrams/week07_distribution_reading.mmd'],
    8: ['datasets/week08_inference_result.csv', 'code/week08_inference_language.py', 'diagrams/week08_inference_boundary.mmd'],
    9: ['datasets/week09_dose_response.csv', 'code/week09_regression_check.py', 'diagrams/week09_correlation_causation.mmd'],
    10: ['datasets/week10_risk_predictions.csv', 'code/week10_confusion_matrix.py', 'diagrams/week10_threshold_tradeoff.mmd'],
    11: ['datasets/week11_figure_claims.csv', 'code/week11_caption_audit.py', 'diagrams/week11_figure_evidence.mmd'],
    12: ['datasets/week12_expression_matrix.csv', 'code/week12_standardize_matrix.py', 'diagrams/week12_matrix_bridge.mmd'],
    13: ['datasets/week13_expression_matrix.csv', 'code/week13_high_dimensional_figures.py', 'diagrams/week13_high_dimensional_reading.mmd'],
    14: ['datasets/week14_count_matrix.csv', 'code/week14_count_matrix_qc.py', 'diagrams/week14_rnaseq_pipeline.mmd'],
    15: ['datasets/week15_deseq2_results.csv', 'code/week15_de_filter.py', 'diagrams/week15_de_interpretation.mmd'],
    16: ['datasets/week16_single_cell_figures.csv', 'code/week16_single_cell_audit.py', 'diagrams/week16_single_cell_spatial.mmd'],
    17: ['datasets/week17_project_package_check.csv', 'code/week17_project_package_audit.py', 'diagrams/week17_project_workflow.mmd'],
    18: ['datasets/week18_presentation_rubric.csv', 'code/week18_rubric_summary.py', 'diagrams/week18_course_closure.mmd']
  };
  return (assetMap[week] ?? []).map((path) => `${prefix}/${path}`);
};

export const weekToCoursebookChapter: Record<number, number> = {1: 1, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 5, 8: 6, 9: 7, 10: 7, 11: 8, 12: 9, 13: 9, 14: 10, 15: 11, 16: 12, 17: 12, 18: 12};

export const coursebookChapters: CoursebookChapter[] = [
  {
  chapter: 1,
  slug: 'chapter-01',
  title: '医药数据、问题意识与证据链',
  part: '全书导论',
  coreQuestion: '药学问题如何转成数据、方法、图表和结论边界？',
  summary: '建立医药问题、数据结构、方法选择、图表表达和结论边界之间的证据链。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-01',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_01.md',
  chapterFocus: '课程定位与证据链入口',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_01_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-01.svg',
  processDiagrams: ['course/textbook/logical_v2/flows/coursebook_12_chapter_chain.mmd'],
  sourceWeeks: ['course/weeks/week_01', 'course/weeks/week_11'],
  sourceChapters: ['course/textbook/chapters/chapter_01.md', 'course/textbook/chapters/chapter_11.md'],
  knowledgeSources: ['knowledge/concepts/医药数据特征.md', 'knowledge/concepts/工具分工_Python_R_Bash.md', 'knowledge/concepts/AI协作边界.md', 'knowledge/sources/生物医药大数据与智能分析.md', 'knowledge/sources/AIDD_Bioinformatics_Course.md'],
  materialSources: ['course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md', 'materials/markdown/aidd_bioinformatics/01_Introduction_To_Biological_Programming_(PY,_R_and_Linux)/chapter.course.md'],
  assetSources: ['course/textbook/assets/datasets/week01_glucose_contract.csv', 'course/textbook/assets/diagrams/week01_evidence_chain.mmd', 'course/textbook/assets/knowledge_graph/course_graph.mmd'],
  learningEvidence: ['问题-数据-方法-图表-边界五栏草表', 'AI 协作边界声明草稿']
},
  {
  chapter: 2,
  slug: 'chapter-02',
  title: '可复现项目与 AI 协作规范',
  part: '工作流与规范',
  coreQuestion: '一个分析为什么必须能追溯来源、代码、Prompt 和人工核验？',
  summary: '把证据链落实为可追溯的项目目录、来源记录、代码日志和 AI 使用声明。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-02',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_02.md',
  chapterFocus: '可复现规范与 AI 使用声明',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_02_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-02.svg',
  processDiagrams: ['course/textbook/logical_v2/flows/chapter_02_reproducible_project_flow.mmd'],
  sourceWeeks: ['course/weeks/week_02', 'course/weeks/week_17', 'course/weeks/week_18'],
  sourceChapters: ['course/textbook/chapters/chapter_02.md', 'course/textbook/chapters/chapter_17.md', 'course/textbook/chapters/chapter_18.md'],
  knowledgeSources: ['knowledge/concepts/项目目录结构与可复现.md', 'knowledge/concepts/AI协作边界.md', 'knowledge/entities/GitHub.md', 'knowledge/sources/OWF_Learn_Git.md', 'knowledge/sources/OWF_Learn_Windows_Shell.md', 'knowledge/sources/OWF_Learn_Linux_Shell.md', 'knowledge/sources/Starting_Data_Analytics_GenAI.md'],
  materialSources: ['materials/markdown/openwaterfoundation_learning/git/README.md', 'materials/markdown/openwaterfoundation_learning/windows_shell/README.md', 'materials/markdown/openwaterfoundation_learning/linux_shell/README.md', 'materials/markdown/aidd_bioinformatics/12_GitHub_Guide_for_Students/chapter.course.md', 'course/evaluation/student_project_rubric.md'],
  assetSources: ['course/textbook/assets/datasets/week02_project_manifest.csv', 'course/textbook/assets/code/week02_project_manifest.py', 'course/textbook/assets/diagrams/week02_reproducible_workflow.mmd'],
  learningEvidence: ['项目 README 草稿', 'data_sources 与 ai_use_statement 最小交付包']
},
  {
  chapter: 3,
  slug: 'chapter-03',
  title: '编程最小工具箱',
  part: '工具最小集',
  coreQuestion: '药学学生需要掌握哪些 Python、R、Shell 最小能力？',
  summary: '提炼 Python、R 和 Shell 的最小能力，使药学学生能读懂、运行并核验小型分析脚本。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-03',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_03.md',
  chapterFocus: 'Python/R/Shell 最小能力',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_03_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-03.svg',
  processDiagrams: [],
  sourceWeeks: ['course/weeks/week_03', 'course/weeks/week_04', 'course/weeks/week_17'],
  sourceChapters: ['course/textbook/chapters/chapter_03.md', 'course/textbook/chapters/chapter_04.md', 'course/textbook/chapters/chapter_17.md'],
  knowledgeSources: ['knowledge/entities/Python.md', 'knowledge/entities/R.md', 'knowledge/entities/Bash.md', 'knowledge/entities/Biopython.md', 'knowledge/sources/Learn_AI_Assisted_Python_Programming.md', 'knowledge/sources/Python程序设计_以医药数据为例.md', 'knowledge/sources/嵩天PythonPPT.md'],
  materialSources: ['materials/markdown/aidd_bioinformatics/02_Python_Language_for_Bioinformatics_(Biopython_for_Bioinformatics)/chapter.course.md', 'materials/markdown/aidd_bioinformatics/04_Bash_for_bioinformatics_(Linux_use_in_Bioinformatics)/chapter.course.md', 'materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md', 'materials/markdown/pdf_library_mineru/Pythonppt', 'materials/markdown/pdf_library_mineru/R240_Learn_AI_Assisted_Python_Programming_With_GitHub_Copilot_and_ChatGPT_2023_Leo_Porter_Daniel_Zingaro'],
  assetSources: ['course/textbook/assets/datasets/week03_glucose_values.csv', 'course/textbook/assets/code/week03_glucose_filter.py', 'course/textbook/assets/diagrams/week03_python_audit_loop.mmd', 'course/textbook/assets/datasets/week04_marker_table.csv', 'course/textbook/assets/code/week04_marker_summary.R'],
  learningEvidence: ['代码、运行输出和手工核验记录', 'R/Python 数据结构对照注释']
},
  {
  chapter: 4,
  slug: 'chapter-04',
  title: '表格数据读取、整理与质量控制',
  part: '数据质量',
  coreQuestion: '原始表怎样变成可分析表，哪些处理不能交给 AI 代判？',
  summary: '把读取、整理、数据字典、缺失异常处理和清洗日志合并为数据质量章。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-04',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_04.md',
  chapterFocus: '数据字典、清洗日志与人工判断',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_04_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-04.svg',
  processDiagrams: ['course/textbook/logical_v2/flows/chapter_04_data_quality_flow.mmd'],
  sourceWeeks: ['course/weeks/week_05', 'course/weeks/week_06'],
  sourceChapters: ['course/textbook/chapters/chapter_05.md', 'course/textbook/chapters/chapter_06.md'],
  knowledgeSources: ['knowledge/concepts/项目目录结构与可复现.md', 'knowledge/sources/Starting_Data_Analytics_GenAI.md', 'knowledge/sources/Python程序设计_以医药数据为例.md'],
  materialSources: ['materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210', 'materials/markdown/aidd_bioinformatics/02_Python_Language_for_Bioinformatics_(Biopython_for_Bioinformatics)/chapter.course.md', 'materials/markdown/aidd_bioinformatics/07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/chapter.course.md'],
  assetSources: ['course/textbook/assets/datasets/week05_raw_glucose_table.csv', 'course/textbook/assets/code/week05_dictionary_check.py', 'course/textbook/assets/diagrams/week05_table_reshape.mmd', 'course/textbook/assets/datasets/week06_cleaning_cases.csv', 'course/textbook/assets/code/week06_cleaning_log.py'],
  learningEvidence: ['数据字典和整理规则', '清洗日志、异常解释和分组汇总表']
},
  {
  chapter: 5,
  slug: 'chapter-05',
  title: '描述统计与分布可视化',
  part: '描述与表达',
  coreQuestion: '一组医药指标怎样被统计量和图形共同描述？',
  summary: '用统计量和分布图共同描述医药指标，避免只凭单个均值解释数据。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-05',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_05.md',
  chapterFocus: '描述统计与分布图形',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_05_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-05.svg',
  processDiagrams: [],
  sourceWeeks: ['course/weeks/week_07', 'course/weeks/week_11'],
  sourceChapters: ['course/textbook/chapters/chapter_07.md', 'course/textbook/chapters/chapter_11.md'],
  knowledgeSources: ['knowledge/entities/ggplot2.md', 'knowledge/sources/Python程序设计_以医药数据为例.md', 'knowledge/sources/Starting_Data_Analytics_GenAI.md'],
  materialSources: ['materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210', 'materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md'],
  assetSources: ['course/textbook/assets/datasets/week07_concentration_distribution.csv', 'course/textbook/assets/code/week07_descriptive_stats.py', 'course/textbook/assets/diagrams/week07_distribution_reading.mmd', 'course/textbook/assets/datasets/week11_figure_claims.csv'],
  learningEvidence: ['描述统计表', '直方图、箱线图或分布图图注']
},
  {
  chapter: 6,
  slug: 'chapter-06',
  title: '统计推断与结果解释边界',
  part: '统计判断',
  coreQuestion: 'P 值、置信区间、效应量和多重比较分别能说明什么？',
  summary: '解释 P 值、置信区间、效应量和多重比较的功能，使统计语言服务于证据边界。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-06',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_06.md',
  chapterFocus: '统计推断语言与解释边界',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_06_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-06.svg',
  processDiagrams: [],
  sourceWeeks: ['course/weeks/week_08', 'course/weeks/week_15'],
  sourceChapters: ['course/textbook/chapters/chapter_08.md', 'course/textbook/chapters/chapter_15.md'],
  knowledgeSources: ['knowledge/sources/ISLP.md', 'knowledge/sources/ISLR.md', 'knowledge/entities/DESeq2.md', 'knowledge/concepts/差异表达分析.md'],
  materialSources: ['materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R', 'materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md'],
  assetSources: ['course/textbook/assets/datasets/week08_inference_result.csv', 'course/textbook/assets/code/week08_inference_language.py', 'course/textbook/assets/diagrams/week08_inference_boundary.mmd', 'course/textbook/assets/datasets/week15_deseq2_results.csv'],
  learningEvidence: ['检验前提与解释边界表', 'P 值、CI、效应量和 FDR 的克制表述']
},
  {
  chapter: 7,
  slug: 'chapter-07',
  title: '相关、回归与分类预测',
  part: '模型与预测',
  coreQuestion: '相关、回归、预测概率和阈值如何服务药学判断？',
  summary: '把相关、线性回归、逻辑回归、预测概率和阈值转化为可解释的药学判断材料。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-07',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_07.md',
  chapterFocus: '关系建模与预测边界',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_07_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-07.svg',
  processDiagrams: [],
  sourceWeeks: ['course/weeks/week_09', 'course/weeks/week_10'],
  sourceChapters: ['course/textbook/chapters/chapter_09.md', 'course/textbook/chapters/chapter_10.md'],
  knowledgeSources: ['knowledge/sources/ISLP.md', 'knowledge/sources/ISLR.md', 'knowledge/sources/Starting_Data_Analytics_GenAI.md'],
  materialSources: ['materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R', 'course/evaluation/student_project_rubric.md'],
  assetSources: ['course/textbook/assets/datasets/week09_dose_response.csv', 'course/textbook/assets/code/week09_regression_check.py', 'course/textbook/assets/diagrams/week09_correlation_causation.mmd', 'course/textbook/assets/datasets/week10_risk_predictions.csv', 'course/textbook/assets/code/week10_confusion_matrix.py'],
  learningEvidence: ['相关与回归图注', '阈值-性能-解释表']
},
  {
  chapter: 8,
  slug: 'chapter-08',
  title: '科研图表与 SCI 表达',
  part: '图表与写作',
  coreQuestion: '图表如何支撑结论，如何避免漂亮但无证据？',
  summary: '训练科研图表的证据表达能力，使图形、统计标注、图注和结论保持一致。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-08',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_08.md',
  chapterFocus: '图表证据边界与图注表达',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_08_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-08.svg',
  processDiagrams: [],
  sourceWeeks: ['course/weeks/week_11', 'course/weeks/week_18'],
  sourceChapters: ['course/textbook/chapters/chapter_11.md', 'course/textbook/chapters/chapter_18.md'],
  knowledgeSources: ['knowledge/entities/ggplot2.md', 'knowledge/concepts/AI协作边界.md', 'knowledge/sources/AIDD_Bioinformatics_Course.md'],
  materialSources: ['materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md', 'materials/markdown/aidd_bioinformatics/08_Variant_Calling_on_Bash/chapter.course.md', 'course/evaluation/learning_outcome_matrix.md', 'course/evaluation/courseware_rubric.md'],
  assetSources: ['course/textbook/assets/datasets/week11_figure_claims.csv', 'course/textbook/assets/code/week11_caption_audit.py', 'course/textbook/assets/diagrams/week11_figure_evidence.mmd', 'course/textbook/assets/datasets/week18_presentation_rubric.csv'],
  learningEvidence: ['图表证据边界表', '修改后的图注和 AI 审计记录']
},
  {
  chapter: 9,
  slug: 'chapter-09',
  title: '高维矩阵、降维、聚类与热图',
  part: '高维数据',
  coreQuestion: '表达矩阵、PCA、聚类、热图和 UMAP 能看出什么，不能证明什么？',
  summary: '用矩阵、PCA、聚类、热图和 UMAP 建立高维图形的观察路径和解释限制。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-09',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_09.md',
  chapterFocus: '高维图形输入、观察和边界',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_09_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-09.svg',
  processDiagrams: [],
  sourceWeeks: ['course/weeks/week_12', 'course/weeks/week_13', 'course/weeks/week_16'],
  sourceChapters: ['course/textbook/chapters/chapter_12.md', 'course/textbook/chapters/chapter_13.md', 'course/textbook/chapters/chapter_16.md'],
  knowledgeSources: ['knowledge/sources/Single_Cell_Best_Practices.md', 'knowledge/sources/OSCA.md', 'knowledge/sources/OSTA.md', 'knowledge/concepts/医药数据特征.md'],
  materialSources: ['materials/markdown/sc_best_practices/scbp.course_index.md', 'materials/markdown/bioconductor_books/README.md'],
  assetSources: ['course/textbook/assets/datasets/week12_expression_matrix.csv', 'course/textbook/assets/code/week12_standardize_matrix.py', 'course/textbook/assets/diagrams/week12_matrix_bridge.mmd', 'course/textbook/assets/datasets/week13_expression_matrix.csv', 'course/textbook/assets/diagrams/week13_high_dimensional_reading.mmd'],
  learningEvidence: ['矩阵结构说明和标准化解释', '高维图形输入-观察-解释-待核验四栏表']
},
  {
  chapter: 10,
  slug: 'chapter-10',
  title: '转录组流程与表达矩阵',
  part: '组学流程',
  coreQuestion: 'FASTQ 如何走到 count matrix，metadata 为什么是底线？',
  summary: '说明 RNA-seq 从 FASTQ 到 count matrix 的基本链条，并强调 metadata 对齐是下游分析底线。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-10',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_10.md',
  chapterFocus: 'RNA-seq 上游流程与 metadata 对齐',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_10_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-10.svg',
  processDiagrams: ['course/textbook/logical_v2/flows/chapter_10_rnaseq_count_matrix_flow.mmd'],
  sourceWeeks: ['course/weeks/week_14', 'course/weeks/week_15'],
  sourceChapters: ['course/textbook/chapters/chapter_14.md', 'course/textbook/chapters/chapter_15.md'],
  knowledgeSources: ['knowledge/concepts/RNA-seq上游流程.md', 'knowledge/entities/samtools.md', 'knowledge/sources/AIDD_Bioinformatics_Course.md', 'knowledge/sources/OSCA.md', 'knowledge/sources/Single_Cell_Best_Practices.md'],
  materialSources: ['materials/markdown/aidd_bioinformatics/07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/chapter.course.md', 'materials/markdown/aidd_bioinformatics/06_Understanding_Bioinformatics_Pipeline/chapter.course.md', 'materials/markdown/sc_best_practices/scbp.course_index.md', 'materials/markdown/bioconductor_books/README.md'],
  assetSources: ['course/textbook/assets/datasets/week14_count_matrix.csv', 'course/textbook/assets/code/week14_count_matrix_qc.py', 'course/textbook/assets/diagrams/week14_rnaseq_pipeline.mmd'],
  learningEvidence: ['FASTQ 到 count matrix 流程链条图', 'count matrix 与 metadata 对齐核验表']
},
  {
  chapter: 11,
  slug: 'chapter-11',
  title: '差异表达、富集分析与功能解释',
  part: '组学解释',
  coreQuestion: 'DE 结果表如何进入图表和候选解释，哪里必须停止？',
  summary: '把 DESeq2 结果、火山图、富集分析和功能解释组织成候选证据链。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-11',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_11.md',
  chapterFocus: 'DE 结果字段、火山图和功能解释降级',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_11_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-11.svg',
  processDiagrams: ['course/textbook/logical_v2/flows/chapter_11_de_interpretation_flow.mmd'],
  sourceWeeks: ['course/weeks/week_15', 'course/weeks/week_16'],
  sourceChapters: ['course/textbook/chapters/chapter_15.md', 'course/textbook/chapters/chapter_16.md'],
  knowledgeSources: ['knowledge/entities/DESeq2.md', 'knowledge/concepts/差异表达分析.md', 'knowledge/concepts/富集分析_GO_KEGG.md', 'knowledge/sources/Single_Cell_Best_Practices.md', 'knowledge/sources/OSCA.md'],
  materialSources: ['materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md', 'materials/markdown/sc_best_practices/scbp.course_index.md', 'materials/markdown/bioconductor_books/README.md'],
  assetSources: ['course/textbook/assets/datasets/week15_deseq2_results.csv', 'course/textbook/assets/code/week15_de_filter.py', 'course/textbook/assets/diagrams/week15_de_interpretation.mmd', 'course/textbook/assets/datasets/week16_single_cell_figures.csv'],
  learningEvidence: ['DE 结果字段解释和火山图图注', '候选基因功能解释降级清单']
},
  {
  chapter: 12,
  slug: 'chapter-12',
  title: '单细胞、空间组学与综合项目',
  part: '前沿与项目',
  coreQuestion: '单细胞/空间图形如何解读，并怎样转成学生项目交付？',
  summary: '用单细胞和空间组学图形训练本科层面的判读边界，并收束为综合项目交付。',
  status: 'coursebook_ready',
  page: '/coursebook/chapter-12',
  chapterSource: 'course/textbook/logical_v2/chapters/chapter_12.md',
  chapterFocus: '单细胞/空间图形判读与项目交付',
  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_12_knowledge_graph.mmd',
  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-12.svg',
  processDiagrams: ['course/textbook/logical_v2/flows/chapter_12_project_delivery_flow.mmd'],
  sourceWeeks: ['course/weeks/week_16', 'course/weeks/week_17', 'course/weeks/week_18'],
  sourceChapters: ['course/textbook/chapters/chapter_16.md', 'course/textbook/chapters/chapter_17.md', 'course/textbook/chapters/chapter_18.md'],
  knowledgeSources: ['knowledge/sources/Single_Cell_Best_Practices.md', 'knowledge/sources/OSCA.md', 'knowledge/sources/OSTA.md', 'knowledge/sources/生物医药大数据与智能分析.md', 'knowledge/concepts/AI协作边界.md'],
  materialSources: ['materials/markdown/sc_best_practices/scbp.course_index.md', 'materials/markdown/bioconductor_books/README.md', 'course/evaluation/student_project_rubric.md', 'course/templates/ai_use_statement_template.md', 'course/templates/project_readme_template.md', 'course/templates/data_sources_template.md'],
  assetSources: ['course/textbook/assets/datasets/week16_single_cell_figures.csv', 'course/textbook/assets/code/week16_single_cell_audit.py', 'course/textbook/assets/diagrams/week16_single_cell_spatial.mmd', 'course/textbook/assets/datasets/week17_project_package_check.csv', 'course/textbook/assets/datasets/week18_presentation_rubric.csv'],
  learningEvidence: ['单细胞/空间图形四栏解读表', 'README、data_sources、ai_use_statement 和 6-8 页项目 storyboard']
}
];

export const textbookChapters = coursebookChapters;
export const logicalV2Chapters = coursebookChapters;
export const logicalV2ReviewChapters = coursebookChapters;
export const sampleChapters: CoursebookChapter[] = [];

export type CoursewareWeek = {
  week: number;
  slug: string;
  title: string;
  page: string;
  coursebookPage: string;
  phase: string;
  summary: string;
  reviewStatus: string;
  pptStatus: string;
  teachingPlanStatus: string;
  teachingPlanSource: string;
  storyboardSource: string;
  storyboardPages: number;
  sourceWeekFiles: string[];
  assetSources: string[];
  badges?: string[];
};

const pilotReadyWeeks = new Set([3, 13, 14, 15, 16]);

export const coursewareWeeks: CoursewareWeek[] = weeks.map((week) => {
  const chapter = getCoursebookChapterByWeek(week.week);
  return {
    week: week.week,
    slug: week.slug,
    title: week.title,
    page: `/courseware/${week.slug}`,
    coursebookPage: chapter?.page ?? '/coursebook',
    phase: week.phase,
    summary: week.question,
    reviewStatus: pilotReadyWeeks.has(week.week) ? 'pilot_ready' : 'pilot_candidate',
    pptStatus: 'storyboard_expanded',
    teachingPlanStatus: 'teaching_plan_ready',
    teachingPlanSource: textbookTeachingPlanSource(week.week),
    storyboardSource: textbookStoryboardSource(week.week),
    storyboardPages: 40,
    sourceWeekFiles: [
      `course/weeks/week_${String(week.week).padStart(2, '0')}/materials.md`,
      `course/weeks/week_${String(week.week).padStart(2, '0')}/outline.md`,
      `course/weeks/week_${String(week.week).padStart(2, '0')}/script.md`,
      textbookTeachingPlanSource(week.week),
      textbookStoryboardSource(week.week)
    ],
    assetSources: textbookAssetSources(week.week),
    badges: ['40 页主干 storyboard']
  };
});

export function getCoursebookChapterBySlug(slug: string) {
  return coursebookChapters.find((chapter) => chapter.slug === slug);
}

export function getCoursebookChapterByWeek(week: number) {
  const chapterNo = weekToCoursebookChapter[week];
  return coursebookChapters.find((chapter) => chapter.chapter === chapterNo);
}

export function getLogicalV2ChapterBySlug(slug: string) {
  return getCoursebookChapterBySlug(slug);
}

export function getCoursewareWeekBySlug(slug: string) {
  return coursewareWeeks.find((week) => week.slug === slug);
}

export function getCoursewareWeekByWeek(week: number) {
  return coursewareWeeks.find((coursewareWeek) => coursewareWeek.week === week);
}
