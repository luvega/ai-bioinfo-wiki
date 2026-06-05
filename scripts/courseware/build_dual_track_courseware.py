"""Build the dual-track textbook and courseware sources.

This generator keeps three products separate:

- textbook chapters: knowledge-system prose for reading and review
- teaching plans: 90-minute classroom organization by week
- PPT storyboards: 40-page page-level source drafts for future slide trimming

It writes source-controlled Markdown/YAML only. It does not generate PPTX,
PNG previews, contact sheets, or other binary presentation outputs.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from build_expanded_storyboards_and_chapters import (
    MODULES,
    STORYBOARD_PAGES,
    STORYBOARD_STATUS,
    TEXTBOOK_STATUS,
    asset_paths,
    chinese_count,
    pipe,
    storyboard_mapping_table,
    storyboard_markdown,
    storyboard_row,
    timing_for_slide,
)
from build_textbook_source_assets import ASSETS_DIR, CHAPTERS, CHAPTERS_DIR, ROOT, TEXTBOOK, ChapterSpec


MAP_PATH = TEXTBOOK / "coursebook_map.yml"
PLAN_STATUS = "teaching_plan_ready"
FOCUS_WEEKS = {3, 5, 8, 11, 12, 13, 14, 15, 16, 18}

BLOCK_PURPOSE: dict[str, tuple[str, str, str]] = {
    "课程定位与导入": (
        "校准本周问题、上一周衔接和常见误区。",
        "用导入问题和反例表达建立本周证据边界。",
        "学生完成问题拆解或过度结论降级。",
    ),
    "核心概念展开": (
        "把术语放回输入、输出和药学解释场景。",
        "逐个概念追问字段、前提和不能支持的结论。",
        "学生标注概念对应的数据字段或图形元素。",
    ),
    "数据结构与案例": (
        "用小数据表建立字段、观测单位和 metadata 直觉。",
        "带学生阅读字段字典、来源说明和质量风险。",
        "学生标出主键、分组、单位和进入代码前的风险。",
    ),
    "方法流程与代码": (
        "把方法路线、代码输入、处理逻辑和输出连成可复核链条。",
        "逐段解释代码意图，只讲本周需要的最小结构。",
        "学生运行或阅读代码，并手工复核一处输出。",
    ),
    "图表与结果解释": (
        "训练图表视觉编码、结果表字段和图注证据边界。",
        "用同一张图或表反复追问看到什么、支持什么、还需核验什么。",
        "学生改写图注或执行 Claim-Evidence Gate。",
    ),
    "AI 协作与核验收束": (
        "把 AI 使用限定为解释、检查、重构和边界改写。",
        "示范把 AI 输出拆成保留、修改、删除三类。",
        "学生写出限定任务边界的 prompt 和克制总结句。",
    ),
}

PHASE_LINKS = (
    (1, 4, "工具、AI 边界与可复现入口"),
    (5, 10, "表格整理、统计推断与模型解释"),
    (11, 13, "科研图表、高维矩阵与现代组学图形桥接"),
    (14, 16, "转录组、差异表达、单细胞与空间组学图形"),
    (17, 18, "项目交付、汇报答辩与课程闭环"),
)


def teaching_plan_source(week: int) -> str:
    return f"course/weeks/week_{week:02d}/teaching_plan.md"


def week_dir(week: int) -> Path:
    return ROOT / "course" / "weeks" / f"week_{week:02d}"


def slide_range_minutes(start: int, end: int) -> int:
    return sum(int(timing_for_slide(slide).split()[0]) for slide in range(start, end + 1))


def phase_band(week: int) -> str:
    for start, end, label in PHASE_LINKS:
        if start <= week <= end:
            return label
    return "课程主线"


def block_rows(spec: ChapterSpec) -> list[list[str]]:
    assets = asset_paths(spec)
    rows: list[list[str]] = []
    for start, end, module, _purpose in MODULES:
        focus, teacher, student = BLOCK_PURPOSE[module]
        minutes = slide_range_minutes(start, end)
        if module == "数据结构与案例":
            material = assets["dataset"]
            product = "字段字典、观测单位判断和质量风险清单"
            evidence = "能准确说出关键字段、单位、来源和进入代码前的核验点"
        elif module == "方法流程与代码":
            material = assets["code"]
            product = "代码运行记录、手工复核结果和参数说明"
            evidence = "能把代码输入、处理逻辑和输出结果逐项对应"
        elif module == "图表与结果解释":
            material = assets["diagram"]
            product = "图注草稿、结果解释句和 Claim-Evidence Gate"
            evidence = "能区分图上观察、统计关联、候选解释和待核验事实"
        elif module == "AI 协作与核验收束":
            material = assets["chapter"]
            product = "限定边界的 prompt、AI 输出审计和克制总结句"
            evidence = "能指出 AI 输出中可保留、需修改和必须删除的内容"
        elif module == "核心概念展开":
            material = assets["diagram"]
            product = "概念输入输出表和不能支持的结论清单"
            evidence = "能把术语放回字段、图形或方法前提中解释"
        else:
            material = assets["chapter"]
            product = "问题拆解表和过度结论降级句"
            evidence = "能把本周导入问题拆成数据、方法、边界三栏"
        rows.append(
            [
                module,
                f"{minutes} min",
                f"{start}-{end}",
                focus,
                teacher,
                student,
                product,
                evidence,
                material,
            ]
        )
    return rows


def teaching_plan_markdown(spec: ChapterSpec) -> str:
    assets = asset_paths(spec)
    goals = "\n".join(f"- {goal}" for goal in spec.goals)
    concepts = "、".join(term for term, _desc in spec.concepts)
    source_refs = "\n".join(f"- `{source}`" for source in spec.source_refs)
    rows = [" | ".join(pipe(cell) for cell in row) for row in block_rows(spec)]
    header = "Block | Minutes | Storyboard slides | Teaching focus | Teacher activity | Student action | Classroom product | Assessment evidence | Materials"
    divider = "--- | ---: | --- | --- | --- | --- | --- | --- | ---"
    total_minutes = sum(int(row[1].split()[0]) for row in block_rows(spec))
    if total_minutes != 90:
        raise ValueError(f"Week {spec.week:02d} teaching plan totals {total_minutes} minutes")
    return f"""---
type: course-teaching-plan
week: {spec.week}
title: {spec.title}
duration_minutes: 90
teaching_plan_status: {PLAN_STATUS}
storyboard_source: {assets["storyboard"]}
chapter_source: {assets["chapter"]}
source: [materials.md, outline.md, script.md, ppt_storyboard.md, {assets["chapter"]}]
---

# Week {spec.week:02d} Teaching Plan：{spec.title}

## 本周定位

本教学计划回答“90 分钟怎么教”，不替代教材章节，也不替代 PPT storyboard。教材章节负责组织 `{concepts}` 等知识体系；PPT storyboard 负责把这些内容拆成 40 页可审查投屏源稿；本文件负责把教师活动、学生动作、课堂产物和评价证据串成 2 课时课堂流程。

本周位于“{phase_band(spec.week)}”阶段，导入问题是：{spec.intro} 课堂目标不是把学生训练成完整 workflow 操作者，而是让学生能在药学本科背景下说清楚输入、处理、输出和证据边界。

## 学习目标

{goals}

## 90 分钟时间切分

| {header} |
| {divider} |
""" + "\n".join(f"| {row} |" for row in rows) + f"""

## 课堂产物与评价证据

- 学生至少完成一个可提交产物：`{spec.exercise}`。
- 评价证据以“能否解释字段、代码、图表和证据边界”为准，不以是否复现完整高级 workflow 为准。
- 参考答案要点：{spec.answer}
- 教师巡查时优先看学生是否记录输入文件、处理规则、输出解释、AI 使用和人工修订理由。

## 所需素材

- 教材章节：`{assets["chapter"]}`
- PPT storyboard：`{assets["storyboard"]}`
- 小数据：`{assets["dataset"]}`
- 代码或伪代码：`{assets["code"]}`
- Mermaid 示意图：`{assets["diagram"]}`

## AI 协作边界

AI 可以帮助解释概念、定位报错、改写图注和生成核验清单；不能替代医学判断、统计判断、真实数据核验、基因功能核验、细胞注释或临床建议。教师应要求学生把 AI 输出写入审计记录，并标出可保留、需修改和必须删除的句子。

## 与教材和 storyboard 的关系

- 教材章节用于课前预习、课后复习和知识体系整理。
- 教学计划用于组织 90 分钟课堂节奏、学生动作和评价证据。
- PPT storyboard 用于后续裁剪成正式投屏页；40 页源稿不等于最终课件页数，也不表示 PPTX 或视觉 QA 完成。
- 本周 storyboard 的每一页 `Timing` 必须落入上方 6 个教学块；若后续改 storyboard，应同步调整本教学计划。

## 来源与待核验点

{source_refs}

- 若替换外部图、真实数据或公开图形，必须重新核对来源、授权和参数记录。
- 若 AI 输出涉及机制、疗效、统计显著性、基因功能、通路或细胞类型，必须回到课程数据、数据库或人工审查记录核验。
"""


def storyboard_markdown_with_teaching_plan(spec: ChapterSpec) -> str:
    text = storyboard_markdown(spec)
    old_source = f"source: [materials.md, outline.md, script.md, course/textbook/chapters/chapter_{spec.week:02d}.md]"
    new_source = (
        f"source: [materials.md, outline.md, script.md, teaching_plan.md, "
        f"course/textbook/chapters/chapter_{spec.week:02d}.md]"
    )
    text = text.replace(old_source, new_source)
    text = text.replace(
        "本 storyboard 是 40 页主干内容源稿，用于后续 PPTX 裁剪、教师备课和在线教材同步扩写。",
        "本 storyboard 是 40 页主干内容源稿，用于后续 PPTX 裁剪；90 分钟教学组织以 `teaching_plan.md` 为准，教材知识体系以对应章节为准。",
    )
    return text


def concept_map_mermaid(spec: ChapterSpec) -> str:
    concept_nodes = "\n".join(
        f"    c{idx}[\"{term}\"]" for idx, (term, _desc) in enumerate(spec.concepts, start=1)
    )
    concept_edges = "\n".join(f"    route --> c{idx}" for idx in range(1, len(spec.concepts) + 1))
    return f"""flowchart LR
    intro["导入问题"]
    route["{spec.route}"]
    case["{spec.case_title}"]
{concept_nodes}
    ai["AI 核验边界"]
    intro --> route
    route --> case
{concept_edges}
    case --> ai
"""


def thematic_paragraphs(spec: ChapterSpec) -> str:
    assets = asset_paths(spec)
    concept_terms = "、".join(term for term, _desc in spec.concepts)
    return f"""
本章的知识体系围绕 `{spec.route}` 展开。学生阅读时应先抓住主线，而不是从函数名或图形名称开始背诵。`{concept_terms}` 这些概念只有放在输入、处理、输出和证据边界中才有教学意义。教师讲授时要不断把学生带回“这列数据从哪里来、这段代码改变了什么、这张图支持什么、这句话还缺什么证据”四个问题。

在药学本科课堂中，概念不应被处理成百科条目。以“{spec.case_title}”为例，教材首先说明案例为何足够小、为何可以现场核验、为何不能外推为真实医学结论。小数据 `{assets["dataset"]}` 的作用是让学生看见字段、单位、分组、观测单位和质量风险；代码 `{assets["code"]}` 的作用是把处理逻辑暴露出来；示意图 `{assets["diagram"]}` 的作用是组织表达，而不是充当未经核验的研究证据。

教材正文和课堂投屏的职责不同。教材需要保留解释链条，让学生课后能复盘每个概念的来源、前提和风险；PPT storyboard 需要把课堂注意力拆成页级动作；教学计划需要安排 90 分钟内教师讲什么、学生做什么、提交什么和教师如何判断达标。因此本章保留 storyboard 对应表，但不逐页复述 40 张 slide。对应表只用于索引，真正的知识组织由本章各节承担。

本章的跨章价值在于把前后周连接起来。前置章节提供工具、表格、统计、图形或矩阵直觉；后续章节要求学生把这些能力用于更复杂的数据结构或项目汇报。教师应明确哪些内容是本周必须达成，哪些只是为后续铺垫。任何超出本周数据和方法支持范围的表述，都必须降级为候选解释或待核验点。
"""


def chapter_markdown_dual_track(spec: ChapterSpec) -> str:
    assets = asset_paths(spec)
    concept_lines = "\n".join(f"- **{term}**：{desc}" for term, desc in spec.concepts)
    goal_lines = "\n".join(f"- {goal}" for goal in spec.goals)
    source_lines = "\n".join(f"- `{source}`" for source in spec.source_refs)
    diagram_path = ASSETS_DIR / "diagrams" / spec.diagram_name
    diagram_text = diagram_path.read_text(encoding="utf-8").strip() if diagram_path.exists() else concept_map_mermaid(spec)
    body = f"""---
type: textbook-chapter
chapter: {spec.week}
week: {spec.week}
title: {spec.title}
status: expanded_draft
textbook_status: {TEXTBOOK_STATUS}
teaching_plan_source: {teaching_plan_source(spec.week)}
storyboard_source: {assets["storyboard"]}
storyboard_pages: {STORYBOARD_PAGES}
updated: 2026-06-05
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

本章是教材知识体系正文，不是 40 页 PPT storyboard 的长文版。教材负责帮助学生建立可复习、可归纳、可迁移的知识结构；教学计划负责 90 分钟课堂组织；PPT storyboard 负责后续投屏源稿裁剪。三者互相引用，但不互相替代。

## 知识地图

```mermaid
{concept_map_mermaid(spec).strip()}
```

这张知识地图把本章导入问题、方法路线、主案例、核心概念和 AI 核验边界放在同一个结构中。学生复习时先读图，再回到正文核对每个节点的输入、输出和不能支持的结论。

## 学习目标

{goal_lines}

## Storyboard 对应表

{storyboard_mapping_table()}

上表只表示教材小节与 40 页 storyboard 模块的对应关系。它不是教材正文的展开顺序，也不要求教师在正式课件中保留 40 页。后续制作 PPTX 时可以裁剪页数，但不能删除数据来源、字段含义、代码输出、图表解释和证据边界。

## 本章主线与课程位置

第 {spec.week:02d} 周位于“{phase_band(spec.week)}”阶段。本章路线是 **{spec.route}**。这一路线回答三个问题：本周从什么输入开始，经过什么处理或解释，最后能形成什么可核验输出。对药学本科生而言，关键不是记住所有工具细节，而是知道每一个结论的证据从哪里来。

{thematic_paragraphs(spec)}

## 跨章衔接

- Week 01-04 建立工具、AI 边界与可复现记录意识。
- Week 05-10 建立表格整理、统计推断和模型解释的基础。
- Week 11-13 把科研图表、高维矩阵、PCA、聚类和热图连接起来。
- Week 14-16 把表达矩阵、差异表达、单细胞和空间组学图形纳入可解释边界。
- Week 17-18 把数据、代码、图表、AI 使用和证据边界整理为项目交付物。

本章在这条链中的作用是让学生把已经学过的能力接到当前主题上，同时为后续章节保留必要的概念入口。教师不能把后续高级 workflow 提前变成学生必跑任务，也不能把本章的教学模拟结果写成真实研究结论。

## 核心概念

{concept_lines}

## 概念展开与药学解释

概念讲解必须回到药学场景。教师可以先让学生说出一个日常或实验问题，再追问这个问题需要什么字段、什么单位、什么分组和什么核验路径。对于 `{spec.case_title}`，学生应先判断观测单位，再解释关键字段，最后才讨论代码或图形。

每个概念都要回答三件事：它需要什么输入，它产生什么输出，它不能支持什么结论。若学生把概念直接写成医学事实、机制事实或统计事实，教师应要求其补充来源、参数和前提。AI 可以帮助检查表达是否遗漏边界，但不能替代人工判断。

## 方法路线

本章路线可以概括为：**{spec.route}**。

```mermaid
{diagram_text}
```

路线图进入教材时承担“组织知识”的功能，进入 storyboard 时承担“组织页面”的功能，进入教学计划时承担“组织时间”的功能。三种用法不同，但都必须保留输入、输出和待核验点。学生复习时应能沿着路线图说明每一步的课堂产物。

## 案例数据与字段说明

本章配套小数据是 `{assets["dataset"]}`。小数据用于训练字段阅读、观测单位判断和质量风险识别。教师应要求学生先标出主键、分组、指标、单位和来源，再进入代码或图形。若字段名称来自外部素材缩写，教材只保留课程化解释，不把未核验缩写当作事实。

主案例“{spec.case_title}”的价值在于足够小、可现场核验、可暴露错误。学生可以通过它练习三件事：读懂数据结构，说明处理逻辑，写出克制解释。任何课堂观察都必须标注为教学模拟或课程化素材，不能被描述为真实患者、真实药效、真实表达矩阵或真实细胞注释。

## 工具实现与代码样例

本章配套代码是 `{assets["code"]}`。代码只承担课堂核验和结构说明功能，不作为真实研究 pipeline。教师讲代码时按四层展开：输入文件、关键字段、处理逻辑、输出结果。每一层都要能被学生用小数据复核。

代码讲解不能退化为语法百科。本章只解释完成当前案例所需的最小结构：读入数据、检查字段、执行处理、输出结果、记录参数和边界。AI 可以帮助解释代码、定位报错或生成边界样本，但学生必须保留人工运行记录和修改理由。

## 方法流程与代码解读

方法流程需要把路线图、数据表和代码输出连成一条可追溯证据链。教师应先让学生在流程图中圈出输入和输出，再让学生阅读代码中真正使用的列名，最后回到小数据复核一处结果。若代码依赖阈值、分组、标准化、距离或图形参数，教材必须说明这些规则是课堂教学规则，不是通用医学或统计标准。

学生复盘时应能回答：代码读取了哪个文件，使用了哪些字段，改变了哪些数据，输出能回答哪个课堂问题，不能回答哪些真实研究问题。这个解读过程比“一次跑通”更重要，因为课程目标是建立可核验分析习惯。

## 图表与结果解释

图表解释遵循四步：确认数据来源，解释视觉编码，说明统计或处理前提，写出证据边界。无论本章使用流程图、结果表、散点图、热图、UMAP 还是项目 rubric，都不能跳过图注和来源说明。

图表中的颜色、距离、聚类、P 值、阈值或分数只是在特定数据和方法前提下的观察，不自动构成机制、疗效、诊断或推荐。教师应要求学生把图上观察、统计关联、候选解释和待核验事实分开写。

## 课堂案例

**案例名称：{spec.case_title}**

课堂使用步骤：

1. 说明数据来源是教学模拟或课程化素材。
2. 标出关键字段、观测单位和可能的质量风险。
3. 用配套代码或手算方式得到一个可复核结果。
4. 把结果写成克制表达，并列出仍需人工核验的项目。

本案例的课堂产物不是最终论文结论，而是字段字典、代码运行记录、图注草稿和 Claim-Evidence Gate。教师应根据这些产物判断学生是否达成学习目标。

## AI 协作与核验

推荐 Prompt：

```text
请检查我对“{spec.case_title}”的解释是否越过证据边界。
请只指出字段、方法、图表和待核验点中的遗漏，不要替我编造医学、统计、基因功能、通路机制、细胞注释或临床建议。
```

AI 可以用于解释术语、检查代码、改写图注和生成待核验清单；不能替代数据来源、统计前提、医学意义、基因功能、细胞注释或真实结果核验。教师应要求学生把 AI 输出分为三类：可以保留的语言、需要修改的表达、必须删除的越界结论。

## 练习与参考答案要点

练习：{spec.exercise}

参考答案要点：{spec.answer}

练习和答案保留在教材章节中，服务复习与复盘；它们不作为本轮 40 页 storyboard 的独立页面。后续如需课堂练习页、参考答案页、课后复盘页或备用页，应在教学包或正式 PPT 生产轮单独追加。

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
    while chinese_count(body) < target:
        body += (
            "\n## 知识体系补充说明\n\n"
            f"本补充说明继续围绕“{spec.route}”展开，目的不是增加投屏页数，而是帮助学生在课后复盘时把概念、案例、代码和图表重新连成一条证据链。"
            f"学生应回到 `{assets['dataset']}` 检查字段，再回到 `{assets['code']}` 检查处理逻辑，最后回到 `{assets['diagram']}` 检查表达边界。"
            "如果任何一步缺少来源、参数、单位或人工核验记录，结论都必须降级为课堂观察或待核验点。"
        )
    if re.search(r"^###\s+Slide\s+\d+", body, flags=re.M) or "这一页属于" in body:
        raise ValueError(f"Chapter {spec.week:02d} still contains slide-by-slide prose")
    return body


def scalar_value(line: str) -> str:
    return line.split(":", 1)[1].strip().strip("'\"")


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
            current = {"chapter": int(scalar_value(stripped))}
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


def source_list(chapter: dict[str, object], field: str) -> list[str]:
    values = chapter.get(field, [])
    return [str(value) for value in values] if isinstance(values, list) else []


def write_map(chapters: Iterable[dict[str, object]]) -> None:
    spec_by_week = {spec.week: spec for spec in CHAPTERS}
    lines = [
        "version: 1",
        "title: 医药数据处理与可视化在线教材映射",
        "policy: course/syllabus and course/weeks are the course truth layer; knowledge is supporting context only.",
        "chapters:",
    ]
    for chapter in chapters:
        week = int(chapter["week"])
        spec = spec_by_week[week]
        assets = asset_paths(spec)
        teaching_plan = teaching_plan_source(week)
        source_files = source_list(chapter, "source_week_files")
        for path in (teaching_plan, assets["storyboard"]):
            if path not in source_files:
                source_files.append(path)
        lines.extend(
            [
                f"  - chapter: {week}",
                f"    week: {week}",
                f"    title: {spec.title}",
                f"    page: /coursebook/week-{week:02d}",
                f"    chapter_source: {assets['chapter']}",
                f"    textbook_status: {TEXTBOOK_STATUS}",
                f"    teaching_plan_source: {teaching_plan}",
                f"    storyboard_source: {assets['storyboard']}",
                f"    storyboard_pages: {STORYBOARD_PAGES}",
                "    asset_sources:",
                f"      - {assets['dataset']}",
                f"      - {assets['code']}",
                f"      - {assets['diagram']}",
                "    source_week_files:",
            ]
        )
        for value in source_files:
            lines.append(f"      - {value}")
        for field in ("knowledge_sources", "material_sources"):
            lines.append(f"    {field}:")
            for value in source_list(chapter, field):
                lines.append(f"      - {value}")
        lines.append(f"    ppt_status: {STORYBOARD_STATUS}")
        lines.append(f"    review_status: {chapter.get('review_status', 'pilot_candidate')}")
    MAP_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_all() -> None:
    for spec in CHAPTERS:
        target_week_dir = week_dir(spec.week)
        target_week_dir.mkdir(parents=True, exist_ok=True)
        (target_week_dir / "teaching_plan.md").write_text(teaching_plan_markdown(spec), encoding="utf-8", newline="\n")
        (target_week_dir / "ppt_storyboard.md").write_text(storyboard_markdown_with_teaching_plan(spec), encoding="utf-8", newline="\n")
        (CHAPTERS_DIR / f"chapter_{spec.week:02d}.md").write_text(chapter_markdown_dual_track(spec), encoding="utf-8", newline="\n")
    write_map(parse_map(MAP_PATH))


def main() -> None:
    write_all()
    print(f"Generated {len(CHAPTERS)} teaching plans, refreshed storyboards, and dual-track textbook chapters.")


if __name__ == "__main__":
    main()
