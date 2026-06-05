"""Extract local PDF textbooks into the AI_Course materials library.

This script handles two local cases that do not require a MinerU API token:

- PDFs with a usable text layer are extracted page by page with pdfplumber,
  falling back to pypdf for sparse pages.
- Scanned PDFs are rendered with PyMuPDF and OCRed with local Tesseract.

Raw PDFs remain immutable under materials/raw/pdf_originals. Page-level caches
are written under outputs/ so they stay local. The searchable textbook artifact
is a single book.fulltext.md under materials/markdown/pdf_library_local_text.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unicodedata
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal

import fitz
import pdfplumber
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = ROOT / "materials" / "raw" / "pdf_originals"
OUT_ROOT = ROOT / "materials" / "markdown" / "pdf_library_local_text"
CACHE_ROOT = ROOT / "outputs" / "pdf_library_local_text_cache"
MANIFEST_PATH = OUT_ROOT / "manifest.json"
TEXT_LAYER_THRESHOLD_CHARS_PER_PAGE = 80
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]\n]{1,120})\]\(([^)]{1,240})\)", re.S)

KNOWN_SLUGS = {
    "生物医药大数据与智能分析": "Biomedical_Big_Data_Intelligent_Analysis",
    "Python程序设计-以医药数据为例": "Python_Programming_Medical_Data",
}


@dataclass
class PdfItem:
    title: str
    pdf_path: str
    slug: str
    pages: int
    size_mb: float


@dataclass
class ExtractionSummary:
    title: str
    slug: str
    pdf_path: str
    pages: int
    size_mb: float
    method: str
    status: str
    chars: int
    processed_pages: int
    missing_pages: int
    output_markdown: str
    report: str
    cache_dir: str
    generated: str
    ocr_language: str | None
    ocr_dpi: int | None
    ocr_psm: str | None
    notes: list[str]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def slugify(name: str) -> str:
    if name in KNOWN_SLUGS:
        return KNOWN_SLUGS[name]
    text = unicodedata.normalize("NFKC", name)
    text = "".join(ch if ch.isascii() and ch.isalnum() else "_" for ch in text)
    text = re.sub(r"_+", "_", text).strip("._-")
    if text:
        return text
    digest = hashlib.sha1(name.encode("utf-8")).hexdigest()[:10]
    return f"pdf_{digest}"


def find_tesseract() -> Path | None:
    candidate = shutil.which("tesseract")
    if candidate:
        return Path(candidate)
    default = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    return default if default.exists() else None


def count_pages(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def iter_pdfs() -> list[PdfItem]:
    items: list[PdfItem] = []
    if not INPUT_DIR.exists():
        return items
    for pdf_path in sorted(INPUT_DIR.glob("*.pdf")):
        items.append(
            PdfItem(
                title=pdf_path.stem,
                pdf_path=rel(pdf_path),
                slug=slugify(pdf_path.stem),
                pages=count_pages(pdf_path),
                size_mb=round(pdf_path.stat().st_size / 1024 / 1024, 2),
            )
        )
    return items


def filter_items(items: list[PdfItem], only: list[str] | None) -> list[PdfItem]:
    if not only:
        return items
    needles = [needle.casefold() for needle in only]
    selected = [
        item
        for item in items
        if any(
            needle in item.title.casefold()
            or needle in item.slug.casefold()
            or needle in item.pdf_path.casefold()
            for needle in needles
        )
    ]
    if not selected:
        raise SystemExit(f"No PDFs matched --only: {only}")
    return selected


def page_range(total_pages: int, start: int | None, end: int | None) -> range:
    first = max(1, start or 1)
    last = min(total_pages, end or total_pages)
    if first > last:
        raise SystemExit(f"Invalid page range: {first}-{last} for {total_pages} pages")
    return range(first, last + 1)


def normalise_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def sanitize_markdown_links(text: str) -> str:
    """Remove accidental local Markdown links produced by PDF text.

    Source textbooks may contain bracketed abbreviations followed by
    parentheses. The project link checker treats these as managed Markdown
    links, so keep only anchors and external URI links.
    """

    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip().strip("<>")
        if target.startswith("#") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
            return match.group(0)
        return label

    return MARKDOWN_LINK_RE.sub(replace, text)


def text_layer_probe(item: PdfItem, sample_pages: int = 20) -> tuple[bool, float]:
    pdf_path = ROOT / item.pdf_path
    counts: list[int] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        probes = list(range(min(sample_pages, len(pdf.pages))))
        if len(pdf.pages) > sample_pages:
            probes.extend([len(pdf.pages) // 2, len(pdf.pages) - 1])
        for idx in sorted(set(probes)):
            try:
                text = pdf.pages[idx].extract_text() or ""
            except Exception:
                text = ""
            counts.append(len(text.strip()))
    avg = sum(counts) / max(1, len(counts))
    return avg >= TEXT_LAYER_THRESHOLD_CHARS_PER_PAGE, avg


def cache_path(item: PdfItem, page_no: int) -> Path:
    return CACHE_ROOT / item.slug / "pages" / f"page_{page_no:04d}.txt"


def read_pypdf_pages(path: Path) -> list[str]:
    reader = PdfReader(str(path))
    return [page.extract_text() or "" for page in reader.pages]


def extract_text_layer_pages(item: PdfItem, args: argparse.Namespace) -> None:
    pdf_path = ROOT / item.pdf_path
    pypdf_pages: list[str] | None = None
    targets = page_range(item.pages, args.start_page, args.end_page)
    cache_path(item, 1).parent.mkdir(parents=True, exist_ok=True)
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page_no in targets:
            out_path = cache_path(item, page_no)
            if out_path.exists() and not args.force:
                continue
            try:
                text = pdf.pages[page_no - 1].extract_text(x_tolerance=2, y_tolerance=3) or ""
            except Exception:
                text = ""
            if len(text.strip()) < 20:
                if pypdf_pages is None:
                    pypdf_pages = read_pypdf_pages(pdf_path)
                if page_no - 1 < len(pypdf_pages) and len(pypdf_pages[page_no - 1].strip()) > len(text.strip()):
                    text = pypdf_pages[page_no - 1]
            out_path.write_text(normalise_text(text) + "\n", encoding="utf-8", newline="\n")
            print(f"{item.slug}: text page {page_no}/{item.pages}", flush=True)


def ocr_pages(item: PdfItem, args: argparse.Namespace) -> None:
    tesseract = find_tesseract()
    if tesseract is None:
        raise SystemExit("Tesseract not found. Install Tesseract or set it on PATH.")
    pdf_path = ROOT / item.pdf_path
    cache_path(item, 1).parent.mkdir(parents=True, exist_ok=True)
    targets = page_range(item.pages, args.start_page, args.end_page)
    doc = fitz.open(str(pdf_path))
    try:
        for page_no in targets:
            out_path = cache_path(item, page_no)
            if out_path.exists() and not args.force:
                continue
            with tempfile.TemporaryDirectory() as temp_dir:
                image_path = Path(temp_dir) / f"page_{page_no:04d}.png"
                pix = doc[page_no - 1].get_pixmap(dpi=args.dpi, alpha=False)
                pix.save(str(image_path))
                command = [
                    str(tesseract),
                    str(image_path),
                    "stdout",
                    "-l",
                    args.lang,
                    "--psm",
                    args.psm,
                ]
                completed = subprocess.run(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=args.timeout,
                )
            if completed.returncode != 0:
                raise SystemExit(
                    f"Tesseract failed on {item.title} page {page_no}: {completed.stderr.strip()}"
                )
            out_path.write_text(normalise_text(completed.stdout) + "\n", encoding="utf-8", newline="\n")
            print(
                f"{item.slug}: OCR page {page_no}/{item.pages} "
                f"({len(completed.stdout.strip())} chars)",
                flush=True,
            )
    finally:
        doc.close()


def book_dir(item: PdfItem) -> Path:
    return OUT_ROOT / item.slug


def output_book_path(item: PdfItem) -> Path:
    return book_dir(item) / "book.fulltext.md"


def report_path(item: PdfItem) -> Path:
    return book_dir(item) / "extraction_report.md"


def front_matter(item: PdfItem, method: str, generated: str, status: str, args: argparse.Namespace) -> str:
    tags = ["pdf", "textbook", "local-extract", "course-material"]
    if method == "tesseract-ocr":
        tags.append("ocr")
    tag_text = ", ".join(tags)
    ocr_lines = ""
    if method == "tesseract-ocr":
        ocr_lines = (
            f"ocr_language: {args.lang}\n"
            f"ocr_dpi: {args.dpi}\n"
            f"ocr_psm: {args.psm}\n"
        )
    return (
        "---\n"
        "type: source\n"
        f"title: {item.title}\n"
        "format: local-pdf-fulltext\n"
        f"raw_path: {item.pdf_path}\n"
        f"source_pages: {item.pages}\n"
        f"generated: {generated}\n"
        f"status: {status}\n"
        f"extraction_method: {method}\n"
        f"{ocr_lines}"
        f"tags: [{tag_text}]\n"
        "---\n\n"
    )


def combine_book(item: PdfItem, method: str, args: argparse.Namespace) -> ExtractionSummary:
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pages: list[tuple[int, str]] = []
    missing = 0
    for page_no in range(1, item.pages + 1):
        path = cache_path(item, page_no)
        if not path.exists():
            missing += 1
            continue
        raw_text = path.read_text(encoding="utf-8", errors="replace").strip()
        pages.append((page_no, sanitize_markdown_links(raw_text)))

    status = "generated" if missing == 0 else "partial"
    notes = [
        "Raw PDFs are unchanged under materials/raw/pdf_originals.",
        "Page-level extraction cache is under outputs/ and is not committed.",
        "Use the raw PDF for page-accurate quotation or figure verification.",
    ]
    if method == "tesseract-ocr":
        notes.append("OCR text is suitable for retrieval and lesson planning, but code snippets and tables require manual verification.")

    body_lines = [
        front_matter(item, method, generated, status, args),
        f"# {item.title}",
        "",
        "> 本文件是本地 PDF 全文提取层, 用于 AI_Course 备课检索与素材归档; 不替代原始 PDF 的人工核验。",
        "",
        "## Extraction Notes",
        "",
    ]
    body_lines.extend(f"- {note}" for note in notes)
    if missing:
        body_lines.extend(["", f"- Missing pages in current cache: {missing}"])
    body_lines.extend(["", "## Full Text", ""])
    for page_no, text in pages:
        body_lines.extend([f"<!-- page {page_no} -->", "", f"### Page {page_no}", "", text or "[empty page]", ""])

    out_path = output_book_path(item)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(body_lines).rstrip() + "\n", encoding="utf-8", newline="\n")

    chars = sum(len(text) for _, text in pages)
    summary = ExtractionSummary(
        title=item.title,
        slug=item.slug,
        pdf_path=item.pdf_path,
        pages=item.pages,
        size_mb=item.size_mb,
        method=method,
        status=status,
        chars=chars,
        processed_pages=len(pages),
        missing_pages=missing,
        output_markdown=rel(out_path),
        report=rel(report_path(item)),
        cache_dir=rel(CACHE_ROOT / item.slug),
        generated=generated,
        ocr_language=args.lang if method == "tesseract-ocr" else None,
        ocr_dpi=args.dpi if method == "tesseract-ocr" else None,
        ocr_psm=args.psm if method == "tesseract-ocr" else None,
        notes=notes,
    )
    write_report(summary)
    return summary


def write_report(summary: ExtractionSummary) -> None:
    lines = [
        "---",
        "type: source-report",
        f"title: {summary.title} local PDF extraction report",
        "status: generated",
        "tags: [pdf, extraction-report, local-extract]",
        "---",
        "",
        f"# {summary.title} · Local PDF Extraction Report",
        "",
        "## Source",
        "",
        f"- PDF: `{summary.pdf_path}`",
        f"- Pages: {summary.pages}",
        f"- Size MB: {summary.size_mb}",
        "",
        "## Extraction",
        "",
        f"- Method: `{summary.method}`",
        f"- Status: `{summary.status}`",
        f"- Processed pages: {summary.processed_pages}",
        f"- Missing pages: {summary.missing_pages}",
        f"- Characters: {summary.chars}",
        f"- Generated: {summary.generated}",
        "- Markdown: [book.fulltext.md](book.fulltext.md)",
        f"- Page cache: `{summary.cache_dir}`",
    ]
    if summary.method == "tesseract-ocr":
        lines.extend(
            [
                f"- OCR language: `{summary.ocr_language}`",
                f"- OCR DPI: `{summary.ocr_dpi}`",
                f"- OCR PSM: `{summary.ocr_psm}`",
            ]
        )
    lines.extend(["", "## Notes", ""])
    lines.extend(f"- {note}" for note in summary.notes)
    report = ROOT / summary.report
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def write_root_index(summaries: list[ExtractionSummary]) -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "---",
        "type: raw-index",
        "title: Local PDF Textbook Extract Index",
        "source_dirs:",
        "  - materials/raw/pdf_originals",
        "output_dir: materials/markdown/pdf_library_local_text",
        f"generated: {generated}",
        "status: generated",
        "tags: [pdf, local-extract, textbook]",
        "---",
        "",
        "# Local PDF Textbook Extract Index",
        "",
        "This directory stores local text-layer and Tesseract OCR extraction results for PDF textbooks.",
        "Original PDFs remain under `materials/raw/pdf_originals/`.",
        "",
        "| Source | Method | Status | Pages | Chars | Markdown | Report |",
        "|---|---|---|---:|---:|---|---|",
    ]
    for summary in sorted(summaries, key=lambda row: row.slug.lower()):
        lines.append(
            f"| `{summary.pdf_path}` | {summary.method} | {summary.status} | "
            f"{summary.processed_pages}/{summary.pages} | {summary.chars} | "
            f"[{summary.slug}/book.fulltext.md]({summary.slug}/book.fulltext.md) | "
            f"[{summary.slug}/extraction_report.md]({summary.slug}/extraction_report.md) |"
        )
    (OUT_ROOT / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    MANIFEST_PATH.write_text(
        json.dumps([asdict(summary) for summary in summaries], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def load_existing_manifest() -> list[ExtractionSummary]:
    if not MANIFEST_PATH.exists():
        return []
    rows = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return [ExtractionSummary(**row) for row in rows]


def choose_method(item: PdfItem, requested: Literal["auto", "text", "ocr"]) -> str:
    if requested == "text":
        return "text-layer"
    if requested == "ocr":
        return "tesseract-ocr"
    has_text, avg = text_layer_probe(item)
    method = "text-layer" if has_text else "tesseract-ocr"
    print(f"{item.slug}: text-layer average probe chars/page = {avg:.1f}; method = {method}", flush=True)
    return method


def extract_item(item: PdfItem, args: argparse.Namespace) -> ExtractionSummary:
    method = choose_method(item, args.method)
    if not args.combine_only:
        if method == "text-layer":
            extract_text_layer_pages(item, args)
        else:
            ocr_pages(item, args)
    return combine_book(item, method, args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Process all PDFs in materials/raw/pdf_originals.")
    parser.add_argument("--only", action="append", help="Filter PDFs by title, slug, or path substring.")
    parser.add_argument("--method", choices=["auto", "text", "ocr"], default="auto", help="Extraction method.")
    parser.add_argument("--start-page", type=int, help="First page to process.")
    parser.add_argument("--end-page", type=int, help="Last page to process.")
    parser.add_argument("--force", action="store_true", help="Reprocess pages even when cache exists.")
    parser.add_argument("--combine-only", action="store_true", help="Rebuild book.fulltext.md from cached pages.")
    parser.add_argument("--lang", default="chi_sim+eng", help="Tesseract language expression.")
    parser.add_argument("--dpi", type=int, default=220, help="OCR render DPI.")
    parser.add_argument("--psm", default="3", help="Tesseract page segmentation mode.")
    parser.add_argument("--timeout", type=int, default=180, help="Per-page OCR timeout in seconds.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not args.all and not args.only:
        parser.error("Choose --all or at least one --only filter.")
    items = filter_items(iter_pdfs(), args.only)
    existing = {summary.slug: summary for summary in load_existing_manifest()}
    summaries: list[ExtractionSummary] = []
    for item in items:
        summary = extract_item(item, args)
        existing[item.slug] = summary
        summaries.append(summary)
    write_root_index(list(existing.values()))
    print(json.dumps([asdict(summary) for summary in summaries], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
