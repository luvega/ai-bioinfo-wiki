export type Resource = {
  title: string;
  type: string;
  source: string;
  weeks: string;
  use: string;
  status: '已课程化' | '待筛选' | '扩展素材';
};

export const resources: Resource[] = [
  {
    title: '36 课时 AI 前置课程大纲',
    type: '课程主线',
    source: 'course/syllabus/36课时-AI前置调整版.docx',
    weeks: 'Week 01-18',
    use: '确定周次、主题、教学目标和 AI 使用边界。',
    status: '已课程化'
  },
  {
    title: '课程教学讲稿',
    type: '课程主线',
    source: 'course/syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md',
    weeks: 'Week 01-18',
    use: '作为周次页面、讲稿摘要和课堂任务的主要来源。',
    status: '已课程化'
  },
  {
    title: 'AIDD Bioinformatics Course',
    type: '生物信息学素材',
    source: 'materials/markdown/aidd_bioinformatics/',
    weeks: 'Week 01-04, 14-18',
    use: '补充 Python/R/Bash 分工、pipeline、RNA-seq、DESeq2、scRNA-seq 和 GitHub 协作案例。',
    status: '扩展素材'
  },
  {
    title: 'An Introduction to Statistical Learning with Applications in Python',
    type: '参考书',
    source: 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python/',
    weeks: 'Week 08-10',
    use: '扩展统计学习、回归、分类和模型评估案例。',
    status: '待筛选'
  },
  {
    title: 'An Introduction to Statistical Learning with Applications in R',
    type: '参考书',
    source: 'materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R/',
    weeks: 'Week 04, 08-10',
    use: '补充 R 统计建模与图形表达内容。',
    status: '待筛选'
  },
  {
    title: 'Learn AI-Assisted Python Programming',
    type: 'AI 编程参考',
    source: 'materials/markdown/pdf_library_mineru/R240_Learn_AI_Assisted_Python_Programming_With_GitHub_Copilot_and_ChatGPT_2023_Leo_Porter_Daniel_Zingaro/',
    weeks: 'Week 03, 17',
    use: '支撑 AI 辅助编程、代码解释、调试和学习反思。',
    status: '扩展素材'
  },
  {
    title: 'Starting Data Analytics with Generative AI and Python',
    type: 'AI 数据分析参考',
    source: 'materials/markdown/pdf_library_mineru/Starting_Data_Analytics_with_Generative_AI_and_Python_9781633437210/',
    weeks: 'Week 02-11',
    use: '补充数据分析流程、生成式 AI 协作和 Python 分析案例。',
    status: '扩展素材'
  },
  {
    title: '嵩天 Python PPT',
    type: '外部课件',
    source: 'materials/markdown/pdf_library_mineru/Pythonppt/',
    weeks: 'Week 03',
    use: '作为 Python 快速入门的补充材料，需重新课程化后使用。',
    status: '待筛选'
  },
  {
    title: 'AI 协作记录模板',
    type: '规范模板',
    source: 'course/templates/',
    weeks: 'Week 01-18',
    use: '记录 Prompt、AI 输出、人工核验、修改和风险反思。',
    status: '已课程化'
  },
  {
    title: '知识索引',
    type: '知识层',
    source: 'knowledge/index.md',
    weeks: 'Week 01-18',
    use: '连接 source、entity、concept 和 synthesis 页面，作为资源索引生成来源。',
    status: '已课程化'
  }
];
