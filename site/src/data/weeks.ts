export type Week = {
  week: number;
  slug: string;
  title: string;
  phase: string;
  keywords: string[];
  question: string;
  goals: string[];
  outline: string[];
  practice: string;
  aiBoundary: string;
  sourcePaths: string[];
  coursebook: string[];
};

export const weeks: Week[] = [
  {
    week: 1,
    slug: 'week-01',
    title: '课程导论与医药数据特征',
    phase: 'AI 边界、流程与复现',
    keywords: ['医药数据', '多源性', '高维性', 'AI 边界'],
    question: '面对一个医药问题，如何把问题转化为可分析的数据链条？',
    goals: ['识别常见医药数据类型', '理解多源、高维、异质和强解释性要求', '建立 AI 只能辅助、不能替代判断的底线'],
    outline: ['医药数据类型与课程任务', 'Python、R、Bash 的角色分工', 'AI 可做与不可做的边界', '个人学习项目目录初识'],
    practice: '写下一个医药数据问题，并说明需要的数据字段、可视化方式和人工核验点。',
    aiBoundary: '只用于概念解释、问题拆解和边界讨论，不直接生成结论。',
    sourcePaths: ['course/weeks/week_01', 'knowledge/concepts/医药数据特征.md', 'knowledge/concepts/AI协作边界.md'],
    coursebook: ['医药数据类型', 'AI 协作边界', '工具分工 Python/R/Bash']
  },
  {
    week: 2,
    slug: 'week-02',
    title: '数据分析流程、复现规范与人机协作规范',
    phase: 'AI 边界、流程与复现',
    keywords: ['项目目录', '可复现', 'Pipeline', 'Prompt 记录'],
    question: '怎样让一次医药数据分析可追溯、可复查、可复现？',
    goals: ['掌握项目文件组织规则', '理解输入、处理、输出的 pipeline 思维', '建立 AI 协作记录模板'],
    outline: ['规范项目目录', '原始数据和结果分离', 'Prompt、输出、核验与修改留痕', 'GitHub 与项目协作基础'],
    practice: '建立个人课程项目目录，并记录一次 AI 报错解释过程。',
    aiBoundary: 'AI 用于解释报错和流程风险，不替代目录设计与清洗决策。',
    sourcePaths: ['course/weeks/week_02', 'knowledge/concepts/项目目录结构与可复现.md', 'knowledge/entities/GitHub.md'],
    coursebook: ['可复现分析', 'AI 协作记录', 'Pipeline 思维']
  },
  {
    week: 3,
    slug: 'week-03',
    title: 'AI 辅助编程与 Python 快速入门',
    phase: '编程、清洗、统计与图表',
    keywords: ['Python', '变量', '列表', '字典', '调试'],
    question: '怎样用最小 Python 语法完成可核验的医药指标处理？',
    goals: ['理解变量、列表、字典、条件和循环', '用小数据手算结果核验代码', '练习解释代码、定位错误、生成小片段三类 prompt'],
    outline: ['Python 环境与基本对象', '列表与缺失值处理', '条件循环与指标筛选', 'AI 生成代码的逐行核验'],
    practice: '处理 `glucose = [5.2, 6.1, 4.9, None, 12.8, 5.7]`，过滤缺失、计算均值并标记高风险值。',
    aiBoundary: '可请求 AI 解释代码和局部调试，但必须人工手算小样例核验。',
    sourcePaths: ['course/weeks/week_03', 'course/first_round_content.md', 'knowledge/entities/Python.md'],
    coursebook: ['Python 快速入门', '缺失值小案例', 'AI 辅助调试']
  },
  {
    week: 4,
    slug: 'week-04',
    title: 'R 基础语法、数据框操作与 AI 代码核验',
    phase: '编程、清洗、统计与图表',
    keywords: ['R', '数据框', '因子', 'ggplot2', '代码核验'],
    question: '为什么 R 的数据框和因子是后续统计与作图的基础？',
    goals: ['理解向量、矩阵、数据框和因子', '区分连续变量和分组变量', '掌握 AI 生成 R 代码的检查点'],
    outline: ['R 对象与 Python 对象对照', '数据框与因子', '包安装与加载', '列名、对象名和变量类型核验'],
    practice: '构建简化药物分组数据框，检查分组变量类型并计算每组均值。',
    aiBoundary: 'AI 可检查代码结构，不能替代变量类型判断。',
    sourcePaths: ['course/weeks/week_04', 'knowledge/entities/R.md', 'knowledge/entities/ggplot2.md'],
    coursebook: ['R 数据框', '因子变量', 'R 代码核验清单']
  },
  {
    week: 5,
    slug: 'week-05',
    title: '数据读取与整形',
    phase: '编程、清洗、统计与图表',
    keywords: ['CSV', 'Excel', '长宽表', '数据类型'],
    question: '如何把原始文件整理成适合统计和绘图的分析表？',
    goals: ['掌握 CSV/Excel 读写思路', '识别列名和数据类型问题', '理解长表与宽表转换'],
    outline: ['数据读入与编码问题', '列名整理和类型识别', '原始数据、清洗数据、分析数据分层', '长宽表转换'],
    practice: '读取不规范表格，统一列名，检查类型，并把重复测量宽表转换成长表。',
    aiBoundary: 'AI 可帮助排查读写错误和生成局部转换代码，不能决定字段删改。',
    sourcePaths: ['course/weeks/week_05', 'materials/markdown/pdf_library_mineru', 'materials/markdown/aidd_bioinformatics'],
    coursebook: ['数据读取', '数据整形', '表格结构与文件格式']
  },
  {
    week: 6,
    slug: 'week-06',
    title: '缺失值、异常值处理与分组汇总',
    phase: '编程、清洗、统计与图表',
    keywords: ['缺失值', '异常值', 'IQR', '分组汇总'],
    question: '数据清洗规则怎样影响分析可信度？',
    goals: ['区分缺失、异常和重复问题', '理解删除、填补和保留的风险', '形成清洗日志'],
    outline: ['缺失机制直观解释', '箱线图、Z 分数和 IQR', '重复值判断', '按组生成汇总表'],
    practice: '统计缺失比例、定位异常值、按组汇总，并写出清洗规则。',
    aiBoundary: 'AI 可列出策略和风险，不能替学生决定删除或填补。',
    sourcePaths: ['course/weeks/week_06', 'knowledge/concepts/RNA-seq上游流程.md'],
    coursebook: ['缺失值处理', '异常值识别', '清洗日志']
  },
  {
    week: 7,
    slug: 'week-07',
    title: '描述统计与分布可视化',
    phase: '编程、清洗、统计与图表',
    keywords: ['均值', '中位数', '直方图', '箱线图'],
    question: '图形怎样帮助我们在检验前理解数据分布？',
    goals: ['理解均值、中位数、标准差和四分位数', '选择直方图、箱线图和误差线图', '人工解释图形而不是只看代码'],
    outline: ['描述统计量', '分布形态与偏态', '分组比较图', '图例、单位和样本量标注'],
    practice: '按组计算统计量，绘制直方图和箱线图，并解释分布差异。',
    aiBoundary: 'AI 可优化绘图脚本，但图形解释必须人工完成。',
    sourcePaths: ['course/weeks/week_07', 'knowledge/entities/ggplot2.md'],
    coursebook: ['描述统计', '分布可视化', '图形解释']
  },
  {
    week: 8,
    slug: 'week-08',
    title: '统计推断基础',
    phase: '编程、清洗、统计与图表',
    keywords: ['抽样', '置信区间', 'P 值', '检验前提'],
    question: '什么时候可以从样本数据推断总体差异？',
    goals: ['理解抽样误差和不确定性', '解释置信区间和 P 值', '识别常见检验前提'],
    outline: ['样本与总体', '置信区间', 'P 值的正确解释', 't 检验和非参数检验直觉'],
    practice: '比较两组指标，写出检验前提、结果解释和局限。',
    aiBoundary: 'AI 可辅助解释概念，但不得编造统计结论。',
    sourcePaths: ['course/weeks/week_08', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R'],
    coursebook: ['统计推断', 'P 值误区', '检验前提']
  },
  {
    week: 9,
    slug: 'week-09',
    title: '相关分析与线性回归',
    phase: '编程、清洗、统计与图表',
    keywords: ['相关', '线性回归', '散点图', '残差'],
    question: '两个医学指标的关系如何被量化、可视化和审慎解释？',
    goals: ['区分相关和因果', '理解简单线性回归', '用散点图和残差检查模型'],
    outline: ['Pearson 和 Spearman 相关', '线性回归模型', '散点图与拟合线', '结果解释边界'],
    practice: '对两个连续指标做相关分析和线性回归，并说明不能推出因果的原因。',
    aiBoundary: 'AI 可检查代码和解释输出项，不能把相关写成因果。',
    sourcePaths: ['course/weeks/week_09', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python'],
    coursebook: ['相关分析', '线性回归', '模型解释边界']
  },
  {
    week: 10,
    slug: 'week-10',
    title: '分类问题与逻辑回归',
    phase: '编程、清洗、统计与图表',
    keywords: ['分类', '逻辑回归', '混淆矩阵', 'ROC'],
    question: '怎样分析二分类结局并避免过度承诺预测能力？',
    goals: ['理解二分类结局和概率输出', '掌握逻辑回归基本解释', '识别准确率、敏感度、特异度和 ROC 的含义'],
    outline: ['分类问题定义', '逻辑回归直觉', '混淆矩阵', '模型评价和局限'],
    practice: '用简化数据拟合逻辑回归，报告 OR 或概率解释，并写出局限。',
    aiBoundary: 'AI 可辅助解释指标，不得夸大模型性能。',
    sourcePaths: ['course/weeks/week_10', 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python'],
    coursebook: ['分类问题', '逻辑回归', '模型评价']
  },
  {
    week: 11,
    slug: 'week-11',
    title: '科研图表规范与 SCI 图表表达',
    phase: '编程、清洗、统计与图表',
    keywords: ['SCI 图表', '图注', '配色', '导出规范'],
    question: '什么样的图表能准确表达科研证据？',
    goals: ['掌握图表基本元素', '理解色盲友好和导出规范', '写出不编造信息的图注'],
    outline: ['标题、坐标轴、单位和图例', '配色与可读性', 'DPI、尺寸和文件格式', '论文图注写法'],
    practice: '把一张不规范图改成规范图，并写出经人工核验的图注。',
    aiBoundary: 'AI 只能润色已有事实，不得增加样本量、P 值或统计方法。',
    sourcePaths: ['course/weeks/week_11', 'knowledge/entities/ggplot2.md'],
    coursebook: ['科研图表规范', '图注写作', 'SCI 图表案例']
  },
  {
    week: 12,
    slug: 'week-12',
    title: '高维数据与数学直觉',
    phase: '高维、组学与综合项目',
    keywords: ['矩阵', '标准化', '距离', '高维数据'],
    question: '为什么高维医药数据需要矩阵、标准化和距离直觉？',
    goals: ['理解样本 x 变量矩阵', '解释标准化目的', '建立距离度量直觉'],
    outline: ['表达矩阵和临床矩阵', '中心化与缩放', '欧氏距离和相关距离', '高维数据为什么难直接观察'],
    practice: '构建小型表达矩阵，标准化后计算样本间距离。',
    aiBoundary: 'AI 可做概念解释，但必须贴合医药数据场景。',
    sourcePaths: ['course/weeks/week_12', 'knowledge/concepts/差异表达分析.md'],
    coursebook: ['高维数据', '矩阵直觉', '距离度量']
  },
  {
    week: 13,
    slug: 'week-13',
    title: 'PCA、聚类与热图',
    phase: '高维、组学与综合项目',
    keywords: ['PCA', '聚类', '热图', '参数记录'],
    question: '探索性高维图形怎样帮助发现结构，也怎样可能误导解释？',
    goals: ['理解 PCA 主成分和解释方差', '区分层次聚类和 k-means', '记录热图参数和解释边界'],
    outline: ['PCA 直觉', '聚类方法', '热图标准化与颜色', '参数记录模板'],
    practice: '对模拟表达矩阵做 PCA、聚类和热图，写出标准化、距离和聚类参数。',
    aiBoundary: 'AI 可辅助调试参数，但不能把探索结果写成机制证明。',
    sourcePaths: ['course/weeks/week_13', 'materials/markdown/aidd_bioinformatics'],
    coursebook: ['PCA', '聚类', '热图']
  },
  {
    week: 14,
    slug: 'week-14',
    title: '转录组数据分析基础',
    phase: '高维、组学与综合项目',
    keywords: ['RNA-seq', 'FASTQ', 'BAM', 'count matrix'],
    question: '表达矩阵从哪里来，它经过哪些质量控制和计数步骤？',
    goals: ['理解 RNA-seq 从 reads 到 count matrix 的链条', '区分 FASTQ、SAM/BAM 和 count matrix', '检查 metadata 与样本名对齐'],
    outline: ['SRA/FASTQ', 'QC 与 trimming', '比对、排序和索引', 'feature extraction 与 count matrix'],
    practice: '检查小型 count matrix 与 metadata 的样本名、总 counts 和分组。',
    aiBoundary: 'AI 可梳理流程，不能替代上游质控和参数判断。',
    sourcePaths: ['course/weeks/week_14', 'course/first_round_content.md', 'knowledge/concepts/RNA-seq上游流程.md'],
    coursebook: ['RNA-seq 流程', 'count matrix', 'metadata']
  },
  {
    week: 15,
    slug: 'week-15',
    title: '差异表达分析与功能解读',
    phase: '高维、组学与综合项目',
    keywords: ['DESeq2', 'log2FC', 'padj', '火山图'],
    question: '怎样从高维差异结果走向克制、可核验的功能解释？',
    goals: ['理解差异表达输入和输出', '区分 log2FoldChange、pvalue 和 padj', '掌握火山图和热图解释边界'],
    outline: ['DESeq2 基本思想', '多重检验校正', '火山图和热图', '功能富集和文献核验'],
    practice: '读取差异表达表，筛选基因，绘制火山图，并标注需要核验的功能解释。',
    aiBoundary: 'AI 可整理表格和解释模板，不得编造基因功能。',
    sourcePaths: ['course/weeks/week_15', 'course/first_round_content.md', 'knowledge/entities/DESeq2.md', 'knowledge/concepts/富集分析_GO_KEGG.md'],
    coursebook: ['差异表达分析', '火山图', '功能富集']
  },
  {
    week: 16,
    slug: 'week-16',
    title: '单细胞转录组可视化',
    phase: '高维、组学与综合项目',
    keywords: ['scRNA-seq', 'QC', 'UMAP', 'marker'],
    question: '单细胞图形如何呈现细胞异质性，又为何依赖参数和注释核验？',
    goals: ['区分 bulk RNA-seq 与 scRNA-seq', '理解 QC、HVG、PCA、UMAP、clustering 和 marker 流程', '识别参数敏感性'],
    outline: ['单细胞数据特点', 'QC 指标', '降维聚类', 'marker 展示和细胞类型注释'],
    practice: '阅读一组 UMAP、QC 和 marker 图，写出可能解释及需要核验的参数。',
    aiBoundary: 'AI 可梳理流程和参数风险，不能替代细胞类型注释。',
    sourcePaths: ['course/weeks/week_16', 'course/first_round_content.md', 'knowledge/concepts/差异表达分析.md'],
    coursebook: ['单细胞可视化', 'UMAP', 'marker gene']
  },
  {
    week: 17,
    slug: 'week-17',
    title: '综合项目工作坊：AI 协作分析与结果核验',
    phase: '高维、组学与综合项目',
    keywords: ['项目', '代码重构', '结果核验', '报告初稿'],
    question: '怎样把数据清洗、统计、图表和 AI 记录串成一个可信项目？',
    goals: ['定义项目问题和数据字典', '完成分析计划和图表计划', '整理 AI 协作记录与报告初稿'],
    outline: ['研究问题定义', '数据字典与清洗记录', '分析计划与图表计划', 'AI 输出审查和报告整合'],
    practice: '完成项目流程表、核心图表草稿和 AI 协作记录摘要。',
    aiBoundary: 'AI 可辅助流程梳理、代码重构和语言修改，所有结论必须人工核验。',
    sourcePaths: ['course/weeks/week_17', 'knowledge/concepts/项目目录结构与可复现.md', 'knowledge/entities/GitHub.md'],
    coursebook: ['综合项目', 'AI 审计', '结果核验']
  },
  {
    week: 18,
    slug: 'week-18',
    title: '综合项目汇报与课程总结',
    phase: '高维、组学与综合项目',
    keywords: ['答辩', '图表汇报', 'AI 反思', '课程总结'],
    question: '怎样用证据、边界和责任意识完成一次医药数据分析汇报？',
    goals: ['组织项目汇报结构', '回答方法和结果解释问题', '总结 AI 使用帮助、风险和核验'],
    outline: ['问题、数据、方法、图表、结论', '答辩问题清单', 'AI 协作反思', '课程总收束'],
    practice: '完成项目汇报、提交 AI 协作记录和反思报告。',
    aiBoundary: 'AI 可帮助反思记录和语言修改，不能美化过程或替代答辩。',
    sourcePaths: ['course/weeks/week_18', 'course/templates', 'outputs'],
    coursebook: ['项目汇报', 'AI 使用反思', '课程总结']
  }
];

export const phases = [
  {
    name: 'AI 边界、流程与复现',
    weeks: [1, 2],
    summary: '先建立问题定义、项目组织、复现规范和人机协作边界。'
  },
  {
    name: '编程、清洗、统计与图表',
    weeks: [3, 4, 5, 6, 7, 8, 9, 10, 11],
    summary: '用 Python、R、清洗、统计和图表表达建立可核验的基础能力。'
  },
  {
    name: '高维、组学与综合项目',
    weeks: [12, 13, 14, 15, 16, 17, 18],
    summary: '进入矩阵、高维可视化、转录组、单细胞和综合项目汇报。'
  }
];

export function getWeekLabel(week: number) {
  return `Week ${String(week).padStart(2, '0')}`;
}
