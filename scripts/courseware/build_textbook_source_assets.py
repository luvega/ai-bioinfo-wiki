"""Generate first-draft textbook chapters and source-controlled teaching assets.

The generated files are intentionally small, inspectable source assets. Binary
exports such as PNG, PPTX, and contact sheets still belong in outputs/.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEXTBOOK = ROOT / "course" / "textbook"
CHAPTERS_DIR = TEXTBOOK / "chapters"
ASSETS_DIR = TEXTBOOK / "assets"


@dataclass(frozen=True)
class ChapterSpec:
    week: int
    title: str
    phase: str
    intro: str
    goals: tuple[str, str, str]
    concepts: tuple[tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str]]
    route: str
    case_title: str
    dataset_name: str
    code_name: str
    diagram_name: str
    source_refs: tuple[str, str, str]
    exercise: str
    answer: str


CHAPTERS: tuple[ChapterSpec, ...] = (
    ChapterSpec(
        1,
        "课程导论与医药数据特征",
        "课程入口与 AI 边界",
        "某药治疗前后血糖下降，是否可以据此说药物有效？",
        ("识别医药数据的字段、单位和来源。", "把药学问题拆成数据、方法、图表和证据边界。", "说明 AI 可以辅助解释和检查，不能替代医学判断。"),
        (("医药数据", "来自临床、实验、公共数据库或文献的结构化或半结构化资料。"), ("证据边界", "数据和方法能够支持的结论范围。"), ("工具分工", "Python、R、Bash 和 AI 分别服务不同环节。"), ("课程契约", "记录来源、代码、图表、AI 使用和人工核验的共同规范。")),
        "问题 -> 字段 -> 图表 -> 边界",
        "血糖变化小表",
        "week01_glucose_contract.csv",
        "week01_glucose_contract.py",
        "week01_evidence_chain.mmd",
        ("knowledge/concepts/医药数据特征.md", "knowledge/concepts/AI协作边界.md", "course/weeks/week_01/teaching_pack_v1.md"),
        "填写一张“问题-字段-图表-证据边界”四列表。",
        "答案应保留 adherence、分组和模拟数据边界，不能写成“药物有效”。",
    ),
    ChapterSpec(
        2,
        "数据分析流程、复现规范与人机协作规范",
        "课程入口与 AI 边界",
        "为什么一个能跑通的结果，如果没有目录、来源和 Prompt 记录，仍然不能算可靠分析？",
        ("建立课程项目目录。", "说明原始数据、处理脚本和结果之间的追溯关系。", "记录 AI 使用的 Prompt、输出、人工修改和不采纳理由。"),
        (("可复现", "他人能理解输入、步骤、参数和输出。"), ("项目目录", "把 raw、processed、scripts、results、docs 和 ai_logs 分开。"), ("Prompt 记录", "AI 协作的可审计轨迹。"), ("Git/GitHub", "记录关键版本和协作修改。")),
        "原始数据 -> 脚本 -> 结果 -> 报告 -> 审计",
        "课程项目目录检查",
        "week02_project_manifest.csv",
        "week02_project_manifest.py",
        "week02_reproducible_workflow.mmd",
        ("knowledge/concepts/项目目录结构与可复现.md", "knowledge/sources/OWF_Learn_Git.md", "course/weeks/week_02/teaching_pack_v1.md"),
        "为一个课程项目写 README 结构和 AI 使用记录字段。",
        "答案应包含数据来源、运行顺序、环境说明和 AI 核验记录。",
    ),
    ChapterSpec(
        3,
        "AI 辅助编程与 Python 快速入门",
        "编程、清洗与核验",
        "怎样把“忽略缺失值、计算均值、标记高风险值”转成学生能读懂和手算核验的 Python 代码？",
        ("识别变量、列表、条件和循环。", "用小数据手算核验代码输出。", "要求 AI 解释代码和报错，而不是替代判断。"),
        (("变量", "保存一个指标或状态。"), ("列表", "保存一组医药指标值。"), ("缺失值", "必须先定义处理规则。"), ("边界测试", "用极小样本暴露代码漏洞。")),
        "小数据 -> 代码 -> 手算 -> AI 审计",
        "血糖列表处理",
        "week03_glucose_values.csv",
        "week03_glucose_filter.py",
        "week03_python_audit_loop.mmd",
        ("knowledge/entities/Python.md", "knowledge/sources/Learn_AI_Assisted_Python_Programming.md", "course/weeks/week_03/script.md"),
        "过滤缺失值，计算均值，标记大于 7.0 的值。",
        "有效值均值约为 6.94；12.8 是高风险值；阈值需人工说明来源。",
    ),
    ChapterSpec(
        4,
        "R 基础语法、数据框操作与 AI 代码核验",
        "编程、清洗与核验",
        "同一张药物分组表在 R 中为什么要区分数值变量和因子变量？",
        ("识别向量、数据框和因子。", "解释 R 代码输出与字段含义。", "检查 AI 生成 R 代码的对象名、列名和变量类型。"),
        (("data.frame", "R 中最常见的分析表。"), ("factor", "表示分组和类别的变量类型。"), ("ggplot2", "基于图层语法构建科研图。"), ("代码核验", "核对对象、列名、函数参数和输出。")),
        "表格 -> 数据框 -> 因子 -> 图层",
        "药物分组数据框",
        "week04_marker_table.csv",
        "week04_marker_summary.R",
        "week04_r_dataframe_layers.mmd",
        ("knowledge/entities/R.md", "knowledge/entities/ggplot2.md", "course/weeks/week_04/teaching_pack_v1.md"),
        "判断 group 是否应转为因子，并计算每组 marker 均值。",
        "group 是分类变量；Control 均值 2.25，Drug 均值 3.95；AI 不能猜列名。",
    ),
    ChapterSpec(
        5,
        "数据读取与整理",
        "编程、清洗与核验",
        "原始表能打开，为什么仍然不等于可分析表？",
        ("整理列名、单位和字段类型。", "建立数据字典。", "说明长表和宽表各自适合的图形或统计任务。"),
        (("原始表", "来源表，不能随意覆盖。"), ("数据字典", "字段含义、单位、类型和来源的说明。"), ("长表", "每行一个观测，适合分组作图。"), ("宽表", "每行一个样本，适合矩阵或模型输入。")),
        "原始表 -> 字段字典 -> 整形计划",
        "血糖表列名整理",
        "week05_raw_glucose_table.csv",
        "week05_dictionary_check.py",
        "week05_table_reshape.mmd",
        ("knowledge/concepts/项目目录结构与可复现.md", "knowledge/sources/Starting_Data_Analytics_GenAI.md", "course/weeks/week_05/teaching_pack_v1.md"),
        "把 Glu_pre/Glu_post 改写成清楚列名，并写字段字典。",
        "答案必须保留 unit；缩写含义需来源核验；长表适合按 time 作图。",
    ),
    ChapterSpec(
        6,
        "缺失值、异常值处理与分组汇总",
        "编程、清洗与核验",
        "面对缺失、异常和重复记录，为什么不能一删了之？",
        ("区分缺失、异常和重复的处理理由。", "写清洗日志。", "解释分组汇总表的风险。"),
        (("缺失值", "可能表示未记录、未检测或不适用。"), ("异常值", "可能是错误，也可能是真实极端情况。"), ("清洗日志", "记录每条处理规则和理由。"), ("分组汇总", "把个体信息压缩成组级统计量。")),
        "识别 -> 解释 -> 处理 -> 记录",
        "清洗日志示例",
        "week06_cleaning_cases.csv",
        "week06_cleaning_log.py",
        "week06_cleaning_decision.mmd",
        ("knowledge/concepts/项目目录结构与可复现.md", "knowledge/sources/Starting_Data_Analytics_GenAI.md", "course/weeks/week_06/teaching_pack_v1.md"),
        "为 5 条记录写缺失、异常、重复的处理建议。",
        "答案应先解释再处理；不能让 AI 自动删除异常值。",
    ),
    ChapterSpec(
        7,
        "描述统计与分布可视化",
        "统计、图表与矩阵桥接",
        "为什么一个均值不能充分描述一组医药指标？",
        ("计算均值、中位数、标准差和 IQR。", "用直方图、箱线图和密度图描述分布。", "写不夸大样本量和差异的图注。"),
        (("中心趋势", "均值和中位数描述典型水平。"), ("离散程度", "标准差和 IQR 描述变异。"), ("分布图", "显示偏态、离群点和分组差异。"), ("图注边界", "说明图支持什么和不能说明什么。")),
        "统计量 + 图形 + 克制图注",
        "药物浓度分布",
        "week07_concentration_distribution.csv",
        "week07_descriptive_stats.py",
        "week07_distribution_reading.mmd",
        ("knowledge/entities/ggplot2.md", "knowledge/sources/Starting_Data_Analytics_GenAI.md", "course/weeks/week_07/teaching_pack_v1.md"),
        "比较均值和中位数，并写一条箱线图图注。",
        "答案应指出分布可能偏态，不能只用均值代表全部样本。",
    ),
    ChapterSpec(
        8,
        "统计推断基础",
        "统计、图表与矩阵桥接",
        "P = 0.03 是否等于“有 97% 概率药物有效”？",
        ("解释样本、总体和抽样误差。", "区分效应量、置信区间和 P 值。", "把显著性语言改写为统计边界语言。"),
        (("总体", "研究希望推广到的对象集合。"), ("置信区间", "在模型设定下的不确定性区间。"), ("P 值", "在零假设下观察到当前或更极端结果的概率。"), ("效应量", "差异大小，不能由 P 值替代。")),
        "样本 -> 效应量 -> CI -> P 值 -> 边界",
        "统计输出解释",
        "week08_inference_result.csv",
        "week08_inference_language.py",
        "week08_inference_boundary.mmd",
        ("knowledge/sources/ISLP.md", "knowledge/sources/ISLR.md", "course/weeks/week_08/teaching_pack_v1.md"),
        "把“显著有效”改写成包含效应量、CI 和前提的表述。",
        "答案应写“在教学样本和模型设定下观察到差异”，不能写临床有效。",
    ),
    ChapterSpec(
        9,
        "相关分析与线性回归",
        "统计、图表与矩阵桥接",
        "两个指标相关，为什么仍然不能直接写成因果？",
        ("解释散点图、相关系数和回归系数。", "识别残差、异常点和混杂因素。", "把相关结果写成克制图注。"),
        (("相关系数", "描述两个变量线性关联强度和方向。"), ("回归系数", "在模型设定下自变量变化对应的平均响应变化。"), ("残差", "观测值与模型拟合值的差异。"), ("混杂", "同时影响解释变量和结局变量的第三因素。")),
        "散点 -> 相关 -> 回归 -> 残差 -> 因果边界",
        "剂量与指标散点图",
        "week09_dose_response.csv",
        "week09_regression_check.py",
        "week09_correlation_causation.mmd",
        ("knowledge/sources/ISLP.md", "knowledge/sources/ISLR.md", "course/weeks/week_09/teaching_pack_v1.md"),
        "根据散点图写一句相关/回归解释，并列出两个潜在混杂因素。",
        "答案应保留“相关不等于因果”，并检查异常点影响。",
    ),
    ChapterSpec(
        10,
        "分类问题与逻辑回归",
        "统计、图表与矩阵桥接",
        "风险概率超过阈值，是否等于可以做临床诊断？",
        ("解释二分类结局、预测概率和阈值。", "计算混淆矩阵。", "比较敏感度、特异度和漏报/误报成本。"),
        (("逻辑回归", "输出事件发生概率的分类模型。"), ("阈值", "把概率转成阳性/阴性的规则。"), ("混淆矩阵", "记录 TP、FP、FN、TN。"), ("适用性边界", "教学模型不等于临床可用模型。")),
        "概率 -> 阈值 -> 混淆矩阵 -> 风险解释",
        "预测概率阈值比较",
        "week10_risk_predictions.csv",
        "week10_confusion_matrix.py",
        "week10_threshold_tradeoff.mmd",
        ("knowledge/sources/ISLP.md", "knowledge/sources/ISLR.md", "course/weeks/week_10/teaching_pack_v1.md"),
        "分别用 0.5 和 0.7 阈值计算混淆矩阵。",
        "0.5 会产生一个误报；0.7 会把 P03 变成漏报；不能宣称临床可用。",
    ),
    ChapterSpec(
        11,
        "科研图表规范与 SCI 图表表达",
        "统计、图表与矩阵桥接",
        "一张图看起来漂亮，为什么仍可能无法支持论文结论？",
        ("用四层框架阅读科研图表。", "识别轴、单位、图例、样本量和统计标注。", "用 AI 改写图注但保留证据边界。"),
        (("视觉编码", "颜色、形状、位置和大小如何映射数据。"), ("图注", "让图脱离正文也能被理解。"), ("统计标注", "说明检验方法、样本量和显著性含义。"), ("证据边界", "图表支持的观察不等于机制结论。")),
        "数据来源 -> 视觉编码 -> 统计标注 -> 结论边界",
        "错误图注改写",
        "week11_figure_claims.csv",
        "week11_caption_audit.py",
        "week11_figure_evidence.mmd",
        ("knowledge/entities/ggplot2.md", "course/weeks/week_11_13_micro_project.md", "course/weeks/week_11/script.md"),
        "把一条过度图注改写为克制图注。",
        "答案应补轴、单位、样本量和待核验统计方法，不编造 P 值。",
    ),
    ChapterSpec(
        12,
        "高维数据与数学直觉",
        "统计、图表与矩阵桥接",
        "临床表格、样本 x 指标矩阵和表达矩阵本质上有什么共同点？",
        ("解释矩阵的行、列和 metadata。", "说明距离、标准化和尺度对图形的影响。", "把表格直觉桥接到表达矩阵。"),
        (("矩阵", "按行列组织样本和变量。"), ("标准化", "改变尺度，便于比较距离和模式。"), ("距离", "用数学方式描述样本或变量相似性。"), ("metadata", "解释样本分组、批次和来源的背景表。")),
        "临床表 -> 样本 x 指标 -> 表达矩阵 -> 高维图形",
        "6 samples x 5 genes 教学矩阵",
        "week12_expression_matrix.csv",
        "week12_standardize_matrix.py",
        "week12_matrix_bridge.mmd",
        ("knowledge/sources/ISLP.md", "knowledge/sources/Single_Cell_Best_Practices.md", "course/weeks/week_11_13_classroom_tables.md"),
        "说明一张矩阵中行、列、分组和批次各自的含义。",
        "答案应指出标准化影响距离和颜色尺度，不产生新的医学事实。",
    ),
    ChapterSpec(
        13,
        "PCA、聚类与热图",
        "组学图形与现代数据结构",
        "PCA、聚类、热图和 UMAP 显示了结构，为什么仍不能直接证明机制？",
        ("解释 PCA、聚类、热图和 UMAP 的输入输出。", "区分 bulk、single-cell、spatial 的观测单位。", "识别参数敏感性和图形误读风险。"),
        (("PCA", "观察主要变异方向的降维方法。"), ("聚类", "依赖距离和参数的候选分组。"), ("热图", "显示标准化矩阵模式的颜色图。"), ("UMAP", "探索邻近结构的可视化，不代表真实距离。")),
        "矩阵 -> 降维/聚类/热图 -> 候选解释 -> 待核验",
        "高维图形四栏解读",
        "week13_expression_matrix.csv",
        "week13_high_dimensional_figures.py",
        "week13_high_dimensional_reading.mmd",
        ("knowledge/sources/Single_Cell_Best_Practices.md", "knowledge/sources/OSCA.md", "course/weeks/week_13/teaching_assets.md"),
        "填写“输入-观察-候选解释-待核验点”四栏表。",
        "答案应写成图上观察和候选解释，不能把 cluster/UMAP 写成机制事实。",
    ),
    ChapterSpec(
        14,
        "转录组数据分析基础",
        "组学图形与现代数据结构",
        "表达矩阵从哪里来，为什么 metadata 对齐是差异分析前的底线？",
        ("描述 FASTQ 到 count matrix 的流程。", "核对 count matrix 与 metadata 样本名。", "说明 QC 和总 counts 的解释边界。"),
        (("FASTQ", "测序 reads 和质量信息。"), ("count matrix", "基因 x 样本计数表。"), ("metadata", "样本分组、批次和来源说明。"), ("QC", "检查数据质量和可用性。")),
        "FASTQ -> QC -> alignment/counting -> count matrix -> metadata",
        "count matrix 样本对齐",
        "week14_count_matrix.csv",
        "week14_count_matrix_qc.py",
        "week14_rnaseq_pipeline.mmd",
        ("knowledge/concepts/RNA-seq上游流程.md", "knowledge/sources/OSCA.md", "course/weeks/week_14/script.md"),
        "检查 count matrix 列名是否全部出现在 metadata 中。",
        "答案应指出样本名、分组和总 counts 必须对齐，不能跳过上游 QC。",
    ),
    ChapterSpec(
        15,
        "差异表达分析与功能解读",
        "组学图形与现代数据结构",
        "为什么差异表达结果表不是基因功能结论表？",
        ("解释 baseMean、log2FoldChange、pvalue 和 padj。", "判读火山图和热图。", "把功能解释写成候选并列出核验路径。"),
        (("log2FoldChange", "表达变化方向和幅度。"), ("pvalue", "原始检验显著性。"), ("padj", "多重检验校正后的显著性。"), ("功能富集", "候选基因集合和数据库条目的统计关联。")),
        "count matrix -> DE 结果 -> 图表 -> 功能候选 -> 核验",
        "DESeq2 结果表字段判读",
        "week15_deseq2_results.csv",
        "week15_de_filter.py",
        "week15_de_interpretation.mmd",
        ("knowledge/entities/DESeq2.md", "knowledge/concepts/富集分析_GO_KEGG.md", "course/weeks/week_15/script.md"),
        "按 padj 和 log2FoldChange 标记候选基因，并写火山图图注。",
        "答案应区分候选基因、统计显著和功能机制，AI 不能编造基因功能。",
    ),
    ChapterSpec(
        16,
        "单细胞转录组可视化",
        "组学图形与现代数据结构",
        "单细胞和空间组学图形怎样呈现异质性，又为什么容易被过度解释？",
        ("读懂 QC、UMAP、cluster、marker 和 spatial 图。", "说明细胞、spot 和样本的观测单位差异。", "识别参数和注释边界。"),
        (("cell x gene matrix", "以细胞为观测单位的表达矩阵。"), ("QC 指标", "帮助识别低质量细胞。"), ("marker gene", "支持候选注释的表达证据。"), ("spatial domain", "空间模式候选，不等于病理机制。")),
        "QC -> UMAP/cluster -> marker -> spatial -> 边界",
        "单细胞图形四栏解读",
        "week16_single_cell_figures.csv",
        "week16_single_cell_audit.py",
        "week16_single_cell_spatial.mmd",
        ("knowledge/sources/Single_Cell_Best_Practices.md", "knowledge/sources/OSTA.md", "course/weeks/week_16/script.md"),
        "为 UMAP/marker/spatial 图各写一个待核验点。",
        "答案应保留候选状态，不能把 UMAP 距离或 spatial domain 写成真实生物距离。",
    ),
    ChapterSpec(
        17,
        "综合项目工作坊：AI 协作分析与结果核验",
        "项目工作坊与汇报",
        "一个项目包怎样让同学和教师追溯问题、数据、代码、图表和 AI 使用？",
        ("整理 README、data_sources、AI statement 和 storyboard。", "完成图表证据边界自查。", "用 Git/GitHub 或等价记录保留关键版本。"),
        (("README", "说明项目问题、文件和运行顺序。"), ("data_sources", "记录数据来源、字段和授权边界。"), ("AI 使用声明", "说明工具、Prompt、用途和人工修改。"), ("storyboard", "把图表证据组织成汇报页。")),
        "项目问题 -> 素材溯源 -> 图表 -> AI 审计 -> storyboard",
        "项目交付包检查",
        "week17_project_package_check.csv",
        "week17_project_package_audit.py",
        "week17_project_workflow.mmd",
        ("knowledge/entities/GitHub.md", "knowledge/concepts/AI协作边界.md", "course/weeks/week_17/teaching_pack_v1.md"),
        "检查一个项目包是否包含五件最低交付物。",
        "答案应指出缺少数据来源、AI 使用声明或图表边界时不得进入最终汇报。",
    ),
    ChapterSpec(
        18,
        "综合项目汇报与课程总结",
        "项目工作坊与汇报",
        "最终汇报应评价漂亮图表，还是评价数据来源、证据边界和可复现记录？",
        ("使用统一 rubric 完成汇报和答辩。", "检查数据来源、图表表达、AI 使用和归档。", "总结全课程的数据分析链条。"),
        (("rubric", "统一评价维度和分值。"), ("答辩记录", "记录问题、回答和后续修订。"), ("归档说明", "确保项目可追溯和可复核。"), ("课程闭环", "从问题到数据、代码、图表、解释和 AI 审计。")),
        "汇报 -> 答辩 -> 修订 -> 归档 -> 反思",
        "项目汇报 rubric",
        "week18_presentation_rubric.csv",
        "week18_rubric_summary.py",
        "week18_course_closure.mmd",
        ("course/evaluation/student_project_rubric.md", "knowledge/concepts/项目目录结构与可复现.md", "course/weeks/week_18/teaching_pack_v1.md"),
        "用 rubric 给一个项目汇报样例打分并写修订建议。",
        "答案应优先看来源、图表证据、AI 声明和可复现记录，而不是只看排版。",
    ),
)


DATASETS: dict[int, list[list[str]]] = {
    1: [["patient_id", "group", "glucose_before", "glucose_after", "dose_mg", "adherence"], ["P01", "Control", "8.1", "8.0", "0", "good"], ["P02", "Control", "7.5", "7.7", "0", "missing"], ["P03", "Drug", "8.4", "6.9", "50", "good"], ["P04", "Drug", "9.1", "7.2", "50", "good"], ["P05", "Drug", "7.9", "7.8", "50", "poor"]],
    2: [["path", "role", "must_commit"], ["data_raw/", "original source data", "no"], ["data_processed/", "cleaned teaching tables", "yes"], ["scripts/", "analysis code", "yes"], ["results/", "figures and tables", "yes"], ["ai_logs/", "AI collaboration records", "no"]],
    3: [["value", "note"], ["5.2", "valid"], ["6.1", "valid"], ["4.9", "valid"], ["", "missing"], ["12.8", "high risk"], ["5.7", "valid"]],
    4: [["group", "marker"], ["control", "2.1"], ["control", "2.4"], ["treat", "3.8"], ["treat", "4.1"]],
    5: [["ID", "Group", "Glu_pre", "Glu_post", "Unit"], ["P01", "Ctrl", "8.1", "8.0", "mmol/L"], ["P02", "Ctrl", "7.5", "7.7", "mmol/L"], ["P03", "Drug", "8.4", "6.9", "mmol/L"], ["P04", "Drug", "9.1", "7.2", "mmol/L"]],
    6: [["patient_id", "group", "marker", "issue"], ["P01", "Control", "2.1", "ok"], ["P02", "Control", "", "missing"], ["P03", "Drug", "99.0", "unit_check"], ["P03", "Drug", "3.9", "duplicate"], ["P04", "Drug", "4.1", "ok"]],
    7: [["sample_id", "group", "concentration"], ["S01", "Control", "1.2"], ["S02", "Control", "1.5"], ["S03", "Control", "4.8"], ["S04", "Drug", "2.0"], ["S05", "Drug", "2.2"], ["S06", "Drug", "2.4"]],
    8: [["metric", "value"], ["mean_difference", "1.2"], ["ci_low", "0.2"], ["ci_high", "2.2"], ["p_value", "0.03"], ["sample_size", "teaching example"]],
    9: [["patient_id", "dose_mg", "response"], ["P01", "0", "1.1"], ["P02", "10", "1.4"], ["P03", "20", "1.8"], ["P04", "30", "2.3"], ["P05", "40", "2.1"]],
    10: [["patient_id", "predicted_risk", "observed_event"], ["P01", "0.20", "no"], ["P02", "0.45", "yes"], ["P03", "0.62", "yes"], ["P04", "0.70", "no"], ["P05", "0.82", "yes"]],
    11: [["claim", "issue", "safe_revision"], ["Drug group is significantly cured", "overclaim", "Teaching data show lower values in the drug group; clinical efficacy is not established."], ["UMAP proves a new cell type", "mechanism overclaim", "UMAP suggests a candidate cluster requiring marker validation."]],
    12: [["sample_id", "group", "batch", "GeneA", "GeneB", "GeneC", "GeneD", "GeneE"], ["Ctrl_1", "Control", "B1", "10", "8", "4", "5", "7"], ["Ctrl_2", "Control", "B1", "11", "7", "5", "4", "6"], ["Ctrl_3", "Control", "B2", "9", "8", "4", "5", "7"], ["Drug_1", "Drug", "B1", "17", "5", "8", "6", "4"], ["Drug_2", "Drug", "B2", "16", "4", "9", "7", "5"], ["Drug_3", "Drug", "B2", "18", "5", "8", "6", "4"]],
    13: [["sample_id", "group", "PC1", "PC2", "cluster"], ["Ctrl_1", "Control", "-1.9", "0.2", "1"], ["Ctrl_2", "Control", "-1.7", "-0.1", "1"], ["Ctrl_3", "Control", "-2.0", "0.0", "1"], ["Drug_1", "Drug", "1.8", "0.1", "2"], ["Drug_2", "Drug", "1.6", "-0.3", "2"], ["Drug_3", "Drug", "2.2", "0.1", "2"]],
    14: [["gene_id", "Ctrl_1", "Ctrl_2", "Drug_1", "Drug_2"], ["GeneA", "120", "118", "240", "230"], ["GeneB", "88", "91", "70", "68"], ["GeneC", "40", "44", "82", "85"]],
    15: [["gene_id", "baseMean", "log2FoldChange", "pvalue", "padj"], ["GeneA", "180", "1.25", "0.0005", "0.01"], ["GeneB", "80", "-0.45", "0.08", "0.20"], ["GeneC", "60", "1.80", "0.002", "0.03"], ["GeneD", "15", "-2.10", "0.04", "0.12"]],
    16: [["cell_id", "cluster", "nFeature", "percent_mt", "marker", "spatial_region"], ["Cell01", "0", "2100", "4.2", "GeneA", "Region1"], ["Cell02", "0", "2050", "5.1", "GeneA", "Region1"], ["Cell03", "1", "1800", "9.8", "GeneC", "Region2"], ["Cell04", "1", "900", "22.0", "GeneC", "Region2"]],
    17: [["item", "present", "risk"], ["README.md", "yes", "missing run order"], ["data_sources.md", "yes", "authorization pending"], ["ai_use_statement.md", "partial", "prompt not recorded"], ["ppt_storyboard.md", "yes", "evidence notes incomplete"], ["core_figure", "yes", "caption overclaim"]],
    18: [["criterion", "score", "comment"], ["data_source", "18", "source and unit clear"], ["figure_expression", "20", "caption needs sample size"], ["evidence_boundary", "16", "no causal claim"], ["ai_use", "10", "prompt missing"], ["defense", "18", "answers are traceable"]],
}


def ensure_dirs() -> None:
    for folder in (
        CHAPTERS_DIR,
        ASSETS_DIR / "datasets",
        ASSETS_DIR / "code",
        ASSETS_DIR / "diagrams",
        ASSETS_DIR / "knowledge_graph",
    ):
        folder.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def write_code(spec: ChapterSpec) -> None:
    path = ASSETS_DIR / "code" / spec.code_name
    dataset_path = f"../datasets/{spec.dataset_name}"
    if spec.code_name.endswith(".R"):
        content = f"""# Week {spec.week:02d}: {spec.title}
# Teaching source code. It reads a small course dataset and prints a compact check.

data <- read.csv("{dataset_path}", stringsAsFactors = FALSE)
print(head(data))
print(summary(data))
"""
    else:
        content = f'''"""Week {spec.week:02d}: {spec.title}.

Small teaching script for checking the source-controlled dataset. It is not a
clinical or biological analysis workflow.
"""
from __future__ import annotations

import csv
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "datasets" / "{spec.dataset_name}"


def load_rows() -> list[dict[str, str]]:
    with DATA.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = load_rows()
    print(f"week={spec.week:02d}; rows={{len(rows)}}; columns={{list(rows[0]) if rows else []}}")
    for row in rows[:3]:
        print(row)


if __name__ == "__main__":
    main()
'''
    path.write_text(content, encoding="utf-8", newline="\n")


def write_diagram(spec: ChapterSpec) -> None:
    nodes = [part.strip() for part in spec.route.split("->")]
    lines = [
        "flowchart LR",
        f"    accTitle: Week {spec.week:02d} {spec.title}",
        f"    accDescr: {spec.route}。",
    ]
    for index, node in enumerate(nodes, start=1):
        lines.append(f'    n{index}["{node}"]')
    for index in range(1, len(nodes)):
        lines.append(f"    n{index} --> n{index + 1}")
    lines.extend(
        [
            '    ai["AI 审计"] -.-> n1',
            '    boundary["证据边界"] -.-> n' + str(len(nodes)),
        ]
    )
    (ASSETS_DIR / "diagrams" / spec.diagram_name).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def chapter_markdown(spec: ChapterSpec) -> str:
    concept_lines = "\n".join(f"- **{term}**：{desc}" for term, desc in spec.concepts)
    goal_lines = "\n".join(f"- {goal}" for goal in spec.goals)
    source_lines = "\n".join(f"- `{source}`" for source in spec.source_refs)
    return f"""---
type: textbook-chapter
chapter: {spec.week}
week: {spec.week}
title: {spec.title}
status: full_draft
textbook_status: full_draft
updated: 2026-06-04
audience: 药学本科生
chapter_source: course/textbook/chapters/chapter_{spec.week:02d}.md
asset_sources:
  - course/textbook/assets/datasets/{spec.dataset_name}
  - course/textbook/assets/code/{spec.code_name}
  - course/textbook/assets/diagrams/{spec.diagram_name}
---

# 第 {spec.week} 章 {spec.title}

## 本章导入

{spec.intro}

本章仍以课程周次事实文件为主线，所有示例均为教学模拟或课程化改写素材。它们用于训练数据结构、代码核验、图表表达和证据边界，不代表真实医学或生物学结论。

## 学习目标

{goal_lines}

## 核心概念

{concept_lines}

## 方法路线

本章路线可以概括为：**{spec.route}**。教师讲授时应先让学生确认输入数据和字段含义，再进入工具或图形解释。涉及统计、医学、基因功能或细胞注释时，结论必须降级为“观察”“候选解释”或“待核验点”。

```mermaid
{(ASSETS_DIR / "diagrams" / spec.diagram_name).read_text(encoding="utf-8").strip()}
```

## 工具实现与代码样例

本章配套小数据：`course/textbook/assets/datasets/{spec.dataset_name}`。

配套代码：`course/textbook/assets/code/{spec.code_name}`。代码只承担课堂核验和结构说明功能，不作为真实研究流程。学生应先读懂输入列，再运行或改写代码。

## 课堂案例

**案例名称：{spec.case_title}**

课堂使用步骤：

1. 先说明数据来源是教学模拟或课程化素材。
2. 让学生标出关键字段、观测单位和可能的质量风险。
3. 用配套代码或手算方式得到一个可复核结果。
4. 把结果写成克制表达，并列出仍需人工核验的项目。

## AI 协作与核验

推荐 Prompt：

```text
请检查我对“{spec.case_title}”的解释是否越过证据边界。
请只指出字段、方法、图表和待核验点中的遗漏，不要替我编造医学、统计、基因功能或细胞注释结论。
```

AI 可以用于解释术语、检查代码、改写图注和生成待核验清单；不能替代数据来源、统计前提、医学意义、基因功能、细胞注释或真实结果核验。

## 练习与参考答案要点

练习：{spec.exercise}

参考答案要点：{spec.answer}

## 来源与待核验点

主要来源：

{source_lines}

待核验点：

- 进入公开展示或 PPT 前，检查素材授权、字段含义、单位和图形参数。
- 若使用外部书籍、Notebook 或 PDF 中的图形，只记录来源，不直接复制图像进入教材正文。
- 若 AI 输出涉及机制、疗效、统计显著性、基因功能、通路或细胞类型，必须回到课程数据、数据库或人工审查记录核验。
"""


def write_chapters_and_assets() -> None:
    ensure_dirs()
    for spec in CHAPTERS:
        write_csv(ASSETS_DIR / "datasets" / spec.dataset_name, DATASETS[spec.week])
        write_code(spec)
        write_diagram(spec)
        (CHAPTERS_DIR / f"chapter_{spec.week:02d}.md").write_text(
            chapter_markdown(spec),
            encoding="utf-8",
            newline="\n",
        )


def write_knowledge_graph() -> None:
    edges_path = ASSETS_DIR / "knowledge_graph" / "course_graph_edges.csv"
    rows = [["source", "relation", "target", "note"]]
    for spec in CHAPTERS:
        week_node = f"Week {spec.week:02d}"
        chapter_node = f"Chapter {spec.week:02d}"
        rows.extend(
            [
                [week_node, "maps_to", chapter_node, spec.title],
                [chapter_node, "uses_dataset", f"Dataset {spec.week:02d}", spec.dataset_name],
                [chapter_node, "uses_code", f"Code {spec.week:02d}", spec.code_name],
                [chapter_node, "uses_diagram", f"Diagram {spec.week:02d}", spec.diagram_name],
                [chapter_node, "checks", "AI 协作边界", "AI assists but does not replace evidence review"],
            ]
        )
        for term, _desc in spec.concepts[:2]:
            rows.append([chapter_node, "teaches", term, "core concept"])
    write_csv(edges_path, rows)

    lines = [
        "flowchart TD",
        "    accTitle: AI Course Knowledge Graph",
        "    accDescr: 18 周课程、教材章节、素材资产与 AI 审计边界的关系图。",
        '    course["医药数据处理与可视化"]',
        '    ai["AI 协作边界"]',
        '    assets["教材资产包"]',
    ]
    for spec in CHAPTERS:
        lines.extend(
            [
                f'    w{spec.week:02d}["Week {spec.week:02d}<br/>{spec.title}"]',
                f'    c{spec.week:02d}["Chapter {spec.week:02d}"]',
                f'    d{spec.week:02d}["Dataset/Code/Diagram {spec.week:02d}"]',
                f"    course --> w{spec.week:02d}",
                f"    w{spec.week:02d} --> c{spec.week:02d}",
                f"    c{spec.week:02d} --> d{spec.week:02d}",
                f"    d{spec.week:02d} --> assets",
                f"    c{spec.week:02d} -.-> ai",
            ]
        )
    (ASSETS_DIR / "knowledge_graph" / "course_graph.mmd").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    write_chapters_and_assets()
    write_knowledge_graph()
    print(f"Generated {len(CHAPTERS)} textbook chapters and source asset sets under {TEXTBOOK.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
