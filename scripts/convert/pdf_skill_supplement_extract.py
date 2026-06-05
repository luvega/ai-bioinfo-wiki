"""Supplement MinerU PDF outputs with pdf/markitdown skill extraction.

This script intentionally does not replace the MinerU output layer. It creates
an auxiliary text/table/image index from the original PDFs:

- MarkItDown Markdown under materials/markdown/pdf_library_skill_extract/
- pdfplumber table CSV files under the same materials directory
- PyMuPDF extracted image binaries under outputs/pdf_skill_extract/
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import unicodedata
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from markitdown import MarkItDown
import fitz
import pdfplumber
from pypdf import PdfReader


logging.getLogger("pypdf").setLevel(logging.ERROR)

ROOT = Path(__file__).resolve().parents[2]
PDF_INPUT_DIRS = (
    ROOT / "materials" / "raw" / "pdf_originals",
    ROOT / "materials" / "raw" / "external_ppt",
)
OUT_ROOT = ROOT / "materials" / "markdown" / "pdf_library_skill_extract"
IMAGE_ROOT = ROOT / "outputs" / "pdf_skill_extract"
MANIFEST_PATH = OUT_ROOT / "manifest.json"
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")


@dataclass
class PdfItem:
    title: str
    pdf_path: str
    slug: str
    pages: int
    size_mb: float


@dataclass
class TableRecord:
    page: int
    table_index: int
    rows: int
    columns: int
    csv_path: str


@dataclass
class FigureRecord:
    page: int
    image_index: int
    xref: int
    width: int
    height: int
    colorspace: str
    extension: str
    bytes: int
    output_path: str


@dataclass
class ExtractionSummary:
    title: str
    slug: str
    pdf_path: str
    pages: int
    size_mb: float
    markitdown_chars: int
    tables: int
    table_rows: int
    figures: int
    figure_bytes: int
    generated: str
    status: str
    errors: list[str]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def slugify(name: str) -> str:
    text = unicodedata.normalize("NFKC", name)
    text = "".join(ch if ch.isascii() and ch.isalnum() else "_" for ch in text)
    text = re.sub(r"_+", "_", text)
    return text.strip("._-") or "untitled"


def count_pages(path: Path) -> int:
    reader = PdfReader(str(path))
    return len(reader.pages)


def iter_pdfs() -> list[PdfItem]:
    items: list[PdfItem] = []
    seen: set[Path] = set()
    for input_dir in PDF_INPUT_DIRS:
        if not input_dir.exists():
            continue
        for path in sorted(input_dir.rglob("*.pdf")):
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            items.append(
                PdfItem(
                    title=path.stem,
                    pdf_path=rel(path),
                    slug=slugify(path.stem),
                    pages=count_pages(path),
                    size_mb=round(path.stat().st_size / 1024 / 1024, 2),
                )
            )
    return items


def filter_items(items: list[PdfItem], only: list[str] | None) -> list[PdfItem]:
    if not only:
        return items
    needles = [value.lower() for value in only]
    selected = [
        item
        for item in items
        if any(needle in item.slug.lower() or needle in item.title.lower() for needle in needles)
    ]
    if not selected:
        raise SystemExit(f"No PDFs matched --only: {only}")
    return selected


def front_matter(item: PdfItem, generated: str) -> str:
    return (
        "---\n"
        "type: source\n"
        f"title: {item.title}\n"
        "format: markitdown-pdf\n"
        f"raw_path: {item.pdf_path}\n"
        f"source_pages: {item.pages}\n"
        f"generated: {generated}\n"
        "status: generated\n"
        "tags: [markitdown, pdf-supplement, course-material]\n"
        "---\n\n"
    )


def sanitize_markitdown_links(text: str) -> str:
    """Keep external links but remove accidental local links from PDF text.

    MarkItDown can turn formulas or source cross-references into Markdown links,
    for example ``U[ 5,5](uniformdistribution)``. In this repository, local
    Markdown links are checked strictly, so generated book text should not create
    unresolved local targets.
    """

    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip().strip("<>")
        if target.startswith("#") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
            return match.group(0)
        return label

    return MARKDOWN_LINK_RE.sub(replace, text)


def write_markitdown(item: PdfItem, pdf_path: Path, book_dir: Path, generated: str) -> int:
    md = MarkItDown()
    result = md.convert(str(pdf_path))
    text = sanitize_markitdown_links(result.text_content or "")
    out_path = book_dir / "book.markitdown.md"
    out_path.write_text(front_matter(item, generated) + text.rstrip() + "\n", encoding="utf-8")
    return len(text)


def clean_cell(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("\r\n", "\n").replace("\r", "\n").strip()


def write_tables(item: PdfItem, pdf_path: Path, book_dir: Path) -> tuple[list[TableRecord], list[str]]:
    table_dir = book_dir / "tables"
    table_dir.mkdir(parents=True, exist_ok=True)
    records: list[TableRecord] = []
    errors: list[str] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page_no, page in enumerate(pdf.pages, start=1):
            try:
                tables = page.extract_tables() or []
            except Exception as exc:  # pragma: no cover - depends on PDF layout
                errors.append(f"page {page_no}: table extraction failed: {exc}")
                continue
            for table_idx, table in enumerate(tables, start=1):
                rows = [[clean_cell(cell) for cell in row] for row in table if row is not None]
                if not rows:
                    continue
                columns = max((len(row) for row in rows), default=0)
                csv_name = f"page_{page_no:04d}_table_{table_idx:02d}.csv"
                csv_path = table_dir / csv_name
                with csv_path.open("w", encoding="utf-8", newline="") as handle:
                    writer = csv.writer(handle)
                    for row in rows:
                        writer.writerow(row + [""] * (columns - len(row)))
                records.append(
                    TableRecord(
                        page=page_no,
                        table_index=table_idx,
                        rows=len(rows),
                        columns=columns,
                        csv_path=rel(csv_path),
                    )
                )
    return records, errors


def write_figures(item: PdfItem, pdf_path: Path) -> tuple[list[FigureRecord], list[str]]:
    image_dir = IMAGE_ROOT / item.slug / "images"
    image_dir.mkdir(parents=True, exist_ok=True)
    records: list[FigureRecord] = []
    errors: list[str] = []
    doc = fitz.open(str(pdf_path))
    try:
        for page_index in range(len(doc)):
            page = doc[page_index]
            try:
                images = page.get_images(full=True)
            except Exception as exc:  # pragma: no cover - depends on PDF layout
                errors.append(f"page {page_index + 1}: image listing failed: {exc}")
                continue
            for image_idx, image in enumerate(images, start=1):
                xref = int(image[0])
                try:
                    extracted = doc.extract_image(xref)
                except Exception as exc:  # pragma: no cover - depends on PDF internals
                    errors.append(f"page {page_index + 1} xref {xref}: image extraction failed: {exc}")
                    continue
                image_bytes = extracted.get("image") or b""
                if not image_bytes:
                    continue
                ext = str(extracted.get("ext") or "bin").lower()
                width = int(extracted.get("width") or image[2] or 0)
                height = int(extracted.get("height") or image[3] or 0)
                colorspace = str(extracted.get("colorspace") or image[5] or "")
                out_name = f"page_{page_index + 1:04d}_image_{image_idx:02d}_xref_{xref}.{ext}"
                out_path = image_dir / out_name
                out_path.write_bytes(image_bytes)
                records.append(
                    FigureRecord(
                        page=page_index + 1,
                        image_index=image_idx,
                        xref=xref,
                        width=width,
                        height=height,
                        colorspace=colorspace,
                        extension=ext,
                        bytes=len(image_bytes),
                        output_path=rel(out_path),
                    )
                )
    finally:
        doc.close()
    return records, errors


def write_tables_index(book_dir: Path, records: list[TableRecord], errors: list[str]) -> None:
    lines = [
        "---",
        "type: source-index",
        "title: PDF skill supplement tables index",
        "status: generated",
        "tags: [pdf, tables, pdf-supplement]",
        "---",
        "",
        "# Tables Index",
        "",
        "| Page | Table | Rows | Columns | CSV |",
        "|---:|---:|---:|---:|---|",
    ]
    for record in records:
        local_csv = Path(record.csv_path).relative_to(rel(book_dir))
        lines.append(
            f"| {record.page} | {record.table_index} | {record.rows} | {record.columns} | "
            f"[{local_csv.as_posix()}]({local_csv.as_posix()}) |"
        )
    if not records:
        lines.append("|  |  | 0 | 0 | No tables detected |")
    if errors:
        lines.extend(["", "## Extraction Errors", ""])
        lines.extend(f"- {error}" for error in errors[:50])
    (book_dir / "tables_index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_figures_index(book_dir: Path, records: list[FigureRecord], errors: list[str]) -> None:
    lines = [
        "---",
        "type: source-index",
        "title: PDF skill supplement figures index",
        "status: generated",
        "tags: [pdf, figures, images, pdf-supplement]",
        "---",
        "",
        "# Figures / Images Index",
        "",
        "Image binaries are stored under `outputs/pdf_skill_extract/` and are not linked here because outputs are ignored by Git.",
        "",
        "| Page | Image | XRef | Size | Ext | Bytes | Output path |",
        "|---:|---:|---:|---|---|---:|---|",
    ]
    for record in records:
        size = f"{record.width}x{record.height}"
        lines.append(
            f"| {record.page} | {record.image_index} | {record.xref} | {size} | "
            f"{record.extension} | {record.bytes} | `{record.output_path}` |"
        )
    if not records:
        lines.append("|  |  |  |  |  | 0 | No embedded images detected |")
    if errors:
        lines.extend(["", "## Extraction Errors", ""])
        lines.extend(f"- {error}" for error in errors[:50])
    (book_dir / "figures_index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_report(book_dir: Path, summary: ExtractionSummary) -> None:
    lines = [
        "---",
        "type: source-report",
        f"title: {summary.title} PDF skill supplement extraction report",
        "status: generated",
        "tags: [pdf, markitdown, pdf-supplement, extraction-report]",
        "---",
        "",
        f"# {summary.title} · PDF Skill Supplement Extraction Report",
        "",
        "## Source",
        "",
        f"- PDF: `{summary.pdf_path}`",
        f"- Pages: {summary.pages}",
        f"- Size MB: {summary.size_mb}",
        f"- Generated: {summary.generated}",
        "",
        "## Outputs",
        "",
        "- `book.markitdown.md`: MarkItDown Markdown supplement.",
        "- `tables_index.md`: pdfplumber table index and CSV links.",
        "- `figures_index.md`: PyMuPDF embedded image index; binaries remain in `outputs/`.",
        "",
        "## Counts",
        "",
        f"- MarkItDown characters: {summary.markitdown_chars}",
        f"- Tables: {summary.tables}",
        f"- Table rows: {summary.table_rows}",
        f"- Figures/images: {summary.figures}",
        f"- Figure bytes: {summary.figure_bytes}",
        "",
        "## Notes",
        "",
        "- This is a supplement to MinerU, not a replacement.",
        "- OCR, Azure Document Intelligence, and LLM image descriptions were not used.",
    ]
    if summary.errors:
        lines.extend(["", "## Errors", ""])
        lines.extend(f"- {error}" for error in summary.errors[:100])
    (book_dir / "extraction_report.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_root_index(summaries: list[ExtractionSummary]) -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        "type: raw-index",
        "title: PDF Skill Supplement Extract Index",
        "source_dirs:",
        "  - materials/raw/pdf_originals",
        "  - materials/raw/external_ppt",
        "output_dir: materials/markdown/pdf_library_skill_extract",
        f"generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "status: generated",
        "tags: [pdf, markitdown, pdf-supplement]",
        "---",
        "",
        "# PDF Skill Supplement Extract Index",
        "",
        "This directory stores supplemental MarkItDown, pdfplumber, and PyMuPDF extraction results.",
        "MinerU remains the main conversion layer.",
        "",
        "| Source | Markdown | Tables | Figures | Report |",
        "|---|---|---:|---:|---|",
    ]
    for summary in summaries:
        slug = summary.slug
        lines.append(
            f"| `{summary.pdf_path}` | [{slug}/book.markitdown.md]({slug}/book.markitdown.md) | "
            f"{summary.tables} | {summary.figures} | [{slug}/extraction_report.md]({slug}/extraction_report.md) |"
        )
    (OUT_ROOT / "INDEX.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    MANIFEST_PATH.write_text(
        json.dumps([asdict(summary) for summary in summaries], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def extract_item(item: PdfItem) -> ExtractionSummary:
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf_path = ROOT / item.pdf_path
    book_dir = OUT_ROOT / item.slug
    book_dir.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    print(f"Processing {item.slug} ({item.pages} pages)", flush=True)
    try:
        markitdown_chars = write_markitdown(item, pdf_path, book_dir, generated)
    except Exception as exc:
        markitdown_chars = 0
        errors.append(f"markitdown failed: {exc}")
    try:
        table_records, table_errors = write_tables(item, pdf_path, book_dir)
        errors.extend(table_errors)
    except Exception as exc:
        table_records = []
        errors.append(f"table extraction failed: {exc}")
    try:
        figure_records, figure_errors = write_figures(item, pdf_path)
        errors.extend(figure_errors)
    except Exception as exc:
        figure_records = []
        errors.append(f"figure extraction failed: {exc}")
    write_tables_index(book_dir, table_records, [error for error in errors if "table" in error])
    write_figures_index(book_dir, figure_records, [error for error in errors if "image" in error or "xref" in error])
    summary = ExtractionSummary(
        title=item.title,
        slug=item.slug,
        pdf_path=item.pdf_path,
        pages=item.pages,
        size_mb=item.size_mb,
        markitdown_chars=markitdown_chars,
        tables=len(table_records),
        table_rows=sum(record.rows for record in table_records),
        figures=len(figure_records),
        figure_bytes=sum(record.bytes for record in figure_records),
        generated=generated,
        status="generated" if not errors else "partial",
        errors=errors,
    )
    write_report(book_dir, summary)
    print(
        f"  markdown={summary.markitdown_chars} chars, "
        f"tables={summary.tables}, figures={summary.figures}, status={summary.status}",
        flush=True,
    )
    return summary


def run_all(args: argparse.Namespace) -> int:
    items = filter_items(iter_pdfs(), args.only)
    if not items:
        raise SystemExit("No PDFs found.")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    IMAGE_ROOT.mkdir(parents=True, exist_ok=True)
    summaries = [extract_item(item) for item in items]
    write_root_index(summaries)
    print(json.dumps([asdict(summary) for summary in summaries], ensure_ascii=False, indent=2))
    return 0


def run_check(_: argparse.Namespace) -> int:
    expected = iter_pdfs()
    issues: list[str] = []
    if not MANIFEST_PATH.is_file():
        issues.append(f"Missing {rel(MANIFEST_PATH)}")
        summaries: list[dict[str, Any]] = []
    else:
        summaries = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    by_slug = {row.get("slug"): row for row in summaries}
    for item in expected:
        row = by_slug.get(item.slug)
        book_dir = OUT_ROOT / item.slug
        for name in ("book.markitdown.md", "tables_index.md", "figures_index.md", "extraction_report.md"):
            if not (book_dir / name).is_file():
                issues.append(f"{item.slug}: missing {name}")
        if row is None:
            issues.append(f"{item.slug}: missing manifest entry")
            continue
        if int(row.get("pages") or 0) != item.pages:
            issues.append(f"{item.slug}: manifest pages mismatch")
        if int(row.get("markitdown_chars") or 0) <= 0:
            issues.append(f"{item.slug}: markitdown output is empty")
    if issues:
        print("PDF skill supplement check failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("OK: PDF skill supplement extraction outputs are current.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Supplement PDF conversion using pdf and markitdown skill methods.")
    parser.add_argument("--all", action="store_true", help="Run extraction for all source PDFs.")
    parser.add_argument("--check", action="store_true", help="Check generated supplemental outputs.")
    parser.add_argument("--only", action="append", help="Filter source PDFs by title or slug substring.")
    args = parser.parse_args()
    if args.check:
        return run_check(args)
    if args.all:
        return run_all(args)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
