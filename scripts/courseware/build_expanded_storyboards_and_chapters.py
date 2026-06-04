"""Generate 40-page mainline storyboards and expanded textbook chapters.

This script builds source-controlled Markdown only. It does not generate PPTX,
PNG previews, contact sheets, or other binary presentation outputs.
"""
from __future__ import annotations

import re
from pathlib import Path

from build_textbook_source_assets import ASSETS_DIR, CHAPTERS, CHAPTERS_DIR, ROOT, TEXTBOOK, ChapterSpec


MAP_PATH = TEXTBOOK / "coursebook_map.yml"
STORYBOARD_STATUS = "storyboard_expanded"
TEXTBOOK_STATUS = "expanded_draft"
STORYBOARD_PAGES = 40
FOCUS_WEEKS = {3, 11, 12, 13, 14, 15, 16}
STRICT_STORYBOARD_WEEKS = {3, 5, 8, 11, 12, 13, 15, 16, 18}

STORYBOARD_HEADERS = (
    "Slide",
    "Module",
    "Action title",
    "Core content",
    "Visual intent",
    "Data/code asset",
    "Teacher explanation",
    "Student action",
    "Timing",
    "Textbook section link",
    "Evidence/source note",
    "Risk/boundary note",
)

MODULES = (
    (1, 4, "课程定位与导入", "本周先把问题和误区讲清楚"),
    (5, 12, "核心概念展开", "概念必须绑定输入、输出和边界"),
    (13, 20, "数据结构与案例", "案例先看字段和观测单位"),
    (21, 30, "方法流程与代码", "代码要讲输入、处理、输出和错误"),
    (31, 36, "图表与结果解释", "图表只支持有来源的观察"),
    (37, 40, "AI 协作与核验收束", "AI 只能帮助审计和改写边界"),
)


def pipe(text: object) -> str:
    """Escape Markdown table-breaking characters while keeping text compact."""
    return str(text).replace("|", "｜").replace("\n", "<br>")


def chinese_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def asset_paths(spec: ChapterSpec) -> dict[str, str]:
    return {
        "dataset": f"course/textbook/assets/datasets/{spec.dataset_name}",
        "code": f"course/textbook/assets/code/{spec.code_name}",
        "diagram": f"course/textbook/assets/diagrams/{spec.diagram_name}",
        "chapter": f"course/textbook/chapters/chapter_{spec.week:02d}.md",
        "storyboard": f"course/weeks/week_{spec.week:02d}/ppt_storyboard.md",
    }


def module_for_slide(slide: int) -> str:
    for start, end, module, _purpose in MODULES:
        if start <= slide <= end:
            return module
    raise ValueError(f"Unexpected slide: {slide}")


def timing_for_slide(slide: int) -> str:
    """Return a 90-minute two-period timing budget for the 40 mainline pages."""
    timing = {
        1: 2,
        2: 2,
        3: 2,
        4: 2,
        5: 2,
        6: 2,
        7: 2,
        8: 2,
        9: 2,
        10: 2,
        11: 2,
        12: 2,
        13: 2,
        14: 3,
        15: 2,
        16: 3,
        17: 2,
        18: 3,
        19: 2,
        20: 3,
        21: 2,
        22: 3,
        23: 2,
        24: 3,
        25: 2,
        26: 3,
        27: 2,
        28: 3,
        29: 2,
        30: 2,
        31: 2,
        32: 3,
        33: 2,
        34: 3,
        35: 2,
        36: 2,
        37: 2,
        38: 2,
        39: 2,
        40: 2,
    }
    return f"{timing[slide]} min"


def student_action_for_slide(spec: ChapterSpec, slide: int) -> str:
    """Describe the observable learner move for one storyboard page."""
    assets = asset_paths(spec)
    first_concept = spec.concepts[0][0]
    second_concept = spec.concepts[1][0]
    source = spec.source_refs[(slide - 1) % len(spec.source_refs)]
    route_steps = [part.strip() for part in spec.route.split("->")]
    route_step = route_steps[(slide - 1) % len(route_steps)]

    actions: dict[int, str] = {
        1: f"学生用一句话把导入问题改写为“数据、方法、边界”三栏，并标出仍需核验的词。",
        2: f"学生在 18 周路线轴上标出本周输入来自哪里、输出服务下一周哪一步。",
        3: f"学生判断 3 个学习目标中哪个能通过表格、代码或图注现场观察到。",
        4: f"学生改写一条过度结论，把它降级为课堂观察、候选解释或待核验点。",
    }

    concept_actions = (
        f"学生标出“{first_concept}”需要的输入、产生的输出和不能支持的结论。",
        f"学生比较“{second_concept}”与本周案例字段之间的一一对应关系。",
        f"学生判断概念解释中哪一句属于事实、哪一句仍需来源核验。",
        f"学生说出一个把概念误写成医学或机制结论的风险表达。",
        f"学生标出 `{assets['dataset']}` 中与“{first_concept}”对应的字段或图形元素。",
        f"学生写出一句含前提的概念解释，避免脱离输入输出。",
        f"学生检查 AI 对概念的解释是否遗漏来源、参数或观测单位。",
        f"学生补写一个“不能据此说明……”的边界句。",
    )
    for offset, action in enumerate(concept_actions):
        actions[5 + offset] = action

    case_actions = (
        f"学生打开或查看 `{assets['dataset']}`，标出主键、分组和主要指标列。",
        "学生补写每个关键字段的字段含义、单位或来源说明。",
        "学生判断一行数据代表 patient、sample、gene、cell、spot 还是项目条目。",
        "学生把分组、批次、处理条件或来源信息写成 metadata 检查项。",
        "学生检查小数据，找出一个缺失、异常、阈值或样本错位风险。",
        "学生列出进入代码前必须先确认的两个质量问题。",
        f"学生写出来源 `{source}` 与课堂用途之间的一句可追溯说明。",
        f"学生写出本案例能支持的一个观察，并写出不能外推到真实结论的一句话。",
    )
    for offset, action in enumerate(case_actions):
        actions[13 + offset] = action

    method_actions = (
        f"学生在流程图中圈出 `{route_step}` 的输入和输出。",
        f"学生运行或阅读 `{assets['code']}`，标出负责读入数据的代码行。",
        f"学生检查 `{assets['dataset']}`，指出代码实际使用的列名。",
        "学生检查第一段处理逻辑是否过滤、分组或类型转换了正确字段。",
        "学生手工复核一行计算、标记、阈值判断或矩阵转换结果。",
        "学生读出前三行输出，并判断输出能回答哪一个课堂问题。",
        "学生把阈值、参数或分组规则写入运行记录的一句话。",
        "学生标出一个列名、缺失值、类型或样本错位导致的代码风险。",
        "学生补写一条可复现记录：输入文件、代码文件、运行输出和人工修改。",
        f"学生回到导入问题，判断代码结果能回答什么、不能回答什么。",
    )
    for offset, action in enumerate(method_actions):
        actions[21 + offset] = action

    figure_actions = (
        "学生在图表草图上标出横轴、纵轴、颜色、图例和单位分别对应什么字段。",
        "学生标出结果表字段所属的标识、分组、统计、坐标和待核验类别。",
        "学生改写一条图注，补入教学模拟、字段含义、单位或参数说明。",
        "学生改写一句强结论，拆出观察、统计关联、候选解释和待核验事实。",
        "学生检查一次 Claim-Evidence Gate，指出证据来源和人工核验状态。",
        "学生说出本周结果如何衔接下一周，同时指出不能提前完成的任务。",
    )
    for offset, action in enumerate(figure_actions):
        actions[31 + offset] = action

    ai_actions = (
        f"学生写一条限定任务边界的 AI Prompt，只让 AI 检查字段、方法、图表和待核验点。",
        "学生标出一段 AI 输出中可保留、需修改、必须删除的三类句子。",
        "学生判断一个医学、统计、基因功能或细胞注释说法应由谁核验。",
        "学生写出一条克制句子总结本周，只保留数据和方法真正支持的内容。",
    )
    for offset, action in enumerate(ai_actions):
        actions[37 + offset] = action

    return actions[slide]


def storyboard_row(spec: ChapterSpec, slide: int) -> list[str]:
    assets = asset_paths(spec)
    concepts = list(spec.concepts)
    concept = concepts[(slide - 5) % len(concepts)]
    source = spec.source_refs[(slide - 1) % len(spec.source_refs)]
    route_steps = [part.strip() for part in spec.route.split("->")]
    route_step = route_steps[(slide - 1) % len(route_steps)]
    goal = spec.goals[(slide - 1) % len(spec.goals)]

    rows: dict[int, tuple[str, str, str, str, str, str, str]] = {
        1: (
            f"用一个可核验问题打开第 {spec.week:02d} 周",
            f"本周导入问题是：{spec.intro} 教师先要求学生把问题改写为数据、方法和边界三件事。",
            "标题页叠加问题卡和课程链路条",
            assets["chapter"],
            "开场不要给结论，先让学生意识到医药数据分析不是把结果交给工具，而是把问题拆成可检查的结构。",
            "本章导入",
            "不得把导入问题直接讲成医学、机制或统计结论。",
        ),
        2: (
            "本周承接上一周并服务下一周",
            f"把本周放在全课路线中：{spec.route}。这条路线说明本周只解决链条中的特定环节。",
            "18 周课程进度轴，突出本周节点",
            assets["diagram"],
            "教师说明前后周衔接，帮助学生知道哪些知识已经学过，哪些内容只作预告，不在本周展开。",
            "Storyboard 对应表",
            "不把后续周次的高级 workflow 提前变成学生必跑任务。",
        ),
        3: (
            "学习目标要落在可观察行为上",
            "本页把目标拆为三类：能识别输入，能解释处理过程，能写出证据边界。",
            "三列目标表，逐列标出输入、处理、边界",
            assets["chapter"],
            f"教师逐条解释目标：{goal} 目标不是背术语，而是能对小数据、代码或图表做出有依据的说明。",
            "学习目标",
            "学习目标不能写成掌握完整研究流程或独立完成高级生信分析。",
        ),
        4: (
            "先暴露本周最容易犯的解释错误",
            f"本周常见误区是把 {route_step} 看到的课堂观察直接写成真实结论，忽略来源、参数和待核验点。",
            "错误表达与修订表达对照框",
            assets["chapter"],
            "教师用一条错误句子演示怎样降级为观察、候选解释或待核验点，建立整节课的表达边界。",
            "来源与待核验点",
            "错误示例必须标注为反例，不能被学生当成推荐结论。",
        ),
    }

    for offset in range(8):
        slide_no = 5 + offset
        term, desc = concepts[offset % len(concepts)]
        if offset < len(concepts):
            title = f"先定义 {term} 的输入和输出"
        else:
            title = f"用 {term} 检查案例解释边界"
        rows[slide_no] = (
            title,
            f"核心概念“{term}”的课堂定义是：{desc} 本页同时说明它需要什么输入、产生什么输出、不能支持什么结论。",
            f"{term} 概念卡，左侧输入，右侧输出和边界",
            assets["diagram"] if offset % 2 else assets["chapter"],
            f"教师不要只读定义，要把“{term}”放回 {spec.case_title} 的场景，让学生看到概念怎样约束数据解释。",
            "核心概念",
            f"如果学生把“{term}”解释成医学事实、机制事实或统计事实，需要立即要求其补来源和前提。",
        )

    case_rows = (
        ("主案例从一个小表开始", f"案例名称是“{spec.case_title}”。本页先说明数据是教学模拟或课程化改写素材。"),
        ("字段含义决定后续分析是否可信", "逐列解释样本标识、分组、指标、单位、来源和可能缺失。"),
        ("观测单位必须先说清楚", "判断一行代表 patient、sample、gene、cell、spot 还是项目条目。"),
        ("metadata 不是附录而是解释入口", "把分组、批次、处理条件和来源信息从结果表中分离出来。"),
        ("小数据先做人工核验", "让学生先用肉眼或手算识别明显风险，再进入代码或图形。"),
        ("质量风险要早于结论出现", "列出缺失、错位、单位不明、样本量不足、参数不明等风险。"),
        ("素材来源要和课堂用途绑定", f"本页把来源 `{source}` 与本周课堂任务绑定，避免资源堆砌。"),
        ("案例边界决定能写什么句子", f"本案例可支持对 {route_step} 的课堂观察，不支持直接外推为真实研究结论。"),
    )
    for offset, (title, content) in enumerate(case_rows):
        slide_no = 13 + offset
        rows[slide_no] = (
            title,
            content,
            "小数据表、字段字典和风险标记三栏布局",
            assets["dataset"],
            "教师把表格逐行读给学生听，强调每个字段进入分析前都要能回答来源、单位和含义。",
            "案例数据与字段说明",
            "教学模拟数据不得被描述为真实患者、真实药效、真实表达矩阵或真实细胞注释。",
        )

    method_rows = (
        ("方法流程先看全图再看细节", f"用流程图串联 {spec.route}，让学生知道每一步的输入和输出。"),
        ("代码文件只是可核验示例", f"配套代码 `{assets['code']}` 用于说明处理逻辑，不作为真实研究 pipeline。"),
        ("代码输入必须回到字段字典", f"代码读取 `{assets['dataset']}`，教师要求学生先指出会被代码使用的列。"),
        ("第一段处理逻辑负责选择有效记录", "说明过滤、分组、类型转换或样本匹配，不让 AI 直接代替判断规则。"),
        ("第二段处理逻辑负责计算或标记", "解释均值、阈值、矩阵转换、模型字段或图形坐标如何得到。"),
        ("运行输出要能被人工复核", "展示前 3 行输出或汇总结果，并回到小数据手工检查。"),
        ("参数和阈值要写入来源说明", "说明阈值、分组、标准化、距离、resolution 或图形参数来自课堂规则而非通用标准。"),
        ("常见代码错误来自列名和类型", "展示列名拼写、缺失值、因子/字符串、样本错位或空结果的风险。"),
        ("可复现记录比一次跑通更重要", "记录输入文件、代码版本、运行输出、AI 建议和人工修改。"),
        ("方法小结回到本周问题", f"本页把代码输出重新放回“{spec.intro}”，说明能回答什么、不能回答什么。"),
    )
    for offset, (title, content) in enumerate(method_rows):
        slide_no = 21 + offset
        rows[slide_no] = (
            title,
            content,
            "流程图、代码片段、输出框和审计记录并列",
            assets["code"],
            "教师逐步解释代码意图，只讲本周需要的最小结构，不展开无关语法百科或完整高级 workflow。",
            "方法流程与代码解读",
            "代码输出不是研究结论，必须和输入字段、参数、教学模拟边界一起呈现。",
        )

    figure_rows = (
        ("图表先说明视觉编码", "解释横轴、纵轴、颜色、形状、图例和单位分别映射什么字段。"),
        ("结果表字段回答不同问题", "区分标识列、分组列、统计列、图形坐标列和待核验列。"),
        ("图注要保留数据来源和处理前提", "图注必须包含教学模拟、字段含义、单位或参数说明。"),
        ("证据边界决定报告句子的强度", "把观察、统计关联、候选解释和待核验事实分开写。"),
        ("Claim-Evidence Gate 用来拦截过度结论", "每一句结论都要能回答证据从哪里来、是否经过人工核验。"),
        ("本周结果服务下一个学习节点", "把本周图表或结果表连接到下一周，不提前完成下一周任务。"),
    )
    for offset, (title, content) in enumerate(figure_rows):
        slide_no = 31 + offset
        rows[slide_no] = (
            title,
            content,
            "结果表、示意图、图注和证据门四区布局",
            assets["diagram"],
            "教师用同一张图或表反复追问：图上看到了什么，数据支持什么，还需要核验什么。",
            "图表与结果解释",
            "不得把颜色、聚类、P 值、相关性或 AI 图注直接写成机制、疗效或临床建议。",
        )

    ai_rows = (
        ("AI Prompt 必须限制任务边界", f"Prompt 只要求 AI 检查 {spec.case_title} 的字段、方法、图表和待核验点。"),
        ("AI 输出先当作待审文本", "把 AI 生成的解释拆成可保留、需修改、需删除三类。"),
        ("人工核验负责最终证据状态", "教师说明医学意义、统计前提、基因功能、通路和细胞注释都要人工核验。"),
        ("用一条克制句子收束本周", f"最终表达必须回到 {spec.route}，只说本周数据和方法真正支持的内容。"),
    )
    for offset, (title, content) in enumerate(ai_rows):
        slide_no = 37 + offset
        rows[slide_no] = (
            title,
            content,
            "Prompt、AI 输出审计表、人工核验清单和下周衔接条",
            assets["chapter"],
            "教师强调 AI 是解释、检查和重构工具，不是医学判断、统计判断或真实数据核验者。",
            "AI 协作与核验",
            "AI 不得编造数据来源、样本量、统计显著性、基因功能、细胞类型、药效机制或临床建议。",
        )

    title, content, visual, asset, teacher, section, risk = rows[slide]
    student_action = student_action_for_slide(spec, slide)
    timing = timing_for_slide(slide)
    teacher = (
        f"{teacher} 本页教师追问：请学生完成“{student_action}”，并用一句话说明证据边界。"
    )
    return [
        str(slide),
        module_for_slide(slide),
        title,
        content,
        visual,
        asset,
        teacher,
        student_action,
        timing,
        section,
        source,
        risk,
    ]


def storyboard_markdown(spec: ChapterSpec) -> str:
    header = " | ".join(STORYBOARD_HEADERS)
    divider = " | ".join(["---:" if name == "Slide" else "---" for name in STORYBOARD_HEADERS])
    rows = [" | ".join(pipe(cell) for cell in storyboard_row(spec, slide)) for slide in range(1, STORYBOARD_PAGES + 1)]
    source = f"course/textbook/chapters/chapter_{spec.week:02d}.md"
    return f"""---
type: course-ppt-storyboard
week: {spec.week}
title: {spec.title}
ppt_status: {STORYBOARD_STATUS}
storyboard_kind: mainline_source
target_pages: {STORYBOARD_PAGES}
excludes: [practice_pages, answer_pages, review_pages, backup_pages]
source: [materials.md, outline.md, script.md, {source}]
---

# Week {spec.week:02d} PPT Storyboard：{spec.title}

本 storyboard 是 40 页主干内容源稿，用于后续 PPTX 裁剪、教师备课和在线教材同步扩写。它不是最终课堂投屏页数，也不表示 PPTX、PNG 预览或 contact sheet QA 已完成。本轮只扩展主干讲授内容、案例、数据结构、代码、图表解释和 AI 核验边界；其他教学支持材料后续单独追加。

| {header} |
| {divider} |
""" + "\n".join(f"| {row} |" for row in rows) + """

## Evidence Checklist

- 40 页均服务主干讲授，不把完整 storyboard 等同于正式投屏页数。
- 所有数据、代码和图形均引用 source-controlled 教学资产；若替换为外部图或真实数据，必须重新做 source review。
- 本 storyboard 的 `ppt_status` 只表示 `storyboard_expanded`，不表示 PPTX 已生成或视觉 QA 完成。
- AI 仅用于解释、核验和改写边界，不替代医学判断、统计判断、基因功能核验、细胞注释或真实结果确认。
"""


def storyboard_mapping_table() -> str:
    lines = [
        "| Slide range | Storyboard module | Textbook section | Purpose |",
        "|---|---|---|---|",
    ]
    for start, end, module, purpose in MODULES:
        section = {
            "课程定位与导入": "本章导入；本章主线与课程位置",
            "核心概念展开": "核心概念；概念展开与药学解释",
            "数据结构与案例": "案例数据与字段说明；课堂案例",
            "方法流程与代码": "方法路线；工具实现与代码样例；方法流程与代码解读",
            "图表与结果解释": "图表与结果解释；证据边界",
            "AI 协作与核验收束": "AI 协作与核验；来源与待核验点",
        }[module]
        lines.append(f"| {start}-{end} | {module} | {section} | {purpose} |")
    return "\n".join(lines)


def detailed_slide_narrative(spec: ChapterSpec) -> str:
    parts: list[str] = []
    for slide in range(1, STORYBOARD_PAGES + 1):
        row = storyboard_row(spec, slide)
        _, module, title, core, visual, asset, teacher, student_action, timing, section, source, risk = row
        parts.append(
            f"### Slide {slide:02d} · {title}\n\n"
            f"这一页属于“{module}”，在教材中对应“{section}”。主干内容是：{core}"
            f" 画面应采用“{visual}”，并显式引用 `{asset}`。教师讲解时要做到：{teacher}"
            f" 学生当场动作是：{student_action} 预计用时 {timing}。"
            f" 证据来源从 `{source}` 开始核对。边界提示是：{risk}"
            f" 本页进入教材正文时要写成连续说明，不要只保留幻灯片标题；学生复习时应能从文字中看出输入、处理、输出和待核验点之间的关系。\n"
        )
    return "\n".join(parts)


def chapter_markdown(spec: ChapterSpec) -> str:
    assets = asset_paths(spec)
    concept_lines = "\n".join(f"- **{term}**：{desc}" for term, desc in spec.concepts)
    goal_lines = "\n".join(f"- {goal}" for goal in spec.goals)
    source_lines = "\n".join(f"- `{source}`" for source in spec.source_refs)
    diagram_path = ASSETS_DIR / "diagrams" / spec.diagram_name
    diagram_text = diagram_path.read_text(encoding="utf-8").strip() if diagram_path.exists() else "flowchart LR\n    missing[\"diagram source missing\"]"
    focus_note = "本章是本轮重点扩写章节，正文进一步展开案例、代码、图形和证据边界，支撑后续 PPTX 试点。" if spec.week in FOCUS_WEEKS else "本章是全书扩写稿，先形成足够完整的教学主干，后续再追加独立任务页和复盘页。"

    text = f"""---
type: textbook-chapter
chapter: {spec.week}
week: {spec.week}
title: {spec.title}
status: expanded_draft
textbook_status: {TEXTBOOK_STATUS}
storyboard_source: {assets["storyboard"]}
storyboard_pages: {STORYBOARD_PAGES}
updated: 2026-06-04
audience: 药学本科生
chapter_source: {assets["chapter"]}
asset_sources:
  - {assets["dataset"]}
  - {assets["code"]}
  - {assets["diagram"]}
---

# 第 {spec.week} 章 {spec.title}

## 本章导入

{spec.intro}

{focus_note} 本章仍以课程周次事实文件为主线，所有示例均为教学模拟或课程化改写素材。它们用于训练数据结构、代码核验、图表表达和证据边界，不代表真实医学、统计、生物学或临床结论。

## 学习目标

{goal_lines}

## Storyboard 对应表

{storyboard_mapping_table()}

## 本章主线与课程位置

第 {spec.week:02d} 周处在“{spec.phase}”阶段。本章的主线是 **{spec.route}**。教师备课时应把这条路线看作一个证据链：前一环节提供输入，后一环节只在输入可靠、字段清楚、参数可追溯时才有解释价值。学生不需要把所有工具细节一次性掌握，但必须能说明本周为什么需要这些输入、为什么产生这些输出，以及哪些表达必须保留为待核验状态。

从课程整体看，本章不是独立百科条目，而是 36 课时主线中的一个教学节点。它既要服务课堂讲授，也要服务在线教材、后续 PPTX 生成和项目复盘。教材正文因此比课堂投屏更细：它保留字段说明、代码意图、图表解释和 AI 审计理由，方便学生课后回到源稿复习，也方便教师在制作 PPT 时裁剪主干内容。

## 核心概念

{concept_lines}

## 概念展开与药学解释

本章的概念讲解要始终绑定药学语境。以“{spec.case_title}”为例，教师不能只解释术语，还要追问术语背后的输入和输出。学生需要知道一列数据来自哪里，代表什么观测单位，是否有单位、分组、批次或来源说明。如果这些基础信息缺失，任何代码运行、图表展示或 AI 解释都只能算课堂演示，不能被写成可靠结论。

概念之间也要形成顺序。`{spec.route}` 不是装饰性的流程图，而是本章的认知路径。教师应先讲清数据如何进入流程，再讲方法如何处理数据，最后讲输出如何被解释。对药学本科生而言，最重要的不是记住所有函数名，而是形成“先看输入，再看处理，再看输出，最后看证据边界”的稳定习惯。

## 方法路线

本章路线可以概括为：**{spec.route}**。

```mermaid
{diagram_text}
```

这张路线图进入教材和 storyboard 时必须配合文字解释。第一，路线图只表示教学流程，不表示学生已经能够运行完整研究 workflow。第二，图中的每个节点都需要明确输入和输出。第三，图中的 AI 审计只用于检查解释是否遗漏字段、方法和待核验点，不能替代医学、统计或生物学判断。

## 案例数据与字段说明

本章配套小数据是 `{assets["dataset"]}`。教师应先让学生阅读字段，而不是立刻运行代码。字段阅读至少包括四件事：字段名是否清楚，单位是否存在，观测单位是什么，是否有分组、批次或来源说明。若字段名称来自外部素材的缩写，教材正文只能保留课程化解释，不能把未核验缩写直接当作事实。

主案例“{spec.case_title}”承担本章的教学主线。这个案例的价值不在于数据规模，而在于它足够小，学生可以看见每一步处理如何改变输入。教师应把小数据、字段字典和风险提示并列展示，使学生理解：数据表不是结论表，图表也不是机制图，代码输出必须回到字段和来源重新解释。

## 工具实现与代码样例

本章配套代码是 `{assets["code"]}`。代码只承担课堂核验和结构说明功能，不作为真实研究流程。教师讲代码时应按四层展开：输入文件、关键字段、处理逻辑、输出结果。每一层都要能被学生用小数据复核。如果代码依赖阈值、分组、标准化或参数，教材必须写明这些规则是课堂教学规则，不是通用医学或统计标准。

代码讲解不能退化成语法百科。对于 Python 或 R 周次，教师可以多讲变量、列表、数据框、函数和输出；对于统计或组学周次，教师应把代码看作“可复核的流程说明”，重点解释结果表字段、图形坐标和核验清单。AI 可以帮助解释代码、定位报错和生成边界样本，但学生必须保留人工判断和运行记录。

## 方法流程与代码解读

{detailed_slide_narrative(spec)}

## 图表与结果解释

图表解释要遵循四步：先确认数据来源，再解释视觉编码，再说明统计或处理前提，最后写证据边界。无论本章使用流程图、结果表、散点图、热图、UMAP 还是项目 rubric，都不能跳过图注和来源说明。图表中的颜色、距离、聚类、P 值、阈值或分数只是在特定数据和方法前提下的观察，不自动构成机制、疗效、诊断或推荐。

当教师把本章内容转成 PPT 时，可以从 40 页 storyboard 中裁剪正式投屏页，但不能删除证据边界。正式 PPT 可以压缩页数，教材源稿不能压缩证据链。教材应保留足够细的字段、代码和图形解释，方便学生课后复习时知道每张图表为什么能说某句话、为什么不能说另一句话。

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
请只指出字段、方法、图表和待核验点中的遗漏，不要替我编造医学、统计、基因功能、通路机制、细胞注释或临床建议。
```

AI 可以用于解释术语、检查代码、改写图注和生成待核验清单；不能替代数据来源、统计前提、医学意义、基因功能、细胞注释或真实结果核验。教师应要求学生把 AI 输出分为三类：可以保留的语言、需要修改的表达、必须删除的越界结论。只有经过人工核验和来源记录的内容，才可以进入报告或 PPT。

## 练习与参考答案要点

练习：{spec.exercise}

参考答案要点：{spec.answer}

本轮扩写不把练习、答案、课后复盘和备用拓展作为 40 页 storyboard 的独立页面；这些内容先保留在教材章节中，后续再单独追加到教学包或正式 PPT 备份页。

## 来源与待核验点

主要来源：

{source_lines}

待核验点：

- 进入公开展示或 PPT 前，检查素材授权、字段含义、单位和图形参数。
- 若使用外部书籍、Notebook 或 PDF 中的图形，只记录来源，不直接复制图像进入教材正文。
- 若 AI 输出涉及机制、疗效、统计显著性、基因功能、通路或细胞类型，必须回到课程数据、数据库或人工审查记录核验。
- 本章 `textbook_status: expanded_draft` 只表示教材源稿扩写，不表示试讲完成或 PPTX 完成。
"""

    target = 7000 if spec.week in FOCUS_WEEKS else 5000
    if chinese_count(text) < target:
        raise ValueError(f"Chapter {spec.week:02d} is too short: {chinese_count(text)} Chinese chars, target {target}")
    return text


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
                current[key] = int(value) if key in {"week", "chapter", "storyboard_pages"} else value.strip("'\"")
                current_list = None
            else:
                current[key] = []
                current_list = key
    if current is not None:
        chapters.append(current)
    return chapters


def write_map(chapters: list[dict[str, object]]) -> None:
    spec_by_week = {spec.week: spec for spec in CHAPTERS}
    lines = [
        "version: 1",
        "title: 医药数据处理与可视化在线教材映射",
        "policy: course/syllabus and course/weeks are the course truth layer; knowledge is supporting context only.",
        "chapters:",
    ]
    list_fields = ("asset_sources", "source_week_files", "knowledge_sources", "material_sources")
    for chapter in chapters:
        week = int(chapter["week"])
        spec = spec_by_week[week]
        assets = asset_paths(spec)
        chapter["chapter"] = week
        chapter["week"] = week
        chapter["title"] = spec.title
        chapter["page"] = f"/coursebook/week-{week:02d}"
        chapter["chapter_source"] = assets["chapter"]
        chapter["textbook_status"] = TEXTBOOK_STATUS
        chapter["storyboard_source"] = assets["storyboard"]
        chapter["storyboard_pages"] = STORYBOARD_PAGES
        chapter["ppt_status"] = STORYBOARD_STATUS
        chapter["asset_sources"] = [assets["dataset"], assets["code"], assets["diagram"]]
        source_files = list(chapter.get("source_week_files", []))
        if assets["storyboard"] not in source_files:
            source_files.append(assets["storyboard"])
        chapter["source_week_files"] = source_files

        lines.append(f"  - chapter: {week}")
        for key in ("week", "title", "page", "chapter_source", "textbook_status", "storyboard_source", "storyboard_pages"):
            lines.append(f"    {key}: {chapter[key]}")
        for field in list_fields:
            lines.append(f"    {field}:")
            values = chapter.get(field, [])
            assert isinstance(values, list)
            for value in values:
                lines.append(f"      - {value}")
        lines.append(f"    ppt_status: {chapter['ppt_status']}")
        lines.append(f"    review_status: {chapter.get('review_status', 'pilot_candidate')}")
    MAP_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_all() -> None:
    for spec in CHAPTERS:
        week_dir = ROOT / "course" / "weeks" / f"week_{spec.week:02d}"
        week_dir.mkdir(parents=True, exist_ok=True)
        (week_dir / "ppt_storyboard.md").write_text(storyboard_markdown(spec), encoding="utf-8", newline="\n")
        (CHAPTERS_DIR / f"chapter_{spec.week:02d}.md").write_text(chapter_markdown(spec), encoding="utf-8", newline="\n")
    write_map(parse_map(MAP_PATH))


def main() -> None:
    write_all()
    print(f"Generated {len(CHAPTERS)} expanded storyboards and textbook chapters with {STORYBOARD_PAGES} pages each.")


if __name__ == "__main__":
    main()
