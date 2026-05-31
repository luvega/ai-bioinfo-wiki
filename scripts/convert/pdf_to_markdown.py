"""Convert reference PDFs to course-material Markdown.

Pipeline:
  1. For each PDF in INPUT_DIR, extract text page-by-page using ``pdfplumber``;
     fall back to ``pypdf`` when pdfplumber returns an empty page.
  2. Detect scanned/image-only PDFs by measuring extracted character density;
     mark them as needing OCR (no inline OCR — Tesseract is not assumed to be
     installed).
  3. Re-flow page text into paragraphs, normalise whitespace, soft-detect
     headings via leading numbering / ALL CAPS short lines, and emit chapters
     as ``## chunk`` blocks for easier LLM Wiki ingest.
  4. Sanitise the file name (drop ``[]【】`` and other characters that have
     tripped LLM Wiki's PDF loader in the past) and write each Markdown file
     with a YAML front matter (title, original_path, pages, char_count).
  5. Print a JSON summary so we can inspect results from PowerShell.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = ROOT / "materials" / "raw" / "pdf_originals"
OUTPUT_DIR = ROOT / "materials" / "markdown" / "pdf_library_legacy"
SCAN_THRESHOLD_CHARS_PER_PAGE = 60


def slugify(name: str) -> str:
    """ASCII-friendly, LLM-Wiki-safe slug.

    LLM Wiki's PDF loader has historically choked on names containing CJK
    full-width brackets ``【】``, square brackets ``[]``, underscores attached
    to spaces, etc. We drop those, normalise spaces to underscores, and keep
    only ``[A-Za-z0-9-_]``.
    """
    text = unicodedata.normalize("NFKC", name)
    text = re.sub(r"[【】\[\]()（）]", " ", text)
    text = re.sub(r"[^A-Za-z0-9\u4e00-\u9fff\s_\-]", "", text)
    text = re.sub(r"\s+", "_", text.strip())
    text = re.sub(r"_+", "_", text)
    return text.strip("._-") or "untitled"


HEADING_RE = re.compile(
    r"^(?:(?:Chapter|CHAPTER|Section|SECTION|Part|PART)\s+[\dIVXLC]+\b.*"
    r"|\d+(?:\.\d+){0,2}\s+[A-Z\u4e00-\u9fff].{0,80}"
    r"|[A-Z][A-Z0-9 ,\-]{4,80})\s*$"
)


def _normalise(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _reflow_page(text: str) -> str:
    """Merge hard-wrapped lines from PDF columns into proper paragraphs.

    pdfplumber preserves each physical line as a separate line. For prose
    we want to recombine them while preserving headings and bullet lists.
    """
    lines = [line.rstrip() for line in text.split("\n")]
    paragraphs: list[list[str]] = [[]]
    for line in lines:
        if not line.strip():
            if paragraphs[-1]:
                paragraphs.append([])
            continue
        stripped = line.strip()
        if HEADING_RE.match(stripped):
            if paragraphs[-1]:
                paragraphs.append([])
            paragraphs.append([f"## {stripped}"])
            paragraphs.append([])
            continue
        if re.match(r"^[\-\*•·]\s+", stripped):
            paragraphs[-1].append(stripped)
            paragraphs.append([])
            continue
        paragraphs[-1].append(stripped)
    rebuilt: list[str] = []
    for chunk in paragraphs:
        if not chunk:
            continue
        if chunk[0].startswith("## "):
            rebuilt.append(chunk[0])
            continue
        rebuilt.append(_join_lines(chunk))
    return "\n\n".join(rebuilt)


def _join_lines(lines: Iterable[str]) -> str:
    """Concatenate hard-wrapped lines, treating hyphenated word-breaks."""
    out: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if out and out[-1].endswith("-") and re.match(r"[a-z]", line):
            out[-1] = out[-1][:-1] + line
        elif out and re.search(r"[\u4e00-\u9fff]$", out[-1]) and re.match(
            r"[\u4e00-\u9fff]", line
        ):
            out[-1] = out[-1] + line
        else:
            out.append((out.pop() + " " + line) if out else line)
    return " ".join(out) if False else "\n".join(out)


@dataclass
class PdfResult:
    src: Path
    out: Path | None
    pages: int
    chars: int
    needs_ocr: bool
    error: str | None = None


def _extract_with_plumber(path: Path) -> tuple[list[str], int]:
    pages: list[str] = []
    with pdfplumber.open(str(path)) as pdf:
        for page in pdf.pages:
            try:
                t = page.extract_text(x_tolerance=2, y_tolerance=3) or ""
            except Exception:
                t = ""
            pages.append(t)
    return pages, len(pages)


def _extract_with_pypdf(path: Path) -> list[str]:
    reader = PdfReader(str(path))
    return [page.extract_text() or "" for page in reader.pages]


def convert_pdf(src: Path) -> PdfResult:
    try:
        plumber_pages, total = _extract_with_plumber(src)
    except Exception as exc:
        return PdfResult(src=src, out=None, pages=0, chars=0,
                        needs_ocr=False, error=f"pdfplumber: {exc}")

    pypdf_pages: list[str] | None = None
    fixed_pages: list[str] = []
    for i, page_text in enumerate(plumber_pages):
        if len(page_text.strip()) < 20:
            if pypdf_pages is None:
                try:
                    pypdf_pages = _extract_with_pypdf(src)
                except Exception:
                    pypdf_pages = []
            page_text = (
                pypdf_pages[i] if pypdf_pages and i < len(pypdf_pages) else page_text
            )
        fixed_pages.append(page_text)

    char_count = sum(len(p) for p in fixed_pages)
    char_per_page = char_count / max(total, 1)
    needs_ocr = char_per_page < SCAN_THRESHOLD_CHARS_PER_PAGE

    if needs_ocr:
        return PdfResult(src=src, out=None, pages=total, chars=char_count,
                        needs_ocr=True,
                        error="Image-only PDF — install Tesseract + run OCR.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(src.stem)
    out_path = OUTPUT_DIR / f"{slug}.md"

    body_parts: list[str] = []
    for i, page_text in enumerate(fixed_pages, start=1):
        if not page_text.strip():
            continue
        cleaned = _reflow_page(_normalise(page_text))
        body_parts.append(f"<!-- page {i} -->\n\n{cleaned}")
    body = "\n\n".join(body_parts)

    fm = (
        "---\n"
        f"type: source\n"
        f"title: {src.stem}\n"
        f"format: pdf-markdown\n"
        f"pages: {total}\n"
        f"char_count: {char_count}\n"
        f"original_path: {src.as_posix()}\n"
        "language: auto\n"
        "ingest_hint: textbook\n"
        "---\n\n"
    )
    out_path.write_text(fm + f"# {src.stem}\n\n" + body + "\n", encoding="utf-8")

    return PdfResult(src=src, out=out_path, pages=total, chars=char_count,
                    needs_ocr=False)


def main() -> None:
    if not INPUT_DIR.exists():
        sys.exit(f"Input dir missing: {INPUT_DIR}")

    pdfs = sorted(INPUT_DIR.glob("*.pdf"))
    if not pdfs:
        sys.exit(f"No PDFs found in {INPUT_DIR}")

    results: list[PdfResult] = []
    for src in pdfs:
        print(f"Processing: {src.name}", flush=True)
        result = convert_pdf(src)
        results.append(result)
        if result.error:
            print(f"  ! {result.error}", flush=True)
        else:
            print(
                f"  OK -> {result.out.name} ({result.pages} pages,"
                f" {result.chars} chars)",
                flush=True,
            )

    summary = {
        "input_dir": INPUT_DIR.as_posix(),
        "output_dir": OUTPUT_DIR.as_posix(),
        "count": len(results),
        "success": sum(1 for r in results if r.out),
        "needs_ocr": sum(1 for r in results if r.needs_ocr),
        "failed": sum(1 for r in results if r.error and not r.needs_ocr),
        "results": [
            {
                "src": r.src.name,
                "out": r.out.name if r.out else None,
                "pages": r.pages,
                "chars": r.chars,
                "needs_ocr": r.needs_ocr,
                "error": r.error,
            }
            for r in results
        ],
    }
    print("\nSUMMARY:")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
