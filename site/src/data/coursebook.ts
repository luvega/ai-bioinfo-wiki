export type CoursebookStatus = '目录占位' | '样章可读';

export type CoursebookSample = {
  introQuestion: string;
  learningObjectives: string[];
  coreConcepts: Array<{
    term: string;
    explanation: string;
  }>;
  classroomCase: {
    title: string;
    description: string;
    steps: string[];
  };
  aiBoundary: {
    allowed: string[];
    forbidden: string[];
  };
  verificationPoints: string[];
  pptBridge: {
    status: string;
    entry: string;
    nextActions: string[];
  };
};

export type CoursebookChapter = {
  chapter: number;
  week: number;
  slug: string;
  title: string;
  page: string;
  phase: string;
  summary: string;
  status: CoursebookStatus;
  reviewStatus: string;
  pptStatus: string;
  sourceWeekFiles: string[];
  knowledgeSources: string[];
  materialSources: string[];
  coursebookTopics: string[];
  sample?: CoursebookSample;
};

const baseWeekFiles = (week: number) => [
  `course/weeks/week_${String(week).padStart(2, '0')}/materials.md`,
  `course/weeks/week_${String(week).padStart(2, '0')}/outline.md`,
  `course/weeks/week_${String(week).padStart(2, '0')}/script.md`
];

export const coursebookChapters: CoursebookChapter[] = [
  {
    chapter: 1,
    week: 1,
    slug: 'week-01',
    title: '课程导论与医药数据特征',
    page: '/coursebook#week-01',
    phase: 'AI 边界、流程与复现',
    summary: '建立医药问题、数据结构、工具分工和 AI 协作边界的课程地图。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(1),
    knowledgeSources: ['knowledge/concepts/医药数据特征.md', 'knowledge/concepts/工具分工_Python_R_Bash.md', 'knowledge/concepts/AI协作边界.md'],
    materialSources: ['course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md'],
    coursebookTopics: ['医药数据类型', '工具分工', 'AI 协作边界']
  },
  {
    chapter: 2,
    week: 2,
    slug: 'week-02',
    title: '数据分析流程、复现规范与人机协作规范',
    page: '/coursebook#week-02',
    phase: 'AI 边界、流程与复现',
    summary: '把课程项目拆成原始数据、处理脚本、结果、报告和 AI 协作记录。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(2),
    knowledgeSources: ['knowledge/concepts/项目目录结构与可复现.md', 'knowledge/concepts/AI协作边界.md', 'knowledge/entities/GitHub.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/06_Understanding_Bioinformatics_Pipeline/chapter.course.md'],
    coursebookTopics: ['可复现分析', 'Prompt 记录', '项目目录']
  },
  {
    chapter: 3,
    week: 3,
    slug: 'week-03',
    title: 'AI 辅助编程与 Python 快速入门',
    page: '/coursebook/week-03',
    phase: '编程、清洗、统计与图表',
    summary: '用最小 Python 语法处理可手算核验的医药指标列表，并训练 AI 解释、调试和测试边界。',
    status: '样章可读',
    reviewStatus: 'sample_ready',
    pptStatus: 'pptx_trial_done',
    sourceWeekFiles: baseWeekFiles(3),
    knowledgeSources: ['knowledge/entities/Python.md', 'knowledge/entities/Biopython.md', 'knowledge/sources/Learn_AI_Assisted_Python_Programming.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/aidd.course_index.md', 'materials/markdown/pdf_library_mineru/Pythonppt', 'materials/markdown/pdf_library_mineru/R240_Learn_AI_Assisted_Python_Programming_With_GitHub_Copilot_and_ChatGPT_2023_Leo_Porter_Daniel_Zingaro'],
    coursebookTopics: ['Python 快速入门', '缺失值小案例', 'AI 辅助调试'],
    sample: {
      introQuestion: '怎样把“忽略缺失值、计算均值、标记高风险值”转成一段学生能读懂、能手算核验的 Python 代码？',
      learningObjectives: [
        '识别变量、列表、字典、条件和循环在医药数据处理中的作用。',
        '能用 3 到 5 个小样本手算核验代码输出。',
        '能要求 AI 解释代码、定位报错、生成测试用例，而不是直接替代判断。'
      ],
      coreConcepts: [
        { term: '列表', explanation: '保存一组指标值，例如血糖、药物浓度或表达量。' },
        { term: '缺失值', explanation: '`None` 代表本例中没有可用数值，计算均值前必须先明确处理规则。' },
        { term: '阈值判断', explanation: '把医学或课堂规则写成可重复检查的条件表达式。' },
        { term: '测试样本', explanation: '用极小数据暴露代码是否遗漏缺失、边界值或空列表。' }
      ],
      classroomCase: {
        title: '血糖列表中的缺失值和高风险值',
        description: '`glucose = [5.2, 6.1, 4.9, None, 12.8, 5.7]` 是本章贯穿例子。课堂先让学生手工圈出 `None` 和 `12.8`，再阅读代码。',
        steps: [
          '过滤 `None`，保留有效数值。',
          '计算有效值均值，并与手算结果 `6.94` 对照。',
          '标记大于 `7.0` 的高风险值。',
          '写一条 AI 提示词，要求 AI 只解释代码和缺失值处理，不直接扩写完整项目。'
        ]
      },
      aiBoundary: {
        allowed: ['解释 10 行以内代码', '根据报错定位原因', '生成边界测试样本', '提示可能遗漏的输入输出规则'],
        forbidden: ['替代学生判断医学阈值', '生成无法解释的大段代码', '跳过手算核验', '把 AI 输出当最终结果']
      },
      verificationPoints: ['课堂代码必须能本机运行。', '均值和高风险值必须能手算复核。', 'AI 输出必须明确提到 `None` 缺失值。'],
      pptBridge: {
        status: 'Week 03 已有 PPTX 试点样稿和 PNG 视觉验证记录。',
        entry: 'scripts/courseware/build_week03_pilot_ppt.py',
        nextActions: ['复查代码示例和课件文字溢出。', '保留 speaker notes 或迁入 PPT 原生备注。', '进入正式模板前再次检查截图授权。']
      }
    }
  },
  {
    chapter: 4,
    week: 4,
    slug: 'week-04',
    title: 'R 基础语法、数据框操作与 AI 代码核验',
    page: '/coursebook#week-04',
    phase: '编程、清洗、统计与图表',
    summary: '把 Python 数据结构直觉迁移到 R 的向量、数据框、因子和 ggplot2 图层。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(4),
    knowledgeSources: ['knowledge/entities/R.md', 'knowledge/entities/ggplot2.md', 'knowledge/concepts/工具分工_Python_R_Bash.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R'],
    coursebookTopics: ['R 数据框', '因子变量', 'R 代码核验']
  },
  {
    chapter: 5,
    week: 5,
    slug: 'week-05',
    title: '数据读取与整形',
    page: '/coursebook#week-05',
    phase: '编程、清洗、统计与图表',
    summary: '从 CSV、Excel、TSV 和字段说明进入可分析表，强调长宽表和数据字典。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(5),
    knowledgeSources: ['knowledge/concepts/项目目录结构与可复现.md', 'knowledge/sources/Starting_Data_Analytics_GenAI.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/aidd.course_index.md', 'materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210'],
    coursebookTopics: ['数据读取', '数据整形', '字段含义']
  },
  {
    chapter: 6,
    week: 6,
    slug: 'week-06',
    title: '缺失值、异常值处理与分组汇总',
    page: '/coursebook#week-06',
    phase: '编程、清洗、统计与图表',
    summary: '把缺失、异常和重复识别写成可追溯清洗规则和分组汇总表。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(6),
    knowledgeSources: ['knowledge/concepts/项目目录结构与可复现.md', 'knowledge/sources/Starting_Data_Analytics_GenAI.md'],
    materialSources: ['materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210'],
    coursebookTopics: ['缺失值处理', '异常值识别', '清洗日志']
  },
  {
    chapter: 7,
    week: 7,
    slug: 'week-07',
    title: '描述统计与分布可视化',
    page: '/coursebook#week-07',
    phase: '编程、清洗、统计与图表',
    summary: '用统计量和图形共同描述数据分布，避免只报告一个均值。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(7),
    knowledgeSources: ['knowledge/entities/ggplot2.md', 'knowledge/sources/Starting_Data_Analytics_GenAI.md'],
    materialSources: ['materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210'],
    coursebookTopics: ['描述统计', '分布可视化', '图形解释']
  },
  {
    chapter: 8,
    week: 8,
    slug: 'week-08',
    title: '统计推断基础',
    page: '/coursebook#week-08',
    phase: '编程、清洗、统计与图表',
    summary: '用样本、总体、不确定性、置信区间和 P 值解释统计推断边界。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(8),
    knowledgeSources: ['knowledge/sources/ISLP.md', 'knowledge/sources/ISLR.md'],
    materialSources: ['materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R'],
    coursebookTopics: ['统计推断', 'P 值误区', '检验前提']
  },
  {
    chapter: 9,
    week: 9,
    slug: 'week-09',
    title: '相关分析与线性回归',
    page: '/coursebook#week-09',
    phase: '编程、清洗、统计与图表',
    summary: '用散点图、相关系数、回归系数和残差训练变量关系解释边界。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(9),
    knowledgeSources: ['knowledge/sources/ISLP.md', 'knowledge/sources/ISLR.md'],
    materialSources: ['materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R'],
    coursebookTopics: ['相关分析', '线性回归', '因果边界']
  },
  {
    chapter: 10,
    week: 10,
    slug: 'week-10',
    title: '分类问题与逻辑回归',
    page: '/coursebook#week-10',
    phase: '编程、清洗、统计与图表',
    summary: '把二分类结局、概率、阈值和混淆矩阵转成克制的模型解释。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(10),
    knowledgeSources: ['knowledge/sources/ISLP.md', 'knowledge/sources/ISLR.md'],
    materialSources: ['materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R'],
    coursebookTopics: ['分类问题', '逻辑回归', '模型评价']
  },
  {
    chapter: 11,
    week: 11,
    slug: 'week-11',
    title: '科研图表规范与 SCI 图表表达',
    page: '/coursebook#week-11',
    phase: '编程、清洗、统计与图表',
    summary: '从坐标轴、图例、误差线、配色和图注训练科研图表表达。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(11),
    knowledgeSources: ['knowledge/entities/ggplot2.md', 'knowledge/sources/ISLR.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md'],
    coursebookTopics: ['科研图表规范', '图注写作', 'SCI 图表案例']
  },
  {
    chapter: 12,
    week: 12,
    slug: 'week-12',
    title: '高维数据与数学直觉',
    page: '/coursebook#week-12',
    phase: '高维、组学与综合项目',
    summary: '用表达矩阵解释向量、矩阵、标准化、距离和高维直觉。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(12),
    knowledgeSources: ['knowledge/concepts/差异表达分析.md', 'knowledge/sources/ISLP.md'],
    materialSources: ['materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python'],
    coursebookTopics: ['高维数据', '矩阵直觉', '距离度量']
  },
  {
    chapter: 13,
    week: 13,
    slug: 'week-13',
    title: 'PCA、聚类与热图',
    page: '/coursebook#week-13',
    phase: '高维、组学与综合项目',
    summary: '把 PCA、聚类和热图作为高维探索图形，强调参数和解释边界。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(13),
    knowledgeSources: ['knowledge/concepts/差异表达分析.md', 'knowledge/sources/ISLP.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/aidd.course_index.md', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python'],
    coursebookTopics: ['PCA', '聚类', '热图']
  },
  {
    chapter: 14,
    week: 14,
    slug: 'week-14',
    title: '转录组数据分析基础',
    page: '/coursebook/week-14',
    phase: '高维、组学与综合项目',
    summary: '解释 RNA-seq 从 FASTQ 到 count matrix 的链条，为差异表达分析建立输入核验基础。',
    status: '样章可读',
    reviewStatus: 'sample_ready',
    pptStatus: 'storyboard_pending',
    sourceWeekFiles: baseWeekFiles(14),
    knowledgeSources: ['knowledge/concepts/RNA-seq上游流程.md', 'knowledge/concepts/差异表达分析.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/chapter.course.md', 'materials/markdown/aidd_bioinformatics/aidd.course_index.md'],
    coursebookTopics: ['RNA-seq 流程', 'count matrix', 'metadata'],
    sample: {
      introQuestion: '表达矩阵从哪里来，它经过哪些质量控制和计数步骤才成为 Week 15 的统计输入？',
      learningObjectives: [
        '说明 RNA-seq 的目标是测量基因表达水平。',
        '描述 FASTQ 到 count matrix 的输入、处理和输出链条。',
        '检查 count matrix 与 metadata 的样本名、分组和总 counts 是否对齐。'
      ],
      coreConcepts: [
        { term: 'FASTQ', explanation: '测序 reads 和质量信息的原始格式，不是可以直接做统计检验的分析表。' },
        { term: 'SAM/BAM', explanation: 'reads 比对到参考基因组后的中间结果，服务后续排序、索引和计数。' },
        { term: 'count matrix', explanation: '基因 x 样本的计数矩阵，是差异表达分析的主要输入之一。' },
        { term: 'metadata', explanation: '记录样本分组、批次等信息，必须与 count matrix 列名一一对应。' }
      ],
      classroomCase: {
        title: '3 基因 x 4 样本 count matrix 核验',
        description: '用 `Ctrl_1`、`Ctrl_2`、`Drug_1`、`Drug_2` 的小矩阵训练样本对齐和总 counts 检查。',
        steps: [
          '说明行代表基因、列代表样本。',
          '检查列名是否全部出现在 metadata 的 `sample_id` 中。',
          '计算每个样本总 counts。',
          '解释为什么总 counts 差异会影响组间比较。'
        ]
      },
      aiBoundary: {
        allowed: ['把流程整理成输入、步骤、输出、质量问题四列表', '解释文件角色', '提示 metadata 对齐风险'],
        forbidden: ['替代上游 QC 判断', '伪造测序结果', '把字幕中的命令名不经核验写入正式 PPT', '跳过样本名核对']
      },
      verificationPoints: ['上游流程图中的软件名和文件格式进入 PPT 前需回查。', 'count matrix 示例必须和 metadata 样本名严格对齐。', '总 counts 计算要能现场复核。'],
      pptBridge: {
        status: 'Week 14 已进入可授课试点，但尚未生成 storyboard/PPTX。',
        entry: 'course/weeks/week_14/outline.md',
        nextActions: ['先生成 Week 14 storyboard。', '核对 AIDD 上游流程中的命令名、软件名和文件格式。', '再决定是否进入 SYSU 蓝模板 PPTX 生成。']
      }
    }
  },
  {
    chapter: 15,
    week: 15,
    slug: 'week-15',
    title: '差异表达分析与功能解读',
    page: '/coursebook/week-15',
    phase: '高维、组学与综合项目',
    summary: '从 count matrix 和 metadata 进入 DESeq2 结果表、火山图、热图和功能解释核验。',
    status: '样章可读',
    reviewStatus: 'evidence_review_pass',
    pptStatus: 'storyboard_reviewed_and_pptx_trial_done',
    sourceWeekFiles: [...baseWeekFiles(15), 'course/weeks/week_15/ppt_storyboard.md'],
    knowledgeSources: ['knowledge/entities/DESeq2.md', 'knowledge/concepts/差异表达分析.md', 'knowledge/concepts/富集分析_GO_KEGG.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md', 'materials/markdown/aidd_bioinformatics/10_Microarray_Analysis_on_R/chapter.course.md'],
    coursebookTopics: ['差异表达分析', '火山图', '功能富集'],
    sample: {
      introQuestion: '怎样从高维差异表达结果走向克制、可核验的功能解释，而不是只找 P 值最小的基因？',
      learningObjectives: [
        '说明差异表达分析的输入、输出和统计问题。',
        '区分 `baseMean`、`log2FoldChange`、`pvalue` 和 `padj` 各自回答的问题。',
        '解释火山图、热图和功能富集只提供候选证据，不直接证明机制。'
      ],
      coreConcepts: [
        { term: 'log2FoldChange', explanation: '表达变化方向和幅度的效应量指标。' },
        { term: 'pvalue', explanation: '原始检验显著性，面对大量基因时容易放大假阳性风险。' },
        { term: 'padj', explanation: '多重检验校正后的显著性，本课堂用于候选筛选而不是最终医学结论。' },
        { term: '功能解读', explanation: '从候选基因走向数据库或文献核验的过程，不是 AI 直接写机制。' }
      ],
      classroomCase: {
        title: 'DESeq2 结果表字段判读',
        description: '学生用教学模拟结果表按 `padj < 0.05` 和 `abs(log2FoldChange) > 1` 标记候选基因。',
        steps: [
          '逐列说明字段能回答什么问题。',
          '按同一阈值标记上调、下调和不确定。',
          '写一句火山图图注，说明横轴、纵轴和颜色。',
          '列出功能解读前必须回查的数据库或文献证据。'
        ]
      },
      aiBoundary: {
        allowed: ['整理筛选规则', '生成火山图解释模板', '生成待核验清单', '帮助改写图注语言'],
        forbidden: ['编造基因功能', '把候选通路写成机制事实', '把模拟数据写成真实医学结论', '跳过数据库或文献核验']
      },
      verificationPoints: ['所有模拟表格和图形需要标注教学模拟。', 'DESeq2 术语进入 PPT 前需核对官方文档或原始字幕。', '基因功能和通路解释必须保留“需核验”状态。'],
      pptBridge: {
        status: 'Week 15 已完成 storyboard、evidence review、SYSU 官方蓝模板 PPTX、PNG 导出和 contact sheet QA。',
        entry: 'course/weeks/week_15/ppt_storyboard.md',
        nextActions: ['后续修改应先更新 storyboard。', '再运行 evidence review。', '最后重新生成 PPTX 并做 PNG/contact sheet 视觉 QA。']
      }
    }
  },
  {
    chapter: 16,
    week: 16,
    slug: 'week-16',
    title: '单细胞转录组可视化',
    page: '/coursebook/week-16',
    phase: '高维、组学与综合项目',
    summary: '用 QC、UMAP、cluster 和 marker 图训练单细胞可视化解读和参数敏感性意识。',
    status: '样章可读',
    reviewStatus: 'sample_ready',
    pptStatus: 'storyboard_pending',
    sourceWeekFiles: baseWeekFiles(16),
    knowledgeSources: ['knowledge/concepts/差异表达分析.md', 'knowledge/sources/ISLP.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md'],
    coursebookTopics: ['单细胞可视化', 'UMAP', 'marker gene'],
    sample: {
      introQuestion: '单细胞图形如何呈现细胞异质性，又为什么不能把 UMAP 和 cluster 直接写成最终生物学结论？',
      learningObjectives: [
        '区分 bulk RNA-seq 与 scRNA-seq 的数据含义。',
        '读懂 QC、UMAP/t-SNE、cluster 和 marker gene 图。',
        '识别过滤阈值、PCA 维度和 resolution 等参数会影响结果。'
      ],
      coreConcepts: [
        { term: 'cell x gene matrix', explanation: '单细胞数据以细胞为观测单位，比 bulk 平均表达更细，但更稀疏。' },
        { term: 'QC 指标', explanation: '`nFeature`、`nCount` 和 `percent.mt` 用于发现低质量细胞、空液滴或受损细胞。' },
        { term: 'UMAP/t-SNE', explanation: '用于观察细胞状态结构的可视化方法，不是严格定量距离。' },
        { term: 'marker gene', explanation: '支持候选细胞注释的表达证据，需要组合数据库、文献和上下文核验。' }
      ],
      classroomCase: {
        title: '单细胞图形四栏解读表',
        description: '把每张图拆成“图上看到什么、可能解释、不确定性、待核验点”。',
        steps: [
          '判断 QC 图是否提示低质量细胞群。',
          '说明 UMAP 上每个点、颜色和 cluster 标签代表什么。',
          '根据 marker 表达提出候选细胞类型，而不是最终注释。',
          '列出至少 3 个可能影响图形结果的参数。'
        ]
      },
      aiBoundary: {
        allowed: ['梳理 scRNA-seq 流程', '列出参数敏感点', '解释 marker 候选含义', '生成图形解读表框架'],
        forbidden: ['直接给出最终细胞类型注释', '把 UMAP 距离解释为真实生物距离', '忽略参数设置', '编造 marker 证据']
      },
      verificationPoints: ['公开展示图需确认数据来源和授权。', 'UMAP 距离、cluster 含义和 marker 注释需避免过度解释。', '参数敏感性必须在讲稿和后续 storyboard 中明示。'],
      pptBridge: {
        status: 'Week 16 已进入可授课试点，但尚未生成 storyboard/PPTX。',
        entry: 'course/weeks/week_16/outline.md',
        nextActions: ['准备可公开展示的 QC/UMAP/marker 示例图。', '生成 Week 16 storyboard。', '先做 evidence review，再进入 PPTX 生成。']
      }
    }
  },
  {
    chapter: 17,
    week: 17,
    slug: 'week-17',
    title: '综合项目工作坊：AI 协作分析与结果核验',
    page: '/coursebook#week-17',
    phase: '高维、组学与综合项目',
    summary: '把数据清洗、统计、图表、AI 记录和结果复核串成一个可信项目。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(17),
    knowledgeSources: ['knowledge/concepts/项目目录结构与可复现.md', 'knowledge/entities/GitHub.md', 'knowledge/concepts/AI协作边界.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/12_GitHub_Guide_for_Students/chapter.course.md', 'materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210'],
    coursebookTopics: ['综合项目', 'AI 审计', '结果核验']
  },
  {
    chapter: 18,
    week: 18,
    slug: 'week-18',
    title: '综合项目汇报与课程总结',
    page: '/coursebook#week-18',
    phase: '高维、组学与综合项目',
    summary: '训练学生用证据、边界和责任意识完成医药数据分析汇报。',
    status: '目录占位',
    reviewStatus: 'catalog_only',
    pptStatus: 'not_started',
    sourceWeekFiles: baseWeekFiles(18),
    knowledgeSources: ['knowledge/concepts/AI协作边界.md', 'knowledge/entities/GitHub.md'],
    materialSources: ['materials/markdown/aidd_bioinformatics/12_GitHub_Guide_for_Students/chapter.course.md'],
    coursebookTopics: ['项目汇报', 'AI 使用反思', '课程总结']
  }
];

export const sampleChapters = coursebookChapters.filter((chapter) => chapter.sample);

export function getCoursebookChapterBySlug(slug: string) {
  return coursebookChapters.find((chapter) => chapter.slug === slug);
}

export function getCoursebookChapterByWeek(week: number) {
  return coursebookChapters.find((chapter) => chapter.week === week);
}
