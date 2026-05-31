"""MinerU API-only pipeline for course reference PDFs.

This project no longer keeps a local MinerU CLI environment. Original PDFs stay
immutable under ``materials/raw/``. The script submits PDFs to MinerU Precision
API and uses ``page_ranges`` for long files.

Token handling:

    $env:MINERU_API_TOKEN = "<token>"

Typical flow:

    python scripts/convert/mineru_pdf_pipeline.py inventory
    python scripts/convert/mineru_pdf_pipeline.py prepare-parts
    python scripts/convert/mineru_pdf_pipeline.py api-submit --model-version vlm
    python scripts/convert/mineru_pdf_pipeline.py api-poll --wait --download
    python scripts/convert/mineru_pdf_pipeline.py api-promote
"""
from __future__ import annotations

import argparse
import http.client
import json
import logging
import os
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from pypdf import PdfReader
except Exception:  # pragma: no cover
    PdfReader = None  # type: ignore[assignment]

logging.getLogger("pypdf").setLevel(logging.ERROR)


ROOT = Path(__file__).resolve().parents[2]
PDF_INPUT_DIRS = (
    ROOT / "materials" / "raw" / "pdf_originals",
    ROOT / "materials" / "raw" / "external_ppt",
)
OUT_ROOT = ROOT / "materials" / "markdown" / "pdf_library_mineru"
ZIP_DIR = OUT_ROOT / "api_zips"
API_RAW_DIR = OUT_ROOT / "api_raw"
PARTS_PATH = OUT_ROOT / "api_parts.json"
SUBMISSIONS_PATH = OUT_ROOT / "api_submissions.json"
RESULTS_PATH = OUT_ROOT / "api_results.json"
BASE_URL = "https://mineru.net"
MAX_PAGES_PER_TASK = 200
MAX_FILE_SIZE_MB = 200
MAX_UPLOAD_URLS_PER_BATCH = 50


@dataclass
class PdfItem:
    title: str
    pdf_path: str
    slug: str
    pages: int | None
    size_mb: float


@dataclass
class PdfTask:
    title: str
    slug: str
    source_pdf: str
    task_index: int
    page_start: int
    page_end: int
    page_ranges: str
    upload_pdf: str
    upload_name: str
    data_id: str
    size_mb: float


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def slugify(name: str) -> str:
    text = unicodedata.normalize("NFKC", name)
    text = "".join(ch if ch.isascii() and ch.isalnum() else "_" for ch in text)
    while "__" in text:
        text = text.replace("__", "_")
    return text.strip("._-") or "untitled"


def short_slug(slug: str, max_len: int = 80) -> str:
    return slug if len(slug) <= max_len else slug[:max_len].rstrip("_")


def count_pages(pdf_path: Path) -> int | None:
    if PdfReader is None:
        return None
    try:
        return len(PdfReader(str(pdf_path)).pages)
    except Exception:
        return None


def iter_pdfs() -> list[PdfItem]:
    pdfs: list[PdfItem] = []
    seen: set[Path] = set()
    for input_dir in PDF_INPUT_DIRS:
        if not input_dir.exists():
            continue
        for pdf_path in sorted(input_dir.rglob("*.pdf")):
            resolved = pdf_path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            pdfs.append(
                PdfItem(
                    title=pdf_path.stem,
                    pdf_path=rel(pdf_path),
                    slug=slugify(pdf_path.stem),
                    pages=count_pages(pdf_path),
                    size_mb=round(pdf_path.stat().st_size / 1024 / 1024, 2),
                )
            )
    return pdfs


def filter_items(items: list[PdfItem], only: list[str] | None) -> list[PdfItem]:
    if not only:
        return items
    needles = [needle.lower() for needle in only]
    selected = [
        item
        for item in items
        if any(needle in item.slug.lower() or needle in item.title.lower() for needle in needles)
    ]
    if not selected:
        raise SystemExit(f"No PDFs matched --only: {only}")
    return selected


def write_index(items: list[PdfItem]) -> Path:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "---",
        "type: raw-index",
        "title: MinerU PDF Library Index",
        "source_dirs:",
        "  - materials/raw/pdf_originals",
        "  - materials/raw/external_ppt",
        "output_dir: materials/markdown/pdf_library_mineru",
        f"generated: {generated}",
        "status: generated",
        "---",
        "",
        "# MinerU PDF Library Index",
        "",
        "This directory stores Markdown and JSON returned by MinerU Precision API.",
        "Original PDFs remain under `materials/raw/` and are not modified.",
        "",
        "| Book | Source PDF | Pages | Size MB | Output folder |",
        "|---|---|---:|---:|---|",
    ]
    for item in items:
        pages = "" if item.pages is None else str(item.pages)
        lines.append(f"| {item.title} | `{item.pdf_path}` | {pages} | {item.size_mb} | `{item.slug}/` |")
    lines.extend(
        [
            "",
            "## API Workflow",
            "",
            "```powershell",
            "$env:MINERU_API_TOKEN = \"<token>\"",
            "python scripts/convert/mineru_pdf_pipeline.py prepare-parts",
            "python scripts/convert/mineru_pdf_pipeline.py api-submit --model-version vlm",
            "python scripts/convert/mineru_pdf_pipeline.py api-poll --wait --download",
            "python scripts/convert/mineru_pdf_pipeline.py api-promote",
            "```",
            "",
            "`api_zips/` and `api_raw/` are generated caches.",
            "Promoted files use `book.mineru.md` and `book.part_XXX.mineru.md`.",
            "",
        ]
    )
    index_path = OUT_ROOT / "INDEX.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    (OUT_ROOT / "manifest.json").write_text(
        json.dumps([asdict(item) for item in items], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return index_path


def build_tasks(items: list[PdfItem], max_pages: int = MAX_PAGES_PER_TASK) -> list[PdfTask]:
    tasks: list[PdfTask] = []
    if max_pages < 1:
        raise SystemExit("--max-pages must be positive.")
    for item in items:
        if item.pages is None:
            raise SystemExit("Cannot count PDF pages; install pypdf or use a Python env with pypdf.")
        if item.size_mb > MAX_FILE_SIZE_MB:
            raise SystemExit(f"{item.pdf_path} is {item.size_mb} MB; MinerU Precision API limit is {MAX_FILE_SIZE_MB} MB.")
        task_count = (item.pages + max_pages - 1) // max_pages
        for idx in range(task_count):
            start = idx * max_pages + 1
            end = min((idx + 1) * max_pages, item.pages)
            upload_name = f"{short_slug(item.slug)}.part_{idx + 1:03d}.pdf"
            tasks.append(
                PdfTask(
                    title=item.title,
                    slug=item.slug,
                    source_pdf=item.pdf_path,
                    task_index=idx + 1,
                    page_start=start,
                    page_end=end,
                    page_ranges=f"{start}-{end}",
                    upload_pdf=item.pdf_path,
                    upload_name=upload_name,
                    data_id=f"{short_slug(item.slug, 80)}_part_{idx + 1:03d}",
                    size_mb=item.size_mb,
                )
            )
    return tasks


def prepare_parts(args: argparse.Namespace) -> int:
    items = filter_items(iter_pdfs(), args.only)
    write_index(items)
    tasks = build_tasks(items, args.max_pages)
    PARTS_PATH.write_text(
        json.dumps([asdict(task) for task in tasks], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps([asdict(task) for task in tasks], ensure_ascii=False, indent=2))
    print(f"Wrote {rel(PARTS_PATH)}")
    return 0


def token_from_env() -> str:
    token = os.environ.get("MINERU_API_TOKEN", "").strip()
    if not token:
        raise SystemExit("Set MINERU_API_TOKEN in the environment; do not write it to files.")
    return token


def api_json(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "*/*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code} from MinerU API: {body}") from exc


def upload_file(url: str, path: Path) -> None:
    # MinerU's signed OSS URL must be uploaded without a Content-Type header.
    # urllib.request adds application/x-www-form-urlencoded for data=..., which
    # breaks the OSS signature. Use http.client directly so headers stay minimal.
    parsed = urllib.parse.urlsplit(url)
    target = urllib.parse.urlunsplit(("", "", parsed.path, parsed.query, ""))
    connection_cls = http.client.HTTPSConnection if parsed.scheme == "https" else http.client.HTTPConnection
    connection = connection_cls(parsed.netloc, timeout=600)
    try:
        data = path.read_bytes()
        connection.request("PUT", target, body=data, headers={"Content-Length": str(len(data))})
        response = connection.getresponse()
        body = response.read().decode("utf-8", errors="replace")
        if response.status != 200:
            raise SystemExit(f"Upload failed for {path}: HTTP {response.status} {body}")
    finally:
        connection.close()


def load_tasks(args: argparse.Namespace) -> list[PdfTask]:
    if not PARTS_PATH.exists():
        prepare_parts(argparse.Namespace(only=args.only, max_pages=args.max_pages))
    data = json.loads(PARTS_PATH.read_text(encoding="utf-8"))
    tasks = [PdfTask(**row) for row in data]
    if args.only:
        allowed = {item.slug for item in filter_items(iter_pdfs(), args.only)}
        tasks = [task for task in tasks if task.slug in allowed]
    return tasks


def api_submit(args: argparse.Namespace) -> int:
    token = token_from_env()
    if args.batch_size > MAX_UPLOAD_URLS_PER_BATCH:
        raise SystemExit(f"--batch-size cannot exceed {MAX_UPLOAD_URLS_PER_BATCH}.")
    tasks = load_tasks(args)
    if args.limit:
        tasks = tasks[: args.limit]
    submissions: list[dict[str, Any]] = []
    for i in range(0, len(tasks), args.batch_size):
        batch = tasks[i : i + args.batch_size]
        payload = {
            "model_version": args.model_version,
            "language": args.language,
            "enable_formula": args.enable_formula,
            "enable_table": args.enable_table,
            "files": [
                {
                    "name": task.upload_name,
                    "data_id": task.data_id,
                    "is_ocr": args.is_ocr,
                    "page_ranges": task.page_ranges,
                }
                for task in batch
            ],
        }
        if args.extra_format:
            payload["extra_formats"] = args.extra_format
        result = api_json("POST", f"{BASE_URL}/api/v4/file-urls/batch", token, payload)
        if result.get("code") != 0:
            raise SystemExit(f"Apply upload URLs failed: {result}")
        urls = result["data"]["file_urls"]
        for task, upload_url in zip(batch, urls):
            upload_file(upload_url, ROOT / task.upload_pdf)
        submissions.append(
            {
                "batch_id": result["data"]["batch_id"],
                "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "model_version": args.model_version,
                "tasks": [asdict(task) for task in batch],
            }
        )
    SUBMISSIONS_PATH.write_text(
        json.dumps(submissions, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {rel(SUBMISSIONS_PATH)}")
    return 0


def api_poll(args: argparse.Namespace) -> int:
    token = token_from_env()
    if not SUBMISSIONS_PATH.exists():
        raise SystemExit(f"Missing {rel(SUBMISSIONS_PATH)}; run api-submit first.")
    submissions = json.loads(SUBMISSIONS_PATH.read_text(encoding="utf-8"))
    results: list[dict[str, Any]] = []
    pending_states = {"waiting-file", "pending", "running", "converting"}
    for submission in submissions:
        batch_id = submission["batch_id"]
        while True:
            result = api_json("GET", f"{BASE_URL}/api/v4/extract-results/batch/{batch_id}", token)
            if result.get("code") != 0:
                raise SystemExit(f"Poll failed: {result}")
            data = result["data"]
            extract_result = data.get("extract_result", [])
            states = {row.get("state") for row in extract_result}
            if args.download:
                download_done_results(submission, extract_result)
            if not states.intersection(pending_states) or not args.wait:
                results.append({"batch_id": batch_id, "data": data})
                break
            print(f"{batch_id}: {sorted(states)}; sleeping {args.interval}s")
            time.sleep(args.interval)
    RESULTS_PATH.write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {rel(RESULTS_PATH)}")
    return 0


def download_done_results(submission: dict[str, Any], rows: list[dict[str, Any]]) -> None:
    task_by_data_id = {task["data_id"]: task for task in submission["tasks"]}
    for row in rows:
        if row.get("state") != "done" or not row.get("full_zip_url"):
            continue
        data_id = row.get("data_id")
        task = task_by_data_id.get(data_id)
        if not task:
            continue
        zip_path = ZIP_DIR / task["slug"] / f"part_{task['task_index']:03d}.zip"
        raw_dir = API_RAW_DIR / task["slug"] / f"part_{task['task_index']:03d}"
        if zip_path.exists() and raw_dir.exists():
            continue
        zip_path.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(row["full_zip_url"], timeout=600) as response:
            zip_path.write_bytes(response.read())
        raw_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path) as archive:
            archive.extractall(raw_dir)


def find_markdown(raw_dir: Path) -> Path | None:
    candidates = sorted(
        raw_dir.rglob("*.md"),
        key=lambda path: (path.name != "full.md", path.stat().st_size * -1),
    )
    if not candidates:
        return None
    for candidate in candidates:
        if candidate.name == "full.md":
            return candidate
    return max(candidates, key=lambda path: path.stat().st_size)


def api_promote(_: argparse.Namespace) -> int:
    if not PARTS_PATH.exists():
        raise SystemExit(f"Missing {rel(PARTS_PATH)}; run prepare-parts first.")
    tasks = [PdfTask(**row) for row in json.loads(PARTS_PATH.read_text(encoding="utf-8"))]
    promoted: list[str] = []
    by_slug: dict[str, list[PdfTask]] = {}
    items = {item.slug: item for item in iter_pdfs()}
    for task in tasks:
        by_slug.setdefault(task.slug, []).append(task)
    for slug, slug_tasks in by_slug.items():
        item = items[slug]
        book_dir = OUT_ROOT / slug
        book_dir.mkdir(parents=True, exist_ok=True)
        combined: list[str] = []
        for task in sorted(slug_tasks, key=lambda row: row.task_index):
            raw_dir = API_RAW_DIR / slug / f"part_{task.task_index:03d}"
            markdown = find_markdown(raw_dir)
            if not markdown:
                continue
            body = markdown.read_text(encoding="utf-8", errors="replace")
            part_md = book_dir / f"book.part_{task.task_index:03d}.mineru.md"
            front_matter = front_matter_for(item, task, markdown)
            part_md.write_text(front_matter + body, encoding="utf-8")
            promoted.append(rel(part_md))
            combined.append(f"\n\n<!-- part {task.task_index}: pages {task.page_start}-{task.page_end} -->\n\n{body}")
        if combined:
            book_md = book_dir / "book.mineru.md"
            book_md.write_text(front_matter_for(item, None, None) + "".join(combined), encoding="utf-8")
            promoted.append(rel(book_md))
    print(json.dumps({"promoted": promoted}, ensure_ascii=False, indent=2))
    return 0


def front_matter_for(item: PdfItem, task: PdfTask | None, markdown: Path | None) -> str:
    page_range = "" if task is None else f"{task.page_start}-{task.page_end}"
    raw_markdown = "" if markdown is None else rel(markdown)
    status = "generated" if task is None else "generated_part"
    return (
        "---\n"
        "type: source\n"
        f"title: {item.title}\n"
        "format: mineru-api-markdown\n"
        f"raw_path: {item.pdf_path}\n"
        f"mineru_raw_markdown: {raw_markdown}\n"
        f"source_pages: {item.pages if item.pages is not None else ''}\n"
        f"page_range: {page_range}\n"
        f"generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"status: {status}\n"
        "---\n\n"
    )


def inventory(args: argparse.Namespace) -> int:
    items = filter_items(iter_pdfs(), args.only)
    index_path = write_index(items)
    print(json.dumps([asdict(item) for item in items], ensure_ascii=False, indent=2))
    print(f"Wrote {rel(index_path)}")
    return 0


def api_check(_: argparse.Namespace) -> int:
    token = os.environ.get("MINERU_API_TOKEN", "").strip()
    payload = {
        "token_present": bool(token),
        "parts": PARTS_PATH.exists(),
        "submissions": SUBMISSIONS_PATH.exists(),
        "results": RESULTS_PATH.exists(),
        "downloads": API_RAW_DIR.exists(),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if token else 2


def bool_arg(value: str) -> bool:
    normalized = value.lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError("Expected true/false")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    inv = sub.add_parser("inventory", help="Write PDF inventory and MinerU index.")
    inv.add_argument("--only", action="append", help="Filter PDFs by title/slug text.")
    inv.set_defaults(func=inventory)

    prep = sub.add_parser("prepare-parts", help="Write API task plan using page_ranges.")
    prep.add_argument("--only", action="append", help="Filter PDFs by title/slug text.")
    prep.add_argument("--max-pages", type=int, default=MAX_PAGES_PER_TASK)
    prep.set_defaults(func=prepare_parts)

    check = sub.add_parser("api-check", help="Check API token and local API state.")
    check.set_defaults(func=api_check)

    submit = sub.add_parser("api-submit", help="Submit planned PDF tasks to MinerU API.")
    submit.add_argument("--only", action="append", help="Filter PDFs by title/slug text.")
    submit.add_argument("--max-pages", type=int, default=MAX_PAGES_PER_TASK)
    submit.add_argument("--batch-size", type=int, default=10)
    submit.add_argument("--limit", type=int, help="Submit only first N tasks for testing.")
    submit.add_argument("--model-version", default="vlm", choices=["pipeline", "vlm", "MinerU-HTML"])
    submit.add_argument("--language", default="en")
    submit.add_argument("--enable-formula", type=bool_arg, default=True)
    submit.add_argument("--enable-table", type=bool_arg, default=True)
    submit.add_argument("--is-ocr", type=bool_arg, default=False)
    submit.add_argument(
        "--extra-format",
        action="append",
        choices=["docx", "html", "latex"],
        help="Optional additional export format. Can be repeated.",
    )
    submit.set_defaults(func=api_submit)

    poll = sub.add_parser("api-poll", help="Poll submitted MinerU API batches.")
    poll.add_argument("--wait", action="store_true", help="Keep polling until tasks leave pending/running states.")
    poll.add_argument("--interval", type=int, default=60)
    poll.add_argument("--download", action="store_true", help="Download and extract completed result zips.")
    poll.set_defaults(func=api_poll)

    promote = sub.add_parser("api-promote", help="Promote downloaded API Markdown into stable book files.")
    promote.set_defaults(func=api_promote)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
