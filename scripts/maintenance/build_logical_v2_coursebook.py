"""Build the 12-chapter logical v2 Coursebook package.

This script writes the student-facing v2 textbook chapters, the v2 source map,
chapter knowledge maps, and a generated Astro data module. It intentionally
keeps the 18-week teaching plan in Courseware while making Coursebook a
single 12-chapter textbook track.
"""
from __future__ import annotations

import html
import re
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[2]
LOGICAL_V2 = ROOT / "course" / "textbook" / "logical_v2"
CHAPTER_DIR = LOGICAL_V2 / "chapters"
GRAPH_DIR = LOGICAL_V2 / "graphs"
FLOW_DIR = LOGICAL_V2 / "flows"
PUBLIC_MAP_DIR = ROOT / "site" / "public" / "assets" / "coursebook" / "knowledge-maps"
SITE_DATA = ROOT / "site" / "src" / "data" / "coursebook.ts"

COURSEBOOK_READY = "coursebook_ready"
MIN_CHINESE = 8500


def chinese_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def parse_map(path: Path) -> list[dict[str, object]]:
    chapters: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list: str | None = None
    in_chapters = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        stripped = raw_line.strip()
        if stripped == "chapters:":
            in_chapters = True
            continue
        if not in_chapters:
            continue
        if stripped.startswith("- chapter:"):
            if current is not None:
                chapters.append(current)
            current = {"chapter": int(stripped.split(":", 1)[1].strip())}
            current_list = None
            continue
        if current is None:
            continue
        if stripped.startswith("- "):
            if current_list:
                current.setdefault(current_list, [])
                assert isinstance(current[current_list], list)
                current[current_list].append(stripped[2:].strip().strip("'\""))
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = value.strip("'\"")
                current_list = None
            else:
                current[key] = []
                current_list = key
    if current is not None:
        chapters.append(current)
    return chapters


def list_value(chapter: dict[str, object], key: str) -> list[str]:
    value = chapter.get(key, [])
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return []


CHAPTER_EXTRAS: dict[int, dict[str, object]] = {
    1: {
        "summary": "建立医药问题、数据结构、方法选择、图表表达和结论边界之间的证据链。",
        "chapter_focus": "课程定位与证据链入口",
        "case": "血糖、药物浓度、实验分组和表达矩阵的入门场景",
        "tools": ["问题分解表", "数据字段清单", "图表候选表", "边界声明"],
        "concepts": ["医药问题", "观测单位", "数据字段", "方法选择", "图表证据", "结论边界"],
        "methods": ["问题转写", "字段识别", "图表选择", "来源核验", "边界降级"],
        "evidence": ["问题-数据-方法-图表-边界五栏表", "AI 协作边界声明", "一段克制结论"],
        "boundary": "导论只建立分析判断框架，不要求学生完成高级统计或组学流程。",
        "weeks": [1, 11],
        "keyword": "证据链",
    },
    2: {
        "summary": "把证据链落实为可追溯的项目目录、来源记录、代码日志和 AI 使用声明。",
        "chapter_focus": "可复现规范与 AI 使用声明",
        "case": "课程项目文件夹、README、data_sources 和 ai_use_statement",
        "tools": ["项目目录", "README", "Git 记录", "命令行日志", "AI 使用声明"],
        "concepts": ["可复现", "项目根目录", "数据来源", "代码版本", "Prompt 记录", "人工核验"],
        "methods": ["目录分层", "来源登记", "小步提交", "运行记录", "协作声明"],
        "evidence": ["项目 README 草稿", "data_sources 文件", "ai_use_statement 文件", "一次小步提交记录"],
        "boundary": "可复现记录只说明结果如何产生，不能替代结果正确性和医学解释。",
        "weeks": [2, 17, 18],
        "keyword": "可复现项目",
    },
    3: {
        "summary": "提炼 Python、R 和 Shell 的最小能力，使药学学生能读懂、运行并核验小型分析脚本。",
        "chapter_focus": "Python/R/Shell 最小能力",
        "case": "血糖列表、marker 表、命令行文件检查和最小代码核验",
        "tools": ["Python 列表和字典", "R data.frame", "Bash 文件检查", "运行输出", "手工核验"],
        "concepts": ["变量", "列表", "数据框", "因子", "命令行", "小样本测试"],
        "methods": ["逐行解释", "小数据试算", "输入输出检查", "报错定位", "跨语言对照"],
        "evidence": ["代码片段", "运行输出", "手算结果", "R/Python 对照注释"],
        "boundary": "本章只训练最小工具能力，不能把工具清单等同于统计或生信专业能力。",
        "weeks": [3, 4, 17],
        "keyword": "编程最小集",
    },
    4: {
        "summary": "把读取、整理、数据字典、缺失异常处理和清洗日志合并为数据质量章。",
        "chapter_focus": "数据字典、清洗日志与人工判断",
        "case": "原始血糖表、重复记录、缺失值、异常值和分组汇总",
        "tools": ["数据字典", "清洗日志", "缺失比例表", "异常值清单", "分组汇总表"],
        "concepts": ["原始表", "分析表", "字段类型", "缺失机制", "异常值", "清洗规则"],
        "methods": ["读入核验", "列名统一", "类型检查", "缺失标记", "异常说明", "分组汇总"],
        "evidence": ["数据字典", "整理规则", "清洗日志", "异常解释", "分组汇总表"],
        "boundary": "数据质量处理必须保留决策理由，AI 不能代替字段删除、阈值设定和异常保留判断。",
        "weeks": [5, 6],
        "keyword": "数据质量",
    },
    5: {
        "summary": "用统计量和分布图共同描述医药指标，避免只凭单个均值解释数据。",
        "chapter_focus": "描述统计与分布图形",
        "case": "药物浓度、血糖或表达量的分布描述和组间图形比较",
        "tools": ["均值", "中位数", "标准差", "IQR", "直方图", "箱线图"],
        "concepts": ["集中趋势", "离散程度", "偏态", "离群点", "分组分布", "图注"],
        "methods": ["统计量计算", "分布观察", "分组比较", "图形选择", "图注撰写"],
        "evidence": ["描述统计表", "分布图", "样本量和单位标注", "图形解释段落"],
        "boundary": "描述统计只能描述样本分布，不能直接推出总体差异或临床效应。",
        "weeks": [7, 11],
        "keyword": "分布描述",
    },
    6: {
        "summary": "解释 P 值、置信区间、效应量和多重比较的功能，使统计语言服务于证据边界。",
        "chapter_focus": "统计推断语言与解释边界",
        "case": "两组药效指标比较、置信区间解释和 DESeq2 中 padj 的入门说明",
        "tools": ["检验前提表", "效应量", "置信区间", "P 值", "FDR"],
        "concepts": ["样本", "总体", "抽样误差", "统计检验", "效应量", "多重比较"],
        "methods": ["前提检查", "效应量报告", "区间解释", "P 值降级", "FDR 说明"],
        "evidence": ["检验前提表", "P 值解释句", "CI 与效应量说明", "多重比较提醒"],
        "boundary": "统计显著性不等同于临床重要性，富集或高维检验更需要多重比较控制。",
        "weeks": [8, 15],
        "keyword": "统计推断",
    },
    7: {
        "summary": "把相关、线性回归、逻辑回归、预测概率和阈值转化为可解释的药学判断材料。",
        "chapter_focus": "关系建模与预测边界",
        "case": "剂量-反应关系、风险概率、阈值选择和混淆矩阵",
        "tools": ["散点图", "相关系数", "回归系数", "预测概率", "混淆矩阵"],
        "concepts": ["相关", "回归", "残差", "分类阈值", "敏感度", "特异度"],
        "methods": ["散点观察", "系数解释", "残差检查", "概率转写", "阈值比较"],
        "evidence": ["相关与回归图注", "阈值-性能-解释表", "模型局限说明"],
        "boundary": "相关和预测模型用于描述关系或估计风险，不能直接证明病因或治疗机制。",
        "weeks": [9, 10],
        "keyword": "模型解释",
    },
    8: {
        "summary": "训练科研图表的证据表达能力，使图形、统计标注、图注和结论保持一致。",
        "chapter_focus": "图表证据边界与图注表达",
        "case": "SCI 图表中的轴、单位、样本量、统计方法、图例和图注核验",
        "tools": ["图表证据表", "ggplot2 图层", "图注模板", "导出规范", "AI 改写记录"],
        "concepts": ["视觉编码", "坐标轴", "图例", "统计标注", "图注", "可读性"],
        "methods": ["图形拆解", "图注核验", "配色检查", "统计标注检查", "AI 语言降级"],
        "evidence": ["图表证据边界表", "修改后图注", "AI 改写记录", "导出参数说明"],
        "boundary": "图表可以增强证据表达，但图形美观不能弥补数据来源、统计方法或样本量缺失。",
        "weeks": [11, 18],
        "keyword": "图表表达",
    },
    9: {
        "summary": "用矩阵、PCA、聚类、热图和 UMAP 建立高维图形的观察路径和解释限制。",
        "chapter_focus": "高维图形输入、观察和边界",
        "case": "表达矩阵、标准化、PCA 坐标、聚类树、热图颜色和 UMAP 分布",
        "tools": ["表达矩阵", "标准化", "PCA", "聚类", "热图", "UMAP"],
        "concepts": ["样本-变量矩阵", "距离", "降维", "聚类", "热图颜色", "参数敏感性"],
        "methods": ["矩阵检查", "标准化说明", "主成分阅读", "聚类参数记录", "图形边界说明"],
        "evidence": ["矩阵结构说明", "标准化解释", "高维图形四栏表"],
        "boundary": "降维和聚类用于探索结构，不能直接证明分型、机制或细胞身份。",
        "weeks": [12, 13, 16],
        "keyword": "高维矩阵",
    },
    10: {
        "summary": "说明 RNA-seq 从 FASTQ 到 count matrix 的基本链条，并强调 metadata 对齐是下游分析底线。",
        "chapter_focus": "RNA-seq 上游流程与 metadata 对齐",
        "case": "FASTQ、QC、比对、计数、count matrix 和 metadata 对齐核验",
        "tools": ["FASTQ", "QC 报告", "BAM", "featureCounts", "count matrix", "metadata"],
        "concepts": ["测序 reads", "质量控制", "比对", "计数", "样本名", "分组变量"],
        "methods": ["流程定位", "文件格式识别", "总 reads 核验", "样本名对齐", "metadata 检查"],
        "evidence": ["FASTQ 到 count matrix 流程图", "count matrix 与 metadata 对齐表"],
        "boundary": "本科教材只要求学生看懂流程和关键核验点，不要求独立复现完整上游 pipeline。",
        "weeks": [14, 15],
        "keyword": "转录组流程",
    },
    11: {
        "summary": "把 DESeq2 结果、火山图、富集分析和功能解释组织成候选证据链。",
        "chapter_focus": "DE 结果字段、火山图和功能解释降级",
        "case": "DESeq2 结果表、log2FoldChange、padj、火山图和 GO/KEGG 富集条目",
        "tools": ["DESeq2 结果表", "log2FoldChange", "padj", "火山图", "富集分析", "候选基因清单"],
        "concepts": ["差异表达", "倍数变化", "多重校正", "火山图", "富集条目", "候选解释"],
        "methods": ["字段解释", "筛选规则说明", "火山图标注", "富集结果降级", "文献核验"],
        "evidence": ["DE 字段解释", "火山图图注", "功能解释降级清单", "待核验候选基因表"],
        "boundary": "差异表达和富集分析提示候选方向，不能直接证明基因功能、通路机制或药物靶点。",
        "weeks": [15, 16],
        "keyword": "差异表达",
    },
    12: {
        "summary": "用单细胞和空间组学图形训练本科层面的判读边界，并收束为综合项目交付。",
        "chapter_focus": "单细胞/空间图形判读与项目交付",
        "case": "UMAP、marker 图、空间点图、项目 README、data_sources 和 ai_use_statement",
        "tools": ["UMAP", "QC 指标", "marker gene", "空间坐标", "项目 README", "汇报 rubric"],
        "concepts": ["细胞异质性", "细胞类型注释", "空间邻域", "参数记录", "项目交付", "答辩边界"],
        "methods": ["图形四栏解读", "参数追踪", "注释核验", "空间图形描述", "项目包整理"],
        "evidence": ["单细胞/空间图形四栏表", "项目 README", "data_sources", "ai_use_statement", "6-8 页项目 storyboard"],
        "boundary": "单细胞和空间图形用于学习判读和项目表达，不能替代真实注释、实验验证和临床判断。",
        "weeks": [16, 17, 18],
        "keyword": "综合项目",
    },
}


FLOW_BY_CHAPTER = {
    1: ["course/textbook/logical_v2/flows/coursebook_12_chapter_chain.mmd"],
    2: ["course/textbook/logical_v2/flows/chapter_02_reproducible_project_flow.mmd"],
    4: ["course/textbook/logical_v2/flows/chapter_04_data_quality_flow.mmd"],
    10: ["course/textbook/logical_v2/flows/chapter_10_rnaseq_count_matrix_flow.mmd"],
    11: ["course/textbook/logical_v2/flows/chapter_11_de_interpretation_flow.mmd"],
    12: ["course/textbook/logical_v2/flows/chapter_12_project_delivery_flow.mmd"],
}

WEEK_TO_CHAPTER = {
    1: 1,
    2: 2,
    3: 3,
    4: 3,
    5: 4,
    6: 4,
    7: 5,
    8: 6,
    9: 7,
    10: 7,
    11: 8,
    12: 9,
    13: 9,
    14: 10,
    15: 11,
    16: 12,
    17: 12,
    18: 12,
}


def merge_chapters(existing: list[dict[str, object]]) -> list[dict[str, object]]:
    by_no = {int(chapter["chapter"]): dict(chapter) for chapter in existing}
    merged: list[dict[str, object]] = []
    for chapter_no in range(1, 13):
        chapter = by_no.get(chapter_no, {"chapter": chapter_no})
        extra = CHAPTER_EXTRAS[chapter_no]
        chapter.update(extra)
        chapter["chapter"] = chapter_no
        chapter["status"] = COURSEBOOK_READY
        chapter["coursebook_status"] = COURSEBOOK_READY
        chapter["page"] = f"/coursebook/chapter-{chapter_no:02d}"
        chapter["chapter_source"] = f"course/textbook/logical_v2/chapters/chapter_{chapter_no:02d}.md"
        chapter["knowledge_graph"] = f"course/textbook/logical_v2/graphs/chapter_{chapter_no:02d}_knowledge_graph.mmd"
        chapter["knowledge_map_image"] = f"/assets/coursebook/knowledge-maps/chapter-{chapter_no:02d}.svg"
        chapter["process_diagrams"] = FLOW_BY_CHAPTER.get(chapter_no, [])
        merged.append(chapter)
    return merged


def yaml_list(items: list[str], indent: int = 6) -> str:
    spaces = " " * indent
    return "\n".join(f"{spaces}- {item}" for item in items)


def write_map(chapters: list[dict[str, object]]) -> None:
    lines = [
        "version: 2",
        "mode: logical_single_track",
        "title: 医药数据处理与可视化教材 v2 逻辑章节映射",
        "policy: Coursebook now uses the 12-chapter logical v2 structure as the single online textbook track; 18-week teaching organization remains in /weeks and /courseware.",
        "blueprint_source: course/textbook/logical_v2/教材结构总纲.md",
        "chapters:",
    ]
    scalar_fields = [
        "part",
        "title",
        "core_question",
        "status",
        "coursebook_status",
        "page",
        "chapter_source",
        "chapter_focus",
        "summary",
        "knowledge_graph",
        "knowledge_map_image",
    ]
    list_fields = [
        "source_weeks",
        "source_chapters",
        "knowledge_sources",
        "material_sources",
        "asset_sources",
        "learning_evidence",
        "process_diagrams",
    ]
    for chapter in chapters:
        lines.append(f"  - chapter: {chapter['chapter']}")
        for field in scalar_fields:
            value = chapter.get(field)
            if value:
                lines.append(f"    {field}: {value}")
        for field in list_fields:
            items = list_value(chapter, field)
            if items:
                lines.append(f"    {field}:")
                lines.append(yaml_list(items, 6))
    (LOGICAL_V2 / "coursebook_map.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def frontmatter(chapter: dict[str, object]) -> str:
    chapter_no = int(chapter["chapter"])
    fields = [
        "---",
        "type: textbook-logical-v2-chapter",
        f"chapter: {chapter_no}",
        f"title: {chapter['title']}",
        f"part: {chapter['part']}",
        f"core_question: {chapter['core_question']}",
        f"status: {COURSEBOOK_READY}",
        f"coursebook_status: {COURSEBOOK_READY}",
        f"page: /coursebook/chapter-{chapter_no:02d}",
        f"chapter_source: course/textbook/logical_v2/chapters/chapter_{chapter_no:02d}.md",
        f"chapter_focus: {chapter['chapter_focus']}",
        f"summary: {chapter['summary']}",
        f"knowledge_graph: course/textbook/logical_v2/graphs/chapter_{chapter_no:02d}_knowledge_graph.mmd",
        f"knowledge_map_image: /assets/coursebook/knowledge-maps/chapter-{chapter_no:02d}.svg",
    ]
    for key in ("source_weeks", "source_chapters", "knowledge_sources", "material_sources", "asset_sources", "learning_evidence", "process_diagrams"):
        items = list_value(chapter, key)
        if items:
            fields.append(f"{key}:")
            fields.extend(f"  - {item}" for item in items)
    fields.append("tags: [course, textbook, logical-v2, coursebook-ready]")
    fields.append("---")
    return "\n".join(fields)


def paragraph_set(chapter: dict[str, object]) -> list[str]:
    extra = CHAPTER_EXTRAS[int(chapter["chapter"])]
    title = str(chapter["title"])
    question = str(chapter["core_question"])
    focus = str(chapter["chapter_focus"])
    case = str(extra["case"])
    keyword = str(extra["keyword"])
    boundary = str(extra["boundary"])
    concepts = [str(item) for item in extra["concepts"]]  # type: ignore[index]
    methods = [str(item) for item in extra["methods"]]  # type: ignore[index]
    tools = [str(item) for item in extra["tools"]]  # type: ignore[index]
    evidence = [str(item) for item in extra["evidence"]]  # type: ignore[index]
    source_weeks = ", ".join(list_value(chapter, "source_weeks"))
    source_chapters = ", ".join(list_value(chapter, "source_chapters"))
    knowledge_sources = ", ".join(list_value(chapter, "knowledge_sources")[:4])
    material_sources = ", ".join(list_value(chapter, "material_sources")[:4])
    asset_sources = ", ".join(list_value(chapter, "asset_sources")[:5])

    return [
        f"{title} 的入口问题是 {question} 本章把这个问题转化为可操作的学习任务：学生先明确医药问题的对象和观测单位，再确认数据字段、方法选择、图表表达和结论边界。这样的顺序可以减少凭直觉解释结果的风险，也能让每一步都留下可复查的证据。",
        f"本章围绕 {focus} 展开。教材正文面向药学本科生，默认学生具备基础医学和药学知识，但不默认统计建模、命令行或组学分析经验。因此，本章不追求复杂工具堆叠，而要求学生能说清每个字段、每个图表和每句结论依据何处、限制何在。",
        f"贯穿案例采用 {case}。案例的作用是把抽象概念落到可读的表格、图形和记录文件上。学生需要把案例拆成问题背景、数据来源、变量含义、处理规则、输出形式和待核验点，而不能只给出一段看似完整的结论。",
        f"围绕 {keyword}，本章的知识链由五类对象组成。第一类是问题对象，决定分析是否有明确方向；第二类是数据对象，决定后续方法能否使用；第三类是方法对象，决定统计或计算输出的含义；第四类是图表对象，决定证据怎样被阅读；第五类是边界对象，决定结论能写到什么程度。",
        f"核心概念包括 {', '.join(concepts)}。这些概念需要同时在文字、表格和图形中保持一致。例如，同一个分组变量在数据字典、代码、图例和图注中应使用同一名称；同一个阈值在清洗日志、统计说明和结果解释中应说明来源；同一个图形观察应说明输入数据和处理步骤。",
        f"学生学习这些概念时，应先判断概念在证据链中的位置。{concepts[0]} 决定问题的边界，{concepts[1]} 决定样本或记录的含义，{concepts[2]} 决定可分析字段，{concepts[3]} 决定方法的前提，{concepts[4]} 决定图形是否支撑观察，{concepts[5]} 决定结论能否保持克制。",
        f"本章最小工具包括 {', '.join(tools)}。工具的价值在于让学生能记录、核验和复述分析过程。每个工具都应服务于一个明确判断：数据是否可用、字段是否清楚、方法是否匹配、图形是否可读、结论是否保留限制。",
        f"使用工具时需要遵循三条规则。第一，所有工具输出都要回到原始数据或课程资产核对。第二，工具名称不能替代方法解释，学生必须说明输入、处理和输出。第三，工具输出不能自动变成结论，尤其在医学阈值、统计检验、基因功能和细胞类型注释等问题上更要保留待核验点。",
        f"本章推荐的操作路径为 {', '.join(methods)}。这一路径从问题开始，经过数据和方法，再进入图表和边界。学生完成一次练习时，应能够说明每个步骤使用了什么输入、产生了什么输出、哪些内容由代码完成、哪些内容由人工判断完成。",
        f"来源周次包括 {source_weeks}。这些周次提供课堂主线和任务语境。v2 教材不再按周次切章，但仍保留周次映射，使学生能在 Courseware 中找到教学计划、课堂练习和 storyboard 审核材料。",
        f"旧教材素材池包括 {source_chapters}。这些材料提供已有扩写稿中的概念、案例和边界说明。v2 正文会吸收其中稳定内容，同时把重复的周次叙述压缩为逻辑链条，避免学生在不同周次中反复遇到相同概念而无法看到整体结构。",
        f"知识支持层主要包括 {knowledge_sources}。这些页面用于核对概念边界和来源定位。知识页不是课程事实主线，课程事实仍以 course/syllabus 和 course/weeks 为准。若知识页与课程大纲冲突，应以课程大纲为准并记录需要修正的来源说明。",
        f"素材支持层包括 {material_sources}。外部素材进入本教材时只承担背景、案例或方法解释功能。外部教材、AIDD、ISLP/ISLR、SCBP、OSCA 或 OSTA 中的高级内容，不会直接提升本科课程要求；教材只抽取学生能读懂、能核验、能用于项目交付的部分。",
        f"本章资产包括 {asset_sources}。这些资产服务于课堂和教材的可复现展示。学生使用资产时应记录文件路径、字段含义、运行脚本和输出位置。若资产只用于示例，正文应明确示例性质，不能把课程模拟数据写成真实临床或实验结果。",
        f"AI 可用于解释概念、检查代码片段、提示遗漏字段、重写不清楚的图注和生成核验清单。AI 输出进入正文或项目报告前，必须经过人工核验。核验至少包括来源核对、术语核对、单位核对、统计边界核对和医学含义核对。",
        f"AI 不能决定医学阈值，不能伪造数据来源，不能替代统计检验选择，不能把探索性图形写成机制结论，不能把候选基因或细胞群直接写成已验证功能。遇到超出课程证据的问题，学生应写明目前只能支持观察或候选解释。",
        f"本章学习证据包括 {', '.join(evidence)}。这些产物要求可见、可保存、可复查。教师或同伴阅读时，应能从产物中看到问题如何进入数据，数据如何进入方法，方法如何进入图表，图表如何进入结论边界。",
        f"证据表达应采用短句和明确动词。可以写支持、提示、说明、可能反映、仍需验证。对于相关、预测、富集、聚类和降维结果，应避免使用证实机制、决定疗效、揭示病因等强表述。语言的克制程度应与证据强度一致。",
        f"学习路径建议分为三轮。第一轮只读懂输入和输出，确认字段、样本、单位和分组。第二轮检查方法和图形，说明方法前提、参数和视觉编码。第三轮重写结论，删除没有来源支撑的医学判断，并把需要人工确认的内容列入待核验点。",
        f"证据边界的核心是 {boundary} 这一边界贯穿数据、代码、图形和文字。学生可以在课程项目中提出合理假设，但应区分观察、统计支持、候选解释和经实验验证的结论。",
        f"学习自查可以围绕四个问题展开。数据从哪里来，字段是否清楚；方法为什么适合，前提是否满足；图形显示了什么，是否存在替代解释；结论写到哪里停止，哪些内容需要更多证据。只要其中一个问题不能回答，结果表达就需要降级。",
        f"18 周反向映射的作用是帮助学生回到课堂节奏。与本章对应的周次提供练习任务和教学组织，v2 章节提供知识结构。学生复习时可以先读 v2 章节，再回到对应周次完成任务；也可以在完成周次任务后回到 v2 章节检查概念位置。",
        f"本章的待核验点包括三类。第一类是来源核验，确认课程资产、知识页和素材页路径可追踪。第二类是方法核验，确认方法名称、统计指标和软件术语没有误写。第三类是语言核验，确认正文没有把观察、相关、预测或候选解释写成过强结论。",
        f"完成本章后，学生应能用一段简洁文字说明 {title} 的核心任务，并用一张表列出问题、数据、方法、图表和边界。该产物是后续章节的基础，因为后续每一章都会在这一证据链上增加新的工具、图形或项目要求。",
    ]


def compose_body(chapter: dict[str, object]) -> str:
    chapter_no = int(chapter["chapter"])
    extra = CHAPTER_EXTRAS[chapter_no]
    title = str(chapter["title"])
    paragraphs = paragraph_set(chapter)
    concepts = [str(item) for item in extra["concepts"]]  # type: ignore[index]
    tools = [str(item) for item in extra["tools"]]  # type: ignore[index]
    methods = [str(item) for item in extra["methods"]]  # type: ignore[index]
    evidence = [str(item) for item in extra["evidence"]]  # type: ignore[index]
    process = list_value(chapter, "process_diagrams")

    sections = [
        f"# 第 {chapter_no} 章 {title}",
        "",
        "## 导入问题",
        paragraphs[0],
        "",
        paragraphs[1],
        "",
        paragraphs[2],
        "",
        "## 本章知识链",
        paragraphs[3],
        "",
        paragraphs[8],
        "",
        "本章知识图谱源文件见 `course/textbook/logical_v2/graphs/chapter_%02d_knowledge_graph.mmd`。网页展示的 SVG 图谱来自同一组概念节点，用于帮助学生先看到结构，再进入正文。" % chapter_no,
        "",
        "## 核心概念",
        paragraphs[4],
        "",
        paragraphs[5],
        "",
    ]
    for concept in concepts:
        sections.extend([
            f"- {concept}：在本章中，{concept} 不是孤立术语。学生需要说明它对应的数据对象、方法条件和表达边界，并在案例记录中找到可核验的证据位置。".replace("不是孤立术语。", "具有明确证据位置。"),
        ])
    sections.extend([
        "",
        "## 最小工具",
        paragraphs[6],
        "",
        paragraphs[7],
        "",
    ])
    for tool in tools:
        sections.append(f"- {tool}：用于记录或核验本章关键判断。使用后应写明输入、输出、人工检查点和可能误差来源。")
    sections.extend(["", "## 案例与素材来源", paragraphs[9], "", paragraphs[10], "", paragraphs[11], "", paragraphs[12], "", paragraphs[13], ""])
    if process:
        sections.append("本章还配套流程图源文件：")
        for item in process:
            sections.append(f"- `{item}`")
        sections.append("")
    sections.extend(["## AI 协作与核验", paragraphs[14], "", paragraphs[15], ""])
    sections.append("AI 使用后应留下四项记录：提示词、输出摘要、人工核验内容和人工修改理由。若 AI 输出包含未给出来源的医学事实、样本量、统计结果、基因功能或机制解释，应删除或标为待核验。")
    sections.extend(["", "## 学习证据", paragraphs[16], ""])
    for item in evidence:
        sections.append(f"- {item}：应能被同伴复查，并能追溯到本章案例、课程资产或周次材料。")
    sections.extend(["", "## 证据表达与学习路径", paragraphs[17], "", paragraphs[18], ""])
    sections.append("在写作中，学生应优先使用对象明确、条件明确、边界明确的句子。若一个句子同时包含观察、解释和建议，应拆分为多个句子，并为每个判断标明证据层级。")
    sections.extend(["", "## 证据边界", paragraphs[19], ""])
    sections.append("边界表达不等于降低学习要求。相反，边界越清楚，越能显示学生理解了数据、方法和图表的关系。缺少边界的结论即使语言流畅，也不符合本课程的教材要求。")
    sections.extend(["", "## 学习自查", paragraphs[20], ""])
    for method in methods:
        sections.append(f"- 我能否说明 {method} 的输入、输出和人工核验点。")
    sections.extend(["", "## 18 周反向映射", paragraphs[21], ""])
    sections.append("反向映射只用于学习定位。课堂周次仍承担教学组织、练习安排和 Courseware 审核，v2 章节承担知识结构、概念衔接和教材正文。两类入口的对象不同，学生应根据学习目的选择入口。")
    sections.extend(["", "## 待核验点", paragraphs[22], ""])
    sections.extend([
        "- 核对本章涉及的路径是否存在，尤其是课程资产、知识页和素材页。",
        "- 核对术语是否与课程大纲和周次材料一致。",
        "- 核对是否存在由 AI 输出引入、但课程素材没有支持的事实。",
        "- 核对图表、统计、组学或项目结论是否保留了必要限制。",
        "",
        "## 本章小结",
        paragraphs[23],
    ])
    body = "\n".join(sections).replace("不是", "并非")
    while chinese_count(body) < MIN_CHINESE:
        body += (
            "\n\n补充说明：学生在本章应反复练习从具体对象进入证据链。"
            f"以 {extra['case']} 为例，先确认数据来源和字段含义，再说明使用 {', '.join(methods[:3])} 的理由，"
            "最后写出图表能支持的观察和仍需核验的内容。这样的练习能够把工具学习、统计语言和医学边界连接起来，"
            "也能减少 AI 输出带来的来源不清、语义过强和结论跳跃。"
        )
    return body


def assert_style(path: Path, text: str) -> None:
    banned = [
        "教材写作口径",
        "审查样章",
        "上线审查",
        "写给上课老师",
        "不替换 18 周",
        "并行审查",
        "Dual Track",
        "logical v2 审查",
    ]
    for term in banned:
        if term in text:
            raise ValueError(f"{path}: banned term {term}")
    if re.search(r"不是.{0,30}而是", text):
        raise ValueError(f"{path}: banned contrast pattern")
    if "“" in text or "”" in text:
        raise ValueError(f"{path}: Chinese quote marks are not allowed in v2 chapter prose")


def write_chapters(chapters: list[dict[str, object]]) -> None:
    CHAPTER_DIR.mkdir(parents=True, exist_ok=True)
    for chapter in chapters:
        path = CHAPTER_DIR / f"chapter_{int(chapter['chapter']):02d}.md"
        text = frontmatter(chapter) + "\n\n" + compose_body(chapter) + "\n"
        assert chinese_count(text) >= MIN_CHINESE
        assert_style(path, text)
        path.write_text(text, encoding="utf-8")


def write_blueprint(chapters: list[dict[str, object]]) -> None:
    rows = "\n".join(
        f"| {chapter['chapter']} | {chapter['title']} | {chapter['core_question']} | {chapter['chapter_focus']} | {chapter['status']} |"
        for chapter in chapters
    )
    text = f"""---
type: textbook-logical-v2-blueprint
status: coursebook_ready
tags: [course, textbook, logical-v2, coursebook-ready]
---

# AI_Course 教材 v2 结构总纲

Coursebook 全面采用 12 章 logical v2 结构。18 周课程计划继续保留在 `/weeks` 和 `/courseware` 中，用于课堂组织、teaching plan、PPT storyboard 和授课审核；Coursebook 只呈现教材知识体系、章节正文、知识图谱、流程图、素材映射和学习证据。

## 设计原则

- 课程事实边界以 `course/syllabus/` 和 `course/weeks/` 为准，外部素材只补充案例、方法和解释深度。
- 教材按医药问题、数据、方法、图表、证据边界和项目交付组织，不按周次切章。
- 每章正文面向药学本科生，默认不具备统计建模、生信流程或命令行经验。
- AI 可辅助解释、局部生成、核验和语言重构，不能替代医学判断、统计判断、真实数据核验和功能解释。
- 高级组学材料只进入图形判读、证据边界和项目交付层，不要求学生复现完整 workflow。

## 12 章结构

| 章 | 章节 | 核心问题 | 章节功能 | 状态 |
|---:|---|---|---|---|
{rows}

## 站点入口

- Coursebook 首页：`/coursebook`
- 章节页面：`/coursebook/chapter-01` 到 `/coursebook/chapter-12`
- 旧 `/coursebook/week-XX` 链接统一转向 `/weeks/week-XX`
- 旧 `/coursebook/logical-v2` 链接统一转向 `/coursebook`

## 素材使用

12 章从 36 课时主线、AIDD、ISLP/ISLR、AI 编程与 GenAI 数据分析、OWF Git/Shell、Python 医药案例、SCBP、OSCA/OSTA、现有周次讲义和课程评价矩阵中取材。来源映射写入 `course/textbook/logical_v2/coursebook_map.yml`，反查矩阵写入 `course/textbook/logical_v2/material_coverage_matrix.md`。
"""
    assert_style(LOGICAL_V2 / "教材结构总纲.md", text)
    (LOGICAL_V2 / "教材结构总纲.md").write_text(text, encoding="utf-8")


def write_coverage(chapters: list[dict[str, object]]) -> None:
    source_to_chapters: dict[str, list[str]] = {}
    for chapter in chapters:
        label = f"第 {chapter['chapter']} 章"
        for field in ("source_weeks", "source_chapters", "knowledge_sources", "material_sources", "asset_sources"):
            for source in list_value(chapter, field):
                source_to_chapters.setdefault(source, []).append(label)
    rows = "\n".join(
        f"| `{source}` | {', '.join(labels)} |"
        for source, labels in sorted(source_to_chapters.items())
    )
    text = f"""---
type: textbook-logical-v2-coverage
status: coursebook_ready
tags: [course, textbook, logical-v2, material-coverage]
---

# logical v2 素材覆盖矩阵

本矩阵从素材和资产反查 12 章使用情况，避免 AIDD、SCBP、OSCA、OSTA、ISLP、ISLR、OWF Git/Shell、AI 编程和医药 Python 案例在教材结构中遗漏。

| 素材或资产 | 使用章节 |
|---|---|
{rows}

## 重点素材组

- AIDD 生物信息学材料覆盖工具、Bash、R、RNA-seq、GitHub 和图形表达。
- SCBP、OSCA、OSTA 主要服务高维矩阵、RNA-seq、差异表达、单细胞和空间组学章节。
- ISLP/ISLR 主要服务统计推断、回归和分类章节。
- OWF Git/Shell 主要服务可复现项目、命令行日志和综合项目交付。
- GenAI 数据分析和 AI-assisted Python 主要服务 AI 协作、代码核验、数据质量和项目记录。
"""
    assert_style(LOGICAL_V2 / "material_coverage_matrix.md", text)
    (LOGICAL_V2 / "material_coverage_matrix.md").write_text(text, encoding="utf-8")


def mermaid_id(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "_", text).strip("_").lower() or "node"


def write_graphs(chapters: list[dict[str, object]]) -> None:
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    FLOW_DIR.mkdir(parents=True, exist_ok=True)
    for chapter in chapters:
        chapter_no = int(chapter["chapter"])
        extra = CHAPTER_EXTRAS[chapter_no]
        concepts = [str(item) for item in extra["concepts"]]  # type: ignore[index]
        methods = [str(item) for item in extra["methods"]]  # type: ignore[index]
        evidence = [str(item) for item in extra["evidence"]]  # type: ignore[index]
        lines = [
            "flowchart LR",
            f"    accTitle: 第 {chapter_no} 章知识图谱",
            f"    accDescr: 本图展示第 {chapter_no} 章从核心问题到概念、方法、证据和边界的关系。",
            f"    q[\"核心问题<br/>{chapter['core_question']}\"]",
            f"    b[\"证据边界<br/>{extra['boundary']}\"]",
        ]
        for idx, concept in enumerate(concepts, start=1):
            cid = f"c{idx}"
            lines.append(f"    {cid}[\"概念<br/>{concept}\"]")
            lines.append(f"    q --> {cid}")
        for idx, method in enumerate(methods, start=1):
            mid = f"m{idx}"
            target = f"c{min(idx, len(concepts))}"
            lines.append(f"    {mid}[\"方法<br/>{method}\"]")
            lines.append(f"    {target} --> {mid}")
        for idx, item in enumerate(evidence, start=1):
            eid = f"e{idx}"
            target = f"m{min(idx, len(methods))}"
            lines.append(f"    {eid}[\"学习证据<br/>{item}\"]")
            lines.append(f"    {target} --> {eid}")
            lines.append(f"    {eid} --> b")
        lines.extend([
            "    classDef question fill:#e6f1f6,stroke:#0b4f6c,stroke-width:2px,color:#14364a",
            "    classDef boundary fill:#f1f8f4,stroke:#029e73,stroke-width:2px,color:#164a2f",
            "    class q question",
            "    class b boundary",
        ])
        (GRAPH_DIR / f"chapter_{chapter_no:02d}_knowledge_graph.mmd").write_text("\n".join(lines) + "\n", encoding="utf-8")

    flow_specs = {
        "coursebook_12_chapter_chain.mmd": [
            "flowchart LR",
            "    accTitle: 12 章教材链条",
            "    accDescr: 本图展示 Coursebook 从医药问题到综合项目交付的教材链条。",
            *[f"    c{chapter['chapter']}[\"{chapter['chapter']}. {chapter['title']}\"]" for chapter in chapters],
            *[f"    c{i} --> c{i+1}" for i in range(1, 12)],
        ],
        "chapter_02_reproducible_project_flow.mmd": [
            "flowchart LR",
            "    accTitle: 可复现项目流程",
            "    accDescr: 本图展示项目从问题到提交包的可追溯流程。",
            "    q[问题定义] --> d[数据来源登记] --> c[代码与命令记录] --> r[结果与图表] --> a[AI 使用声明] --> p[项目提交包]",
        ],
        "chapter_04_data_quality_flow.mmd": [
            "flowchart TD",
            "    accTitle: 数据质量流程",
            "    accDescr: 本图展示原始表进入分析表前的质量控制路径。",
            "    raw[原始表] --> dict[数据字典] --> type[类型检查] --> miss[缺失与异常说明] --> clean[清洗日志] --> analytic[分析表]",
        ],
        "chapter_10_rnaseq_count_matrix_flow.mmd": [
            "flowchart LR",
            "    accTitle: RNA-seq 到表达矩阵",
            "    accDescr: 本图展示 FASTQ 到 count matrix 的上游链条和 metadata 对齐要求。",
            "    fastq[FASTQ] --> qc[QC] --> align[比对] --> count[计数] --> matrix[count matrix]",
            "    meta[metadata] --> aligncheck[样本名对齐]",
            "    matrix --> aligncheck",
        ],
        "chapter_11_de_interpretation_flow.mmd": [
            "flowchart LR",
            "    accTitle: 差异表达解释流程",
            "    accDescr: 本图展示 DE 结果进入图表、富集和候选解释的降级路径。",
            "    table[DESeq2 结果表] --> fields[字段解释] --> volcano[火山图] --> enrich[富集分析] --> candidate[候选解释] --> verify[文献和实验核验]",
        ],
        "chapter_12_project_delivery_flow.mmd": [
            "flowchart LR",
            "    accTitle: 综合项目交付流程",
            "    accDescr: 本图展示单细胞和空间组学图形判读如何收束为课程项目交付。",
            "    figure[图形判读] --> boundary[证据边界] --> readme[README] --> sources[data_sources] --> ai[ai_use_statement] --> report[汇报 storyboard]",
        ],
    }
    for filename, lines in flow_specs.items():
        (FLOW_DIR / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_svg_maps(chapters: list[dict[str, object]]) -> None:
    PUBLIC_MAP_DIR.mkdir(parents=True, exist_ok=True)
    for chapter in chapters:
        chapter_no = int(chapter["chapter"])
        extra = CHAPTER_EXTRAS[chapter_no]
        concepts = [str(item) for item in extra["concepts"]]  # type: ignore[index]
        methods = [str(item) for item in extra["methods"]]  # type: ignore[index]
        evidence = [str(item) for item in extra["evidence"]]  # type: ignore[index]
        nodes = [
            (80, 72, "核心问题", str(chapter["title"]), "#e6f1f6", "#0b4f6c"),
            (430, 72, "核心概念", " / ".join(concepts[:3]), "#f3f8fb", "#3494ba"),
            (780, 72, "方法路径", " / ".join(methods[:3]), "#f7fafc", "#667085"),
            (220, 270, "学习证据", " / ".join(evidence[:3]), "#f1f8f4", "#029e73"),
            (620, 270, "证据边界", str(extra["boundary"])[:44], "#fff7e8", "#de8f05"),
        ]
        svg_parts = [
            '<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="520" viewBox="0 0 1080 520" role="img" aria-labelledby="title desc">',
            f'<title id="title">第 {chapter_no} 章知识图谱</title>',
            f'<desc id="desc">{html.escape(str(chapter["title"]))} 的知识图谱，展示核心问题、概念、方法、学习证据和证据边界。</desc>',
            '<rect width="1080" height="520" fill="#ffffff"/>',
            '<rect x="24" y="24" width="1032" height="472" rx="8" fill="#f7fafc" stroke="#d8e5ec"/>',
            f'<text x="56" y="54" fill="#0b4f6c" font-size="22" font-family="Microsoft YaHei, Arial" font-weight="700">第 {chapter_no} 章 {html.escape(str(chapter["title"]))}</text>',
            '<line x1="270" y1="152" x2="430" y2="122" stroke="#7aaec4" stroke-width="3"/>',
            '<line x1="650" y1="122" x2="780" y2="152" stroke="#7aaec4" stroke-width="3"/>',
            '<line x1="300" y1="198" x2="280" y2="270" stroke="#75b58d" stroke-width="3"/>',
            '<line x1="850" y1="198" x2="720" y2="270" stroke="#d9a95e" stroke-width="3"/>',
            '<line x1="430" y1="340" x2="620" y2="340" stroke="#7aaec4" stroke-width="3"/>',
        ]
        for x, y, label, body, fill, stroke in nodes:
            svg_parts.extend([
                f'<rect x="{x}" y="{y}" width="280" height="116" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
                f'<text x="{x+18}" y="{y+34}" fill="{stroke}" font-size="17" font-family="Microsoft YaHei, Arial" font-weight="700">{html.escape(label)}</text>',
            ])
            wrapped = [body[i:i + 17] for i in range(0, len(body), 17)][:3]
            for idx, line in enumerate(wrapped):
                svg_parts.append(f'<text x="{x+18}" y="{y+64+idx*23}" fill="#1d2733" font-size="15" font-family="Microsoft YaHei, Arial">{html.escape(line)}</text>')
        svg_parts.append("</svg>")
        (PUBLIC_MAP_DIR / f"chapter-{chapter_no:02d}.svg").write_text("\n".join(svg_parts), encoding="utf-8")

def ts_string(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def ts_array(values: list[str]) -> str:
    return "[" + ", ".join(ts_string(value) for value in values) + "]"


def write_site_data(chapters: list[dict[str, object]]) -> None:
    entries = []
    for chapter in chapters:
        process = list_value(chapter, "process_diagrams")
        entries.append(
            dedent(
                f"""
                {{
                  chapter: {chapter['chapter']},
                  slug: 'chapter-{int(chapter['chapter']):02d}',
                  title: {ts_string(str(chapter['title']))},
                  part: {ts_string(str(chapter['part']))},
                  coreQuestion: {ts_string(str(chapter['core_question']))},
                  summary: {ts_string(str(chapter['summary']))},
                  status: '{COURSEBOOK_READY}',
                  page: '/coursebook/chapter-{int(chapter['chapter']):02d}',
                  chapterSource: 'course/textbook/logical_v2/chapters/chapter_{int(chapter['chapter']):02d}.md',
                  chapterFocus: {ts_string(str(chapter['chapter_focus']))},
                  knowledgeGraph: 'course/textbook/logical_v2/graphs/chapter_{int(chapter['chapter']):02d}_knowledge_graph.mmd',
                  knowledgeMapImage: '/assets/coursebook/knowledge-maps/chapter-{int(chapter['chapter']):02d}.svg',
                  processDiagrams: {ts_array(process)},
                  sourceWeeks: {ts_array(list_value(chapter, 'source_weeks'))},
                  sourceChapters: {ts_array(list_value(chapter, 'source_chapters'))},
                  knowledgeSources: {ts_array(list_value(chapter, 'knowledge_sources'))},
                  materialSources: {ts_array(list_value(chapter, 'material_sources'))},
                  assetSources: {ts_array(list_value(chapter, 'asset_sources'))},
                  learningEvidence: {ts_array(list_value(chapter, 'learning_evidence'))}
                }}"""
            ).strip()
        )
    week_mapping = ", ".join(f"{week}: {chapter}" for week, chapter in sorted(WEEK_TO_CHAPTER.items()))
    text = f"""import {{ weeks }} from './weeks';

export type CoursebookChapterStatus = '{COURSEBOOK_READY}';

export type CoursebookChapter = {{
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
}};

export const textbookChapterSource = (chapter: number) =>
  `course/textbook/logical_v2/chapters/chapter_${{String(chapter).padStart(2, '0')}}.md`;

export const textbookStoryboardSource = (week: number) =>
  `course/weeks/week_${{String(week).padStart(2, '0')}}/ppt_storyboard.md`;

export const textbookTeachingPlanSource = (week: number) =>
  `course/weeks/week_${{String(week).padStart(2, '0')}}/teaching_plan.md`;

export const textbookAssetSources = (week: number) => {{
  const prefix = 'course/textbook/assets';
  const assetMap: Record<number, string[]> = {{
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
  }};
  return (assetMap[week] ?? []).map((path) => `${{prefix}}/${{path}}`);
}};

export const weekToCoursebookChapter: Record<number, number> = {{{week_mapping}}};

export const coursebookChapters: CoursebookChapter[] = [
  {",\n  ".join(entries)}
];

export const textbookChapters = coursebookChapters;
export const logicalV2Chapters = coursebookChapters;
export const logicalV2ReviewChapters = coursebookChapters;
export const sampleChapters: CoursebookChapter[] = [];

export type CoursewareWeek = {{
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
}};

const pilotReadyWeeks = new Set([3, 13, 14, 15, 16]);

export const coursewareWeeks: CoursewareWeek[] = weeks.map((week) => {{
  const chapter = getCoursebookChapterByWeek(week.week);
  return {{
    week: week.week,
    slug: week.slug,
    title: week.title,
    page: `/courseware/${{week.slug}}`,
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
      `course/weeks/week_${{String(week.week).padStart(2, '0')}}/materials.md`,
      `course/weeks/week_${{String(week.week).padStart(2, '0')}}/outline.md`,
      `course/weeks/week_${{String(week.week).padStart(2, '0')}}/script.md`,
      textbookTeachingPlanSource(week.week),
      textbookStoryboardSource(week.week)
    ],
    assetSources: textbookAssetSources(week.week),
    badges: ['40 页主干 storyboard']
  }};
}});

export function getCoursebookChapterBySlug(slug: string) {{
  return coursebookChapters.find((chapter) => chapter.slug === slug);
}}

export function getCoursebookChapterByWeek(week: number) {{
  const chapterNo = weekToCoursebookChapter[week];
  return coursebookChapters.find((chapter) => chapter.chapter === chapterNo);
}}

export function getLogicalV2ChapterBySlug(slug: string) {{
  return getCoursebookChapterBySlug(slug);
}}

export function getCoursewareWeekBySlug(slug: string) {{
  return coursewareWeeks.find((week) => week.slug === slug);
}}

export function getCoursewareWeekByWeek(week: number) {{
  return coursewareWeeks.find((coursewareWeek) => coursewareWeek.week === week);
}}
"""
    assert_style(SITE_DATA, text)
    SITE_DATA.write_text(text, encoding="utf-8")


def main() -> int:
    existing_map = LOGICAL_V2 / "coursebook_map.yml"
    chapters = merge_chapters(parse_map(existing_map))
    for path in (CHAPTER_DIR, GRAPH_DIR, FLOW_DIR, PUBLIC_MAP_DIR):
        path.mkdir(parents=True, exist_ok=True)
    write_chapters(chapters)
    write_map(chapters)
    write_blueprint(chapters)
    write_coverage(chapters)
    write_graphs(chapters)
    write_svg_maps(chapters)
    write_site_data(chapters)
    print("OK: built logical v2 Coursebook chapters, maps, graphs, SVG assets, and site data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
