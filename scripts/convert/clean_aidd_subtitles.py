"""Clean AIDD Bioinformatics subtitles and emit structured plain-text lessons.

Source: G:/医药数据处理与可视化/AIDD Bioinformatics/.../*.srt (WEBVTT content)
Target: materials/raw/aidd_bioinformatics/<chapter>/<lesson>.txt

The pipeline:
  1. Walk the source tree and pick one subtitle per lesson (prefer .srt; the
     paired .vtt is byte-identical so we drop the duplicate).
  2. Strip WEBVTT header, sequence numbers and timecode lines.
  3. Apply a professional-term correction dictionary built from manual review
     of the Chinese machine-translated captions.
  4. Re-flow sentences and merge subtitle line breaks into paragraphs.
  5. Write UTF-8 text with a small YAML front matter so each file is
     self-describing and ready to be ingested by a knowledge-base tool.
  6. Produce INDEX.md with chapter/lesson tables.
"""
from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = Path("G:/医药数据处理与可视化/AIDD Bioinformatics")
OUTPUT_ROOT = ROOT / "materials" / "raw" / "aidd_bioinformatics"
COURSE_DIR_NAME = "Bioinformatics Data Analysis Crash Course Python R and Linux"

# ---------------------------------------------------------------------------
# Professional terminology correction rules.
#
# Each tuple is (pattern, replacement, flags). Order matters: longer/specific
# patterns must come before shorter ones, otherwise partial matches will eat
# the longer context.
#
# Notes on word boundaries: Python's ``\b`` is Unicode-aware, so it does NOT
# match between a Chinese character (which is a word character) and an ASCII
# letter. We therefore use ASCII-only lookarounds ``BL`` / ``BR`` for English
# tokens that need to be matched both at line edges and against Chinese.
# ---------------------------------------------------------------------------
BL = r"(?<![A-Za-z0-9_])"
BR = r"(?![A-Za-z0-9_])"

TERM_RULES: list[tuple[str, str, int]] = [
    # DESeq2 family -------------------------------------------------------
    (BL + r"DSEC\s*2" + BR, "DESeq2", re.IGNORECASE),
    (BL + r"DSEC" + BR, "DESeq2", re.IGNORECASE),
    (BL + r"Deseq\s*2" + BR, "DESeq2", 0),
    (BL + r"Deseq" + BR, "DESeq2", 0),
    # RNA-seq / DNA-seq spellings ---------------------------------------
    (r"RNA[\s-]?(?:SEC|sec|Sec|seq|Seq|测序)", "RNA-seq", 0),
    (r"DNA[\s-]?(?:SEC|sec|Sec|seq|Seq)", "DNA-seq", 0),
    (BL + r"sc\s*RNA[\s-]?seq" + BR, "scRNA-seq", re.IGNORECASE),
    (r"单细胞\s*RNA[\s-]?seq", "单细胞 RNA-seq", 0),
    # FASTQ / FASTA / SAM / BAM ------------------------------------------
    (BL + r"FASCQ" + BR, "FASTQ", 0),
    (BL + r"fasq" + BR, "FASTQ", re.IGNORECASE),
    (BL + r"FASTA[\s-]?A" + BR, "FASTA", 0),
    (BL + r"pasta\s*文件", "FASTA 文件", 0),
    (BL + r"pasta\s*格式", "FASTA 格式", 0),
    # Tool family (Illumina, aligners, samtools, bcftools, etc.) ---------
    (r"氧化铝平台", "Illumina 平台", 0),
    (r"氧化铝读数", "Illumina 测序读段", 0),
    (r"氧化铝", "Illumina", 0),
    (BL + r"LuminaSec" + BR, "Illumina", 0),
    (BL + r"Lumina\s*Sec" + BR, "Illumina", 0),
    (BL + r"PECBio" + BR, "PacBio", 0),
    (BL + r"PEC\s*Bio" + BR, "PacBio", 0),
    (BL + r"Elad" + BR, "Eland", 0),
    (BL + r"Bota" + BR, "Bowtie", 0),
    (BL + r"Mr\.?\s*Fast" + BR, "MrFAST", 0),
    (BL + r"Shreem" + BR, "SHRiMP", 0),
    (BL + r"boros\s*wheeler" + BR, "Burrows-Wheeler", re.IGNORECASE),
    (BL + r"Burrows\s+Wheeler" + BR, "Burrows-Wheeler", 0),
    (r"SAM\s*工具", "samtools", 0),
    (BL + r"Sam\s+tools?" + BR, "samtools", 0),
    (r"BCF\s*工具", "bcftools", 0),
    (BL + r"Bcf\s+tools?" + BR, "bcftools", 0),
    # Biopython internals ------------------------------------------------
    (BL + r"sec\.io" + BR, "SeqIO", 0),
    (BL + r"biosec\.utils" + BR, "Bio.SeqUtils", 0),
    (BL + r"biosec" + BR, "Bio.Seq", 0),
    (BL + r"Sketelearn" + BR, "scikit-learn", 0),
    # Databases ----------------------------------------------------------
    (r"集合基因\s*ID", "Ensembl 基因 ID", 0),
    (r"集合基因", "Ensembl 基因", 0),
    (r"地理数据库", "GEO 数据库", 0),
    (r"地理\s*数据集", "GEO 数据集", 0),
    (BL + r"GEO\s*2\s*R" + BR, "GEO2R", 0),
    (r"SRA\s*工具包", "SRA Toolkit", 0),
    # Misc semantic fixes ------------------------------------------------
    (r"近谷氨酸序列", "核苷酸序列", 0),
    (r"近谷氨酸", "核苷酸", 0),
    (r"变异比对", "序列比对", 0),
    (r"线点\s*SAM", ".sam", 0),
    (r"线点\s*BAM", ".bam", 0),
    (BL + r"sort\s*dot\s*BAM" + BR, "sort.bam", re.IGNORECASE),
    (r"SR\s*SAM\s*文件", "SAM 文件", 0),
    (r"贝叶斯\s*入门", "bash 入门", 0),
    (r"贝叶斯\s*shell", "bash shell", 0),
    (r"贝叶斯\s*脚本", "bash 脚本", 0),
    # Punctuation / dash normalisation -----------------------------------
    (r"—{2,}", "——", 0),
    (r"\s+,", ",", 0),
    (r"\s+。", "。", 0),
    (r"\s+\.\s+", ". ", 0),
]


def apply_terms(text: str) -> str:
    """Apply the term correction rules in order."""
    out = text
    for pattern, replacement, flags in TERM_RULES:
        out = re.sub(pattern, replacement, out, flags=flags)
    return out


# ---------------------------------------------------------------------------
# Subtitle parsing
# ---------------------------------------------------------------------------
TIMECODE_RE = re.compile(
    r"^\s*\d{2}:\d{2}:\d{2}[\.,]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[\.,]\d{3}.*$"
)
INDEX_RE = re.compile(r"^\s*\d+\s*$")


def parse_webvtt(text: str) -> tuple[str, float]:
    """Strip WEBVTT/SRT scaffolding and return (clean_text, duration_seconds)."""
    last_end: float = 0.0
    keep: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip("\ufeff").rstrip()
        if not line:
            keep.append("")
            continue
        if line.upper() == "WEBVTT":
            continue
        if line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if INDEX_RE.match(line):
            continue
        m = TIMECODE_RE.match(line)
        if m:
            tc = line.split("-->")[1].strip().split()[0].replace(",", ".")
            h, mi, sec = tc.split(":")
            last_end = int(h) * 3600 + int(mi) * 60 + float(sec)
            continue
        keep.append(line)

    cleaned = _reflow_paragraphs(keep)
    return cleaned, last_end


def _reflow_paragraphs(lines: list[str]) -> str:
    """Merge subtitle line breaks inside a paragraph and keep blank lines."""
    paragraphs: list[list[str]] = [[]]
    for line in lines:
        if not line:
            if paragraphs[-1]:
                paragraphs.append([])
            continue
        paragraphs[-1].append(line)

    result_paragraphs: list[str] = []
    for chunk in paragraphs:
        if not chunk:
            continue
        merged = "".join(chunk) if _looks_chinese(chunk) else " ".join(chunk)
        result_paragraphs.append(_polish_sentence(merged))
    # Re-segment on common Chinese end-of-sentence punctuation so paragraphs
    # are not a single run-on line.
    text = "\n".join(result_paragraphs)
    text = re.sub(r"([。！？!?])\s*", r"\1\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _looks_chinese(chunk: list[str]) -> bool:
    sample = "".join(chunk)[:200]
    cjk = sum(1 for ch in sample if "\u4e00" <= ch <= "\u9fff")
    return cjk >= max(8, len(sample) // 4)


def _polish_sentence(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\s+", " ", text).strip()
    # Tighten spacing between CJK and ASCII so the result reads cleanly.
    text = re.sub(r"([\u4e00-\u9fff])\s+([\u4e00-\u9fff])", r"\1\2", text)
    text = re.sub(r"([\u4e00-\u9fff])\s+([A-Za-z0-9])", r"\1 \2", text)
    text = re.sub(r"([A-Za-z0-9])\s+([\u4e00-\u9fff])", r"\1 \2", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------
LESSON_NUM_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\.\s*(.+?)\s*$")


def slugify(name: str) -> str:
    safe = re.sub(r"[\\/:*?\"<>|]", " ", name)
    safe = re.sub(r"\s+", "_", safe.strip())
    safe = safe.replace("'", "")
    safe = safe.strip("._")
    return safe or "untitled"


@dataclass
class Lesson:
    chapter_no: int
    chapter_title: str
    lesson_no: float | None
    lesson_title: str
    source: Path
    clean_text: str
    duration_sec: float


def collect_lessons() -> list[Lesson]:
    course_root = SOURCE_ROOT / COURSE_DIR_NAME
    if not course_root.exists():
        raise SystemExit(f"Source course folder not found: {course_root}")

    lessons: list[Lesson] = []
    for chapter_dir in sorted(p for p in course_root.iterdir() if p.is_dir()):
        m = LESSON_NUM_RE.match(chapter_dir.name)
        if not m:
            continue
        chapter_no = int(float(m.group(1)))
        chapter_title = m.group(2)
        srt_files = sorted(chapter_dir.glob("*.srt"))
        for src in srt_files:
            ln_match = LESSON_NUM_RE.match(src.stem)
            lesson_no: float | None
            lesson_title: str
            if ln_match:
                lesson_no = float(ln_match.group(1))
                lesson_title = ln_match.group(2)
            else:
                lesson_no = None
                lesson_title = src.stem
            raw = src.read_text(encoding="utf-8", errors="ignore")
            cleaned, duration = parse_webvtt(raw)
            cleaned = apply_terms(cleaned)
            lessons.append(
                Lesson(
                    chapter_no=chapter_no,
                    chapter_title=chapter_title,
                    lesson_no=lesson_no,
                    lesson_title=lesson_title,
                    source=src,
                    clean_text=cleaned,
                    duration_sec=duration,
                )
            )
    return lessons


def write_lessons(lessons: list[Lesson]) -> dict:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    chapter_buckets: dict[int, dict] = {}
    for lesson in lessons:
        chapter_slug = f"{lesson.chapter_no:02d}_{slugify(lesson.chapter_title)}"
        chapter_dir = OUTPUT_ROOT / chapter_slug
        chapter_dir.mkdir(parents=True, exist_ok=True)
        if lesson.lesson_no is not None:
            base = f"{int(lesson.lesson_no):02d}_{slugify(lesson.lesson_title)}"
        else:
            base = slugify(lesson.lesson_title)
        out_path = chapter_dir / f"{base}.txt"
        front_matter = (
            "---\n"
            f"course: AIDD Bioinformatics\n"
            f"chapter_no: {lesson.chapter_no}\n"
            f"chapter_title: {lesson.chapter_title}\n"
            f"lesson_no: {lesson.lesson_no if lesson.lesson_no is not None else ''}\n"
            f"lesson_title: {lesson.lesson_title}\n"
            f"source_subtitle: {lesson.source.as_posix()}\n"
            f"duration_minutes: {round(lesson.duration_sec / 60, 1)}\n"
            f"language: zh-CN\n"
            f"cleaning: WEBVTT timecodes removed; professional terminology"
            f" corrections applied; sentences reflowed.\n"
            "---\n\n"
            f"# {lesson.lesson_title}\n\n"
        )
        out_path.write_text(front_matter + lesson.clean_text + "\n", encoding="utf-8")
        bucket = chapter_buckets.setdefault(
            lesson.chapter_no,
            {
                "chapter_no": lesson.chapter_no,
                "chapter_title": lesson.chapter_title,
                "slug": chapter_slug,
                "lessons": [],
            },
        )
        bucket["lessons"].append(
            {
                "no": lesson.lesson_no,
                "title": lesson.lesson_title,
                "file": out_path.relative_to(OUTPUT_ROOT).as_posix(),
                "minutes": round(lesson.duration_sec / 60, 1),
                "chars": len(lesson.clean_text),
            }
        )
    return chapter_buckets


def write_index(chapter_buckets: dict) -> None:
    chapters = sorted(chapter_buckets.values(), key=lambda c: c["chapter_no"])
    lines: list[str] = []
    lines.append("# AIDD Bioinformatics 课程讲稿索引")
    lines.append("")
    lines.append(
        "本目录由 `scripts/convert/clean_aidd_subtitles.py` 自动生成。每个文件均为字幕"
        "时间轴剥离后的纯文本，已根据术语校对词典修正常见机器翻译错误，例如"
        "DESeq2、RNA-seq、samtools、bcftools、Illumina、Ensembl 等。"
    )
    lines.append("")
    total_lessons = sum(len(c["lessons"]) for c in chapters)
    total_minutes = round(
        sum(l["minutes"] for c in chapters for l in c["lessons"]), 1
    )
    total_chars = sum(l["chars"] for c in chapters for l in c["lessons"])
    lines.append(f"- 章节数：{len(chapters)}")
    lines.append(f"- 课程数：{total_lessons}")
    lines.append(f"- 累计时长（字幕）：约 {total_minutes} 分钟")
    lines.append(f"- 文本总字符数：约 {total_chars:,}")
    lines.append("")
    for ch in chapters:
        lines.append(
            f"## Chapter {ch['chapter_no']:02d}. {ch['chapter_title']}"
        )
        lines.append("")
        lines.append("| 序号 | 标题 | 时长 | 字符数 | 路径 |")
        lines.append("|---|---|---:|---:|---|")
        for lesson in sorted(
            ch["lessons"],
            key=lambda l: (l["no"] is None, l["no"] or 0, l["title"]),
        ):
            no = "" if lesson["no"] is None else f"{int(lesson['no'])}"
            lines.append(
                f"| {no} | {lesson['title']} | {lesson['minutes']} 分钟 |"
                f" {lesson['chars']} | `{lesson['file']}` |"
            )
        lines.append("")
    (OUTPUT_ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


def write_terms_dictionary() -> None:
    rows = [
        ("模式", "替换为", "说明"),
        ("DSEC / DSEC2 / Deseq2", "DESeq2", "差异表达常用 R 包"),
        ("RNA SEC / RNA 测序 / RNA-Seq", "RNA-seq", "转录组测序"),
        ("FASCQ", "FASTQ", "下机测序数据格式"),
        ("FASTA-A / pasta 文件", "FASTA / FASTA 文件", "序列文件格式"),
        ("氧化铝平台 / LuminaSec", "Illumina 平台 / Illumina", "Illumina 测序平台"),
        ("PECBio", "PacBio", "PacBio 长读测序平台"),
        ("Elad / Bota / Mr.Fast / Shreem", "Eland / Bowtie / MrFAST / SHRiMP", "比对工具"),
        ("boros wheeler", "Burrows-Wheeler", "算法/工具"),
        ("SAM 工具 / BCF 工具", "samtools / bcftools", "命令行工具"),
        ("sec.io / biosec.utils / biosec", "SeqIO / Bio.SeqUtils / Bio.Seq", "Biopython 模块"),
        ("Sketelearn", "scikit-learn", "机器学习库"),
        ("集合基因 / 集合基因 ID", "Ensembl 基因 / Ensembl 基因 ID", "基因 ID 数据库"),
        ("地理数据库 / 地理数据集", "GEO 数据库 / GEO 数据集", "GEO 公共数据库"),
        ("近谷氨酸", "核苷酸", "DNA/RNA 单体"),
        ("变异比对", "序列比对", "alignment"),
        ("线点 SAM / 线点 BAM / sort dot BAM", ".sam / .bam / sort.bam", "文件名口语化错误"),
        ("贝叶斯入门 / 贝叶斯 shell / 贝叶斯脚本", "bash 入门 / bash shell / bash 脚本", "bash 误识别为 Bayesian"),
    ]
    lines = ["# AIDD 字幕术语校正词典", ""]
    header, *body = rows
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "|".join(["---"] * len(header)) + "|")
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    lines.append("术语规则在 `scripts/convert/clean_aidd_subtitles.py` 中维护，更新规则后请重新运行脚本以再生成全部讲稿。")
    (OUTPUT_ROOT / "TERMS.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    lessons = collect_lessons()
    chapter_buckets = write_lessons(lessons)
    write_index(chapter_buckets)
    write_terms_dictionary()

    summary = {
        "lesson_count": len(lessons),
        "chapter_count": len(chapter_buckets),
        "total_minutes": round(sum(l.duration_sec for l in lessons) / 60, 1),
        "total_chars": sum(len(l.clean_text) for l in lessons),
        "output_root": OUTPUT_ROOT.as_posix(),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
