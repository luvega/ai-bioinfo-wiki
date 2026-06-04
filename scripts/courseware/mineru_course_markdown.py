"""Create course-facing Markdown cards from MinerU and AIDD Markdown/text.

The complete OCR/structure-preserving output remains in ``book.mineru.md``.
This script creates a smaller derivative, ``book.course.md``, for lesson
planning: heading outline, course-week mapping, short teaching highlights,
formula/code/example/image markers, and a structure report.

It also indexes the AIDD Bioinformatics txt lectures under
``materials/markdown/aidd_bioinformatics`` so the courseware stage does not
miss the subtitle-derived lecture notes.
"""
from __future__ import annotations

from collections import defaultdict
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MINERU_ROOT = ROOT / "materials" / "markdown" / "pdf_library_mineru"
AIDD_ROOT = ROOT / "materials" / "markdown" / "aidd_bioinformatics"
MAX_OUTLINE_ITEMS = 1200
MAX_SECTION_CARDS = 120
MAX_SNIPPET_CHARS = 220

COURSE_WEEKS = {
    1: "课程导论、医药数据类型与 AI 协作框架",
    2: "数据分析流程、复现规范与人机协作规范",
    3: "AI 辅助编程与 Python 快速入门",
    4: "R 基础语法、数据框操作与 AI 代码核验",
    5: "数据读取与整理",
    6: "缺失值、异常值处理与分组汇总",
    7: "描述统计与分布可视化",
    8: "统计推断基础",
    9: "相关分析与线性回归",
    10: "分类问题与逻辑回归",
    11: "科研图表规范与 SCI 图表表达",
    12: "高维数据与数学直觉",
    13: "PCA、聚类与热图",
    14: "转录组与差异表达分析专题",
    15: "Linux、NGS 流程与变异分析专题",
    16: "公共数据库、微阵列与单细胞拓展",
    17: "综合项目工作坊：AI 协作分析与结果核验",
    18: "项目展示、复盘与课程总结",
}

BOOK_PROFILES = [
    {
        "slug_contains": "Learn_AI_Assisted_Python",
        "position": "AI 辅助 Python 编程教材，适合作为第 3 周 AI 辅助编程和第 17 周综合项目工作流的提示词、测试、调试案例池。",
        "weeks": [3, 17],
    },
    {
        "slug_contains": "Pythonppt",
        "position": "中文 Python 课程 PPT，适合抽取第 3-6 周的 Python 入门、语法、函数、文件和课堂表达方式。",
        "weeks": [3, 5, 6],
    },
    {
        "slug_contains": "Starting_Data_Analytics",
        "position": "GenAI 数据分析工作流教材，适合连接第 2 周复现规范、第 3 周 AI 协作和第 5-10 周数据分析流程。",
        "weeks": [2, 3, 5, 6, 7, 8, 9, 10, 17],
    },
    {
        "slug_contains": "Statistical_Learning_with_Applications_Python",
        "position": "Python 版统计学习教材，适合支撑第 8-13 周统计推断、回归、分类、高维数据、PCA 和聚类。",
        "weeks": [8, 9, 10, 11, 12, 13],
    },
    {
        "slug_contains": "Statistical_Learning_with_Applications_R",
        "position": "R 版统计学习教材，适合支撑第 8-13 周统计学习概念，并为第 4 周 R 语言和第 11 周图表表达提供补充。",
        "weeks": [4, 8, 9, 10, 11, 12, 13],
    },
]

KEYWORD_WEEKS = [
    (3, ["copilot", "chatgpt", "prompt", "ai-assisted", "ai assisted", "python", "doctest", "debug"]),
    (4, [" r ", "r language", "r lab", "r package", "ggplot2"]),
    (5, ["pandas", "dataframe", "read_csv", "loading data", "data import", "读取", "文件"]),
    (6, ["missing", "null", "nan", "groupby", "summar", "异常", "缺失"]),
    (7, ["visualization", "plot", "histogram", "boxplot", "graphics", "可视化", "绘图"]),
    (8, ["inference", "hypothesis", "confidence", "p-value", "statistical learning", "bias-variance"]),
    (9, ["linear regression", "least squares", "regression", "回归"]),
    (10, ["classification", "logistic", "roc", "confusion", "分类"]),
    (11, ["figure", "plot", "graphics", "visual", "ggplot", "heatmap", "图表"]),
    (12, ["high-dimensional", "dimension", "regularization", "lasso", "ridge", "高维"]),
    (13, ["pca", "principal component", "clustering", "cluster", "heatmap", "聚类"]),
    (17, ["project", "workflow", "reproduc", "debug", "test", "collaboration", "项目"]),
]

AIDD_CHAPTER_DEFAULT_WEEKS = {
    1: [1, 3, 4],
    2: [3, 14],
    3: [3, 14, 17],
    4: [15],
    5: [15],
    6: [2, 15],
    7: [14, 15],
    8: [15, 16],
    9: [4, 11, 14, 16],
    10: [16],
    12: [17],
}

AIDD_WEEK_RULES = [
    (1, ["introduction", "biological programming", "bioinformatics"]),
    (2, ["pipeline", "workflow", "reproduc", "project organization"]),
    (3, ["python", "biopython", "tkinter", "application", "sequence analysis", "seqio"]),
    (4, ["r for bioinformatics", " r ", "r package", "deseq2", "ggplot2"]),
    (5, ["database", "retrieval", "sra", "geo", "entrez", "file format", "fasta", "fastq"]),
    (11, ["visualizing", "visualization", "ggplot2", "igv", "ucsc", "plot"]),
    (14, ["rna-seq", "deseq2", "differential", "gene expression", "feature extraction", "single-cell"]),
    (15, ["bash", "linux", "wsl", "ngs", "samtools", "bcftools", "variant calling", "alignment", "fastqc", "trimming"]),
    (16, ["microarray", "geo2r", "scrna-seq", "single-cell", "genome annotation", "proteomics"]),
    (17, ["github", "repository", "fork", "clone", "collaborate", "exe file", "project management"]),
]

AIDD_ENTITY_KEYWORDS = {
    "Biopython": ["biopython", "seqio", "bio.sequtils", "entrez"],
    "FASTA/FASTQ": ["fasta", "fastq"],
    "BLAST": ["blast"],
    "NCBI Entrez": ["entrez", "ncbi e-utilities", "e-utilities"],
    "Galaxy": ["galaxy"],
    "Linux/WSL": ["linux", "wsl", "bash", "shell"],
    "SRA Toolkit": ["sra", "fastq-dump"],
    "samtools": ["samtools", "sam and bam"],
    "bcftools": ["bcftools", "bcf tools"],
    "IGV/UCSC": ["igv", "ucsc"],
    "RNA-seq": ["rna-seq", "gene expression"],
    "DESeq2": ["deseq2", "deseq"],
    "ggplot2": ["ggplot2"],
    "scRNA-seq": ["scrna-seq", "single-cell"],
    "GEO/GEO2R": ["geo2r", "geo"],
    "GitHub": ["github", "repository", "fork", "clone"],
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```([A-Za-z0-9_-]+)?\s*$")
FORMULA_RE = re.compile(r"(\$\$|\\\(|\\\[|\\begin\{|[A-Za-z0-9]\s*=\s*[^=])")
EXAMPLE_RE = re.compile(
    r"\b(example|exercise|lab|case|figure|fig\.|for example|copilot|chatgpt|prompt|doctest)\b|例如|实例|案例|代码|图",
    re.IGNORECASE,
)


@dataclass
class Heading:
    level: int
    text: str
    line_no: int


@dataclass
class CodeBlock:
    language: str
    start_line: int
    lines: list[str]


@dataclass
class BookData:
    slug: str
    title: str
    source_path: Path
    body_lines: list[str]
    headings: list[Heading]
    code_blocks: list[CodeBlock]
    image_lines: list[str]
    table_lines: list[str]
    formula_lines: list[str]
    noisy_lines: list[tuple[int, str]]


@dataclass
class AiddLesson:
    path: Path
    rel_path: str
    chapter_no: int
    chapter_title: str
    lesson_no: float
    lesson_title: str
    duration_minutes: float
    body: str
    char_count: int
    weeks: list[int]
    entities: list[str]
    snippets: list[str]


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, body


def normalize_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_float(value: str, default: float = 0.0) -> float:
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return default


def parse_int(value: str, default: int = 0) -> int:
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return default


def truncate(text: str, limit: int = MAX_SNIPPET_CHARS) -> str:
    text = normalize_text(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def is_noise(text: str) -> bool:
    stripped = normalize_text(text)
    if len(stripped) > 800:
        return True
    if "t h e" in stripped and "p r o m p t" in stripped:
        return True
    chars = [c for c in stripped if c.isalpha()]
    if len(chars) > 120:
        spaced_letters = len(re.findall(r"\b[A-Za-z]\b", stripped))
        if spaced_letters / max(len(chars), 1) > 0.35:
            return True
    return False


def parse_book(path: Path) -> BookData:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_front_matter(text)
    lines = body.splitlines()
    slug = path.parent.name
    title = meta.get("title") or slug
    headings: list[Heading] = []
    code_blocks: list[CodeBlock] = []
    image_lines: list[str] = []
    table_lines: list[str] = []
    formula_lines: list[str] = []
    noisy_lines: list[tuple[int, str]] = []

    in_code = False
    code_lang = ""
    code_start = 0
    code_lines: list[str] = []

    for idx, line in enumerate(lines, start=1):
        fence = FENCE_RE.match(line)
        if fence:
            if in_code:
                code_blocks.append(CodeBlock(language=code_lang, start_line=code_start, lines=code_lines))
                in_code = False
                code_lang = ""
                code_lines = []
            else:
                in_code = True
                code_lang = fence.group(1) or ""
                code_start = idx
                code_lines = []
            continue
        if in_code:
            code_lines.append(line)
            continue

        match = HEADING_RE.match(line)
        if match:
            headings.append(Heading(level=len(match.group(1)), text=normalize_text(match.group(2)), line_no=idx))
        if IMAGE_RE.search(line):
            image_lines.append(line)
        if line.strip().startswith("|") and line.count("|") >= 2:
            table_lines.append(line)
        if FORMULA_RE.search(line) and len(normalize_text(line)) <= 260:
            formula_lines.append(line)
        if is_noise(line):
            noisy_lines.append((idx, line))

    return BookData(
        slug=slug,
        title=title,
        source_path=path,
        body_lines=lines,
        headings=headings,
        code_blocks=code_blocks,
        image_lines=image_lines,
        table_lines=table_lines,
        formula_lines=formula_lines,
        noisy_lines=noisy_lines,
    )


def profile_for(slug: str) -> tuple[str, list[int]]:
    for profile in BOOK_PROFILES:
        if profile["slug_contains"] in slug:
            return str(profile["position"]), list(profile["weeks"])
    return "课程参考资料，需按章节进一步判断可进入的周次。", [3, 17]


def infer_weeks(text: str, default_weeks: list[int]) -> list[int]:
    normalized = f" {text.lower()} "
    weeks = set(default_weeks)
    for week, keywords in KEYWORD_WEEKS:
        if any(keyword in normalized for keyword in keywords):
            weeks.add(week)
    return sorted(weeks)


def infer_aidd_weeks(chapter_no: int, text: str) -> list[int]:
    normalized = f" {text.lower()} "
    weeks = set(AIDD_CHAPTER_DEFAULT_WEEKS.get(chapter_no, [17]))
    for week, keywords in AIDD_WEEK_RULES:
        if any(keyword in normalized for keyword in keywords):
            weeks.add(week)
    return sorted(weeks)


def format_weeks(weeks: list[int]) -> str:
    return ", ".join(f"第 {week} 周" for week in weeks)


def extract_entities(text: str) -> list[str]:
    normalized = f" {text.lower()} "
    entities: list[str] = []
    for entity, keywords in AIDD_ENTITY_KEYWORDS.items():
        if any(keyword in normalized for keyword in keywords):
            entities.append(entity)
    return entities[:8]


def split_sentences(text: str) -> list[str]:
    cleaned = normalize_text(text)
    pieces = re.split(r"(?<=[。！？.!?])\s+", cleaned)
    return [piece.strip() for piece in pieces if len(piece.strip()) >= 30]


def extract_aidd_snippets(body: str, entities: list[str]) -> list[str]:
    sentences = split_sentences(body)
    if not sentences:
        return []
    entity_terms = [term.lower() for entity in entities for term in AIDD_ENTITY_KEYWORDS.get(entity, [entity])]

    def score(sentence: str) -> tuple[int, int]:
        lower = sentence.lower()
        hits = sum(1 for term in entity_terms if term in lower)
        teaching_hits = sum(
            1
            for term in ["example", "code", "data", "analysis", "pipeline", "workflow", "使用", "分析", "数据", "代码", "流程"]
            if term in lower
        )
        return hits + teaching_hits, min(len(sentence), 220)

    ranked = sorted(sentences, key=score, reverse=True)
    snippets: list[str] = []
    seen: set[str] = set()
    for sentence in ranked:
        short = truncate(sentence, 180)
        if short in seen:
            continue
        seen.add(short)
        snippets.append(short)
        if len(snippets) >= 2:
            break
    return snippets


def parse_aidd_lesson(path: Path) -> AiddLesson:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_front_matter(text)
    body_lines = body.splitlines()
    if body_lines and body_lines[0].startswith("# "):
        body = "\n".join(body_lines[1:]).strip()
    rel_path = path.relative_to(AIDD_ROOT).as_posix()
    chapter_no = parse_int(meta.get("chapter_no", "0"))
    lesson_no = parse_float(meta.get("lesson_no", "0"))
    chapter_title = meta.get("chapter_title") or path.parent.name
    lesson_title = meta.get("lesson_title") or path.stem.replace("_", " ")
    duration = parse_float(meta.get("duration_minutes", "0"))
    lookup_text = f"{chapter_title} {lesson_title} {body[:5000]}"
    weeks = infer_aidd_weeks(chapter_no, lookup_text)
    entities = extract_entities(lookup_text)
    snippets = extract_aidd_snippets(body, entities)
    return AiddLesson(
        path=path,
        rel_path=rel_path,
        chapter_no=chapter_no,
        chapter_title=chapter_title,
        lesson_no=lesson_no,
        lesson_title=lesson_title,
        duration_minutes=duration,
        body=body,
        char_count=len(body),
        weeks=weeks,
        entities=entities,
        snippets=snippets,
    )


def week_table(weeks: list[int]) -> list[str]:
    rows = ["| 周次 | 课程主题 |", "|---:|---|"]
    for week in weeks:
        title = COURSE_WEEKS.get(week, "待补充")
        rows.append(f"| {week} | {title} |")
    return rows


def collect_paragraphs(lines: list[str]) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    in_code = False
    for line in lines:
        if FENCE_RE.match(line):
            in_code = not in_code
            if current:
                paragraphs.append(normalize_text(" ".join(current)))
                current = []
            continue
        if in_code:
            continue
        if HEADING_RE.match(line) or IMAGE_RE.search(line) or line.strip().startswith("|"):
            if current:
                paragraphs.append(normalize_text(" ".join(current)))
                current = []
            continue
        if not line.strip():
            if current:
                paragraphs.append(normalize_text(" ".join(current)))
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append(normalize_text(" ".join(current)))
    return [p for p in paragraphs if len(p) >= 30 and not is_noise(p)]


def section_ranges(book: BookData) -> list[tuple[Heading, int, int]]:
    if not book.headings:
        return []
    major = [h for h in book.headings if h.level <= 2]
    if len(major) < 5:
        major = [h for h in book.headings if h.level <= 3]
    ranges: list[tuple[Heading, int, int]] = []
    for idx, heading in enumerate(major):
        next_line = len(book.body_lines) + 1
        for later in major[idx + 1 :]:
            if later.line_no > heading.line_no and later.level <= heading.level:
                next_line = later.line_no
                break
        ranges.append((heading, heading.line_no, next_line))
    return ranges


def extract_code_for_range(book: BookData, start: int, end: int) -> list[str]:
    snippets: list[str] = []
    for block in book.code_blocks:
        if not (start <= block.start_line < end):
            continue
        lang = block.language or "text"
        nonempty = [line for line in block.lines if line.strip()]
        if not nonempty:
            continue
        if lang.lower() == "mermaid" and sum(len(line) for line in nonempty) > 1200:
            snippets.append(f"Mermaid/流程图代码块较长，源行 {block.start_line}，建议回到 `book.mineru.md` 人工清理。")
            continue
        preview = " / ".join(truncate(line, 90) for line in nonempty[:4])
        snippets.append(f"`{lang}` 代码块，源行 {block.start_line}：{preview}")
        if len(snippets) >= 3:
            break
    return snippets


def extract_markers_for_range(book: BookData, start: int, end: int) -> dict[str, list[str]]:
    lines = book.body_lines[start - 1 : end - 1]
    paragraphs = collect_paragraphs(lines)
    highlights = [truncate(p) for p in paragraphs[:3]]
    examples = [truncate(p) for p in paragraphs if EXAMPLE_RE.search(p)][:3]
    formulas = [truncate(line) for line in lines if FORMULA_RE.search(line) and len(normalize_text(line)) <= 260][:5]
    images = []
    tables = []
    for line in lines:
        match = IMAGE_RE.search(line)
        if match:
            images.append(f"图片引用：`{match.group(1)}`")
        if line.strip().startswith("|") and line.count("|") >= 2:
            tables.append(f"表格行：{truncate(line, 160)}")
        if len(images) >= 3 and len(tables) >= 3:
            break
    return {
        "highlights": highlights,
        "examples": examples,
        "formulas": formulas[:5],
        "images": images[:3],
        "tables": tables[:3],
        "code": extract_code_for_range(book, start, end),
    }


def outline_lines(book: BookData) -> tuple[list[str], bool]:
    lines: list[str] = []
    truncated_outline = len(book.headings) > MAX_OUTLINE_ITEMS
    for heading in book.headings[:MAX_OUTLINE_ITEMS]:
        indent = "  " * max(heading.level - 1, 0)
        lines.append(f"{indent}- H{heading.level} L{heading.line_no}: {heading.text}")
    if truncated_outline:
        lines.append(f"- ... 已截断，完整标题数 {len(book.headings)}。")
    return lines, truncated_outline


def write_course_markdown(book: BookData) -> tuple[Path, Path]:
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    position, default_weeks = profile_for(book.slug)
    all_text_for_weeks = " ".join(h.text for h in book.headings[:80])
    recommended_weeks = infer_weeks(f"{book.title} {all_text_for_weeks}", default_weeks)
    outline, outline_truncated = outline_lines(book)
    ranges = section_ranges(book)
    cards = ranges[:MAX_SECTION_CARDS]
    cards_truncated = len(ranges) > MAX_SECTION_CARDS

    rel_source = book.source_path.relative_to(book.source_path.parent).as_posix()
    course_lines = [
        "---",
        "type: course-source",
        f"title: {book.title}",
        f"source_mineru: {rel_source}",
        f"generated: {generated}",
        "status: generated_draft",
        "tags: [mineru, course-material, auto-extract]",
        "---",
        "",
        f"# {book.title} · 课程化整理",
        "",
        "## 使用说明",
        "",
        "本文件由 `book.mineru.md` 自动整理生成，服务于 36 课时课程备课。它不是原书全文，也不替代人工核验；完整解析结果请回到 `book.mineru.md`。",
        "",
        "## 一句话定位",
        "",
        position,
        "",
        "## 推荐进入课程的周次",
        "",
        *week_table(recommended_weeks),
        "",
        "## 章节层级索引",
        "",
        *outline,
        "",
        "## 自动抽取的教学卡片",
        "",
    ]

    if cards_truncated:
        course_lines.extend(
            [
                f"> [!todo] 本书候选大节共有 {len(ranges)} 个，本文件先生成前 {MAX_SECTION_CARDS} 个教学卡片；完整层级见上方索引。",
                "",
            ]
        )

    for idx, (heading, start, end) in enumerate(cards, start=1):
        section_text = " ".join(book.body_lines[start - 1 : min(end - 1, start + 160)])
        weeks = infer_weeks(f"{heading.text} {section_text}", default_weeks)
        markers = extract_markers_for_range(book, start, end)
        course_lines.extend(
            [
                f"### {idx}. {heading.text}",
                "",
                f"- 原始层级：H{heading.level}，源行：L{heading.line_no}",
                f"- 推荐周次：{', '.join(f'第 {week} 周' for week in weeks)}",
                "",
                "#### 核心重点",
                "",
            ]
        )
        if markers["highlights"]:
            for item in markers["highlights"]:
                course_lines.append(f"- {item}")
        else:
            course_lines.append("- 待人工核验：该节可读段落较少，建议回到 `book.mineru.md` 查看原文。")

        course_lines.extend(["", "#### 公式与符号", ""])
        if markers["formulas"]:
            for item in markers["formulas"]:
                course_lines.append(f"- {item}")
        else:
            course_lines.append("- 未在本节自动识别到明显公式。")

        course_lines.extend(["", "#### 例子 / 代码 / 图表", ""])
        combined = markers["examples"] + markers["code"] + markers["images"] + markers["tables"]
        if combined:
            for item in combined[:8]:
                course_lines.append(f"- {item}")
        else:
            course_lines.append("- 未在本节自动识别到明显例子、代码或图表。")

        course_lines.extend(
            [
                "",
                "#### 备课摘取建议",
                "",
                f"- 若用于 PPT，可把本节作为「{heading.text}」的概念或案例素材；正式进入讲稿前需核对公式、代码和图表是否被 MinerU 正确解析。",
                "",
            ]
        )

    course_path = book.source_path.parent / "book.course.md"
    course_path.write_text("\n".join(course_lines).rstrip() + "\n", encoding="utf-8")

    warning_lines: list[str] = []
    if book.noisy_lines:
        warning_lines.append(f"- 检测到 {len(book.noisy_lines)} 行疑似 OCR/版式噪声。")
    if outline_truncated:
        warning_lines.append(f"- 标题数 {len(book.headings)} 超过索引展示上限 {MAX_OUTLINE_ITEMS}。")
    if cards_truncated:
        warning_lines.append(f"- 教学卡片数已从 {len(ranges)} 截断到 {MAX_SECTION_CARDS}。")
    if not book.formula_lines:
        warning_lines.append("- 未检测到明显公式行；如该书应含公式，需要抽样核验 MinerU 输出。")
    if not warning_lines:
        warning_lines.append("- 未发现阻塞性结构问题；仍需人工抽样核验。")

    report_lines = [
        "---",
        "type: structure-report",
        f"title: {book.title} MinerU structure report",
        f"source_mineru: {rel_source}",
        f"generated: {generated}",
        "status: generated",
        "---",
        "",
        f"# {book.title} · 结构报告",
        "",
        "## 生成文件",
        "",
        "- `book.mineru.md`：MinerU 原始提升版。",
        "- `book.course.md`：课程化整理版。",
        "",
        "## 统计",
        "",
        f"- 原始行数：{len(book.body_lines)}",
        f"- 标题数：{len(book.headings)}",
        f"- 候选大节数：{len(ranges)}",
        f"- 已生成教学卡片：{len(cards)}",
        f"- 代码块数：{len(book.code_blocks)}",
        f"- 图片引用数：{len(book.image_lines)}",
        f"- 表格行数：{len(book.table_lines)}",
        f"- 公式线索数：{len(book.formula_lines)}",
        f"- 噪声行数：{len(book.noisy_lines)}",
        "",
        "## 警告与核验点",
        "",
        *warning_lines,
        "",
        "## 下一步",
        "",
        "- 抽样核验 `book.course.md` 中每个拟进入 PPT 的章节。",
        "- 对公式、代码、复杂流程图和表格回查 `book.mineru.md`。",
        "- 将确认可用的内容写入对应 `course/weeks/week_xx/materials.md`。",
    ]
    report_path = book.source_path.parent / "structure_report.md"
    report_path.write_text("\n".join(report_lines).rstrip() + "\n", encoding="utf-8")
    return course_path, report_path


def aidd_lesson_card(lesson: AiddLesson) -> list[str]:
    entity_text = ", ".join(lesson.entities) if lesson.entities else "待人工标注"
    lines = [
        f"### {lesson.lesson_no:g}. {lesson.lesson_title}",
        "",
        f"- 源文件：`{lesson.rel_path}`",
        f"- 时长：{lesson.duration_minutes:g} 分钟；正文字符数：{lesson.char_count}",
        f"- 推荐周次：{format_weeks(lesson.weeks)}",
        f"- 关键词/实体：{entity_text}",
        "- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。",
        "",
        "#### 回查片段",
        "",
    ]
    if lesson.snippets:
        for snippet in lesson.snippets:
            lines.append(f"- {snippet}")
    else:
        lines.append("- 待人工回查：本讲未自动抽到稳定片段。")
    lines.append("")
    return lines


def write_aidd_materials() -> list[dict[str, str]]:
    if not AIDD_ROOT.exists():
        return []

    txt_paths = sorted(path for path in AIDD_ROOT.rglob("*.txt") if path.is_file())
    lessons = [parse_aidd_lesson(path) for path in txt_paths]
    lessons.sort(key=lambda item: (item.chapter_no, item.lesson_no, item.rel_path))

    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    by_chapter: dict[tuple[int, str], list[AiddLesson]] = defaultdict(list)
    by_week: dict[int, list[AiddLesson]] = defaultdict(list)
    for lesson in lessons:
        by_chapter[(lesson.chapter_no, lesson.chapter_title)].append(lesson)
        for week in lesson.weeks:
            by_week[week].append(lesson)

    generated_files: list[dict[str, str]] = []
    chapter_summaries: list[tuple[int, str, int, float, str, Path]] = []

    for (chapter_no, chapter_title), chapter_lessons in sorted(by_chapter.items()):
        chapter_dir = chapter_lessons[0].path.parent
        chapter_path = chapter_dir / "chapter.course.md"
        chapter_weeks = sorted({week for lesson in chapter_lessons for week in lesson.weeks})
        duration_total = sum(lesson.duration_minutes for lesson in chapter_lessons)
        chapter_lines = [
            "---",
            "type: course-source-chapter",
            f"title: AIDD Chapter {chapter_no}: {chapter_title}",
            f"chapter_no: {chapter_no}",
            f"generated: {generated}",
            "status: generated_draft",
            "tags: [aidd, bioinformatics, course-material, auto-extract]",
            "---",
            "",
            f"# AIDD Chapter {chapter_no}: {chapter_title}",
            "",
            "## 课程定位",
            "",
            f"本章来自 AIDD Bioinformatics 字幕清理讲义，适合映射到 {format_weeks(chapter_weeks)}。它是 PDF 教材之外的生信场景素材层。",
            "",
            "## 讲义清单",
            "",
            "| 课次 | 标题 | 时长 | 推荐周次 | 关键词/实体 | 源文件 |",
            "|---:|---|---:|---|---|---|",
        ]
        for lesson in chapter_lessons:
            entity_text = ", ".join(lesson.entities[:5]) if lesson.entities else "待标注"
            chapter_lines.append(
                f"| {lesson.lesson_no:g} | {lesson.lesson_title} | {lesson.duration_minutes:g} | {format_weeks(lesson.weeks)} | {entity_text} | `{lesson.rel_path}` |"
            )
        chapter_lines.extend(["", "## 逐讲义素材卡", ""])
        for lesson in chapter_lessons:
            chapter_lines.extend(aidd_lesson_card(lesson))
        chapter_path.write_text("\n".join(chapter_lines).rstrip() + "\n", encoding="utf-8")
        generated_files.append(
            {
                "kind": "aidd-chapter",
                "path": chapter_path.relative_to(ROOT).as_posix(),
            }
        )
        chapter_summaries.append(
            (
                chapter_no,
                chapter_title,
                len(chapter_lessons),
                duration_total,
                format_weeks(chapter_weeks),
                chapter_path,
            )
        )

    index_path = AIDD_ROOT / "aidd.course_index.md"
    index_lines = [
        "---",
        "type: course-source-index",
        "title: AIDD Bioinformatics 课程素材索引",
        f"generated: {generated}",
        "status: generated_draft",
        "tags: [aidd, bioinformatics, course-material, auto-extract]",
        "---",
        "",
        "# AIDD Bioinformatics 课程素材索引",
        "",
        "## 使用说明",
        "",
        "本索引从 `materials/markdown/aidd_bioinformatics` 下的 txt 讲义自动生成，用于和 PDF 的 `book.course.md` 一起服务 36 课时备课。txt 原文不改写；本文件只做路径、周次、关键词和短片段索引。",
        "",
        "## 章节总览",
        "",
        "| 章 | 标题 | 讲义数 | 总时长(分钟) | 推荐周次 | 课程化文件 |",
        "|---:|---|---:|---:|---|---|",
    ]
    for chapter_no, chapter_title, lesson_count, duration_total, weeks, chapter_path in chapter_summaries:
        rel_chapter = chapter_path.relative_to(AIDD_ROOT).as_posix()
        index_lines.append(
            f"| {chapter_no} | {chapter_title} | {lesson_count} | {duration_total:.1f} | {weeks} | [{rel_chapter}]({rel_chapter}) |"
        )

    index_lines.extend(["", "## 按 36 课时周次映射", ""])
    for week in sorted(by_week):
        lessons_for_week = by_week[week][:12]
        index_lines.extend([f"### 第 {week} 周：{COURSE_WEEKS.get(week, '待补充')}", ""])
        for lesson in lessons_for_week:
            index_lines.append(f"- `{lesson.rel_path}` — {lesson.lesson_title}")
        if len(by_week[week]) > len(lessons_for_week):
            index_lines.append(f"- ... 另有 {len(by_week[week]) - len(lessons_for_week)} 条讲义，详见对应 `chapter.course.md`。")
        index_lines.append("")

    index_lines.extend(
        [
            "## 全量讲义表",
            "",
            "| 章 | 课次 | 标题 | 时长 | 推荐周次 | 关键词/实体 | 源文件 |",
            "|---:|---:|---|---:|---|---|---|",
        ]
    )
    for lesson in lessons:
        entity_text = ", ".join(lesson.entities[:5]) if lesson.entities else "待标注"
        index_lines.append(
            f"| {lesson.chapter_no} | {lesson.lesson_no:g} | {lesson.lesson_title} | {lesson.duration_minutes:g} | {format_weeks(lesson.weeks)} | {entity_text} | `{lesson.rel_path}` |"
        )
    index_path.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    generated_files.append({"kind": "aidd-index", "path": index_path.relative_to(ROOT).as_posix()})

    missing_meta = [lesson.rel_path for lesson in lessons if not lesson.chapter_no or not lesson.lesson_title]
    report_path = AIDD_ROOT / "aidd.structure_report.md"
    report_lines = [
        "---",
        "type: structure-report",
        "title: AIDD Bioinformatics txt lecture report",
        f"generated: {generated}",
        "status: generated",
        "---",
        "",
        "# AIDD Bioinformatics txt 讲义结构报告",
        "",
        "## 统计",
        "",
        f"- txt 讲义数：{len(lessons)}",
        f"- 章节数：{len(by_chapter)}",
        f"- 总时长：{sum(lesson.duration_minutes for lesson in lessons):.1f} 分钟",
        f"- 总字符数：{sum(lesson.char_count for lesson in lessons)}",
        f"- 生成 chapter.course.md：{len(chapter_summaries)} 个",
        "",
        "## 生成文件",
        "",
        "- `aidd.course_index.md`：AIDD 全量讲义课程索引。",
        "- 每个章节目录下的 `chapter.course.md`：逐讲义素材卡。",
        "",
        "## 核验点",
        "",
    ]
    if missing_meta:
        report_lines.append(f"- 有 {len(missing_meta)} 个 txt 缺少完整 front matter，需要人工检查。")
    else:
        report_lines.append("- 所有 txt 均读取到基础 front matter。")
    report_lines.extend(
        [
            "- AIDD 文本由字幕清理而来，可能保留机翻或口语化噪声；进入 PPT 前需核对术语、命令和软件名。",
            "- AIDD 索引用于补足生信案例层，不替代 PDF 教材的统计学习和 AI 编程材料。",
        ]
    )
    report_path.write_text("\n".join(report_lines).rstrip() + "\n", encoding="utf-8")
    generated_files.append({"kind": "aidd-report", "path": report_path.relative_to(ROOT).as_posix()})
    return generated_files


def main() -> int:
    paths = sorted(MINERU_ROOT.glob("*/book.mineru.md"))
    if not paths:
        raise SystemExit(f"No book.mineru.md files found under {MINERU_ROOT}")
    generated = []
    for path in paths:
        book = parse_book(path)
        course_path, report_path = write_course_markdown(book)
        generated.append(
            {
                "book": book.slug,
                "course": course_path.relative_to(ROOT).as_posix(),
                "report": report_path.relative_to(ROOT).as_posix(),
            }
        )
    for row in generated:
        print(f"{row['book']}: {row['course']} ; {row['report']}")
    for row in write_aidd_materials():
        print(f"{row['kind']}: {row['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
