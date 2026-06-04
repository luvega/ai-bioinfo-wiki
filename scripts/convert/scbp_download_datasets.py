"""Download accessible SCBP datasets into ignored outputs cache and update manifests."""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from scbp_utils import ANALYSIS_ROOT, DATASET_OUTPUT_ROOT, USER_AGENT, read_json, safe_name, sha256_file, write_json


def downloadable(item: dict[str, Any]) -> bool:
    return item.get("kind") == "url" and item.get("status") == "pending_download"


def download_with_limit(url: str, target: Path, *, max_bytes: int, timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    target.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            length_header = response.headers.get("Content-Length")
            if length_header and int(length_header) > max_bytes:
                return {"status": "blocked_oversize", "reason": f"Content-Length {length_header} exceeds limit {max_bytes}."}
            with target.open("wb") as handle:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > max_bytes:
                        handle.close()
                        target.unlink(missing_ok=True)
                        return {"status": "blocked_oversize", "reason": f"Downloaded bytes exceed limit {max_bytes}."}
                    handle.write(chunk)
    except urllib.error.HTTPError as exc:
        return {"status": "failed", "reason": f"HTTP {exc.code}: {exc.reason}"}
    except urllib.error.URLError as exc:
        return {"status": "failed", "reason": str(exc.reason)}
    except TimeoutError:
        return {"status": "failed", "reason": "Timeout"}
    if total == 0:
        target.unlink(missing_ok=True)
        return {"status": "failed_empty", "reason": "Downloaded zero bytes."}
    return {"status": "downloaded", "bytes": total, "sha256": sha256_file(target), "local_path": target.as_posix()}


def run_write(max_mb: int, timeout: int) -> dict[str, Any]:
    manifest_path = ANALYSIS_ROOT / "datasets_manifest.json"
    if not manifest_path.exists():
        raise SystemExit("Run scbp_build_analysis_project.py --write before downloading datasets.")
    manifest = read_json(manifest_path)
    DATASET_OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    max_bytes = max_mb * 1024 * 1024
    updated: list[dict[str, Any]] = []
    downloaded = 0
    blocked = 0
    for index, item in enumerate(manifest.get("items", []), start=1):
        record = dict(item)
        if downloadable(item):
            url = item["value"]
            suffix = Path(url.split("?", 1)[0]).suffix
            target = DATASET_OUTPUT_ROOT / f"{index:04d}_{safe_name(item.get('source', 'source'))}{suffix or '.dat'}"
            result = download_with_limit(url, target, max_bytes=max_bytes, timeout=timeout)
            record.update(result)
            if result["status"] == "downloaded":
                downloaded += 1
            else:
                blocked += 1
        elif item.get("status") in {"blocked", "manual_required"}:
            blocked += 1
        updated.append(record)

    updated_manifest = {
        "version": 1,
        "max_download_mb": max_mb,
        "output_root": DATASET_OUTPUT_ROOT.as_posix(),
        "downloaded_count": downloaded,
        "blocked_or_manual_count": blocked,
        "items": updated,
    }
    write_json(manifest_path, updated_manifest)
    write_json(DATASET_OUTPUT_ROOT / "download_manifest.json", updated_manifest)
    write_report(updated_manifest)
    return {"downloaded": downloaded, "blocked_or_manual": blocked, "total": len(updated)}


def write_report(manifest: dict[str, Any]) -> None:
    lines = [
        "# SCBP Dataset Download Report",
        "",
        f"- Downloaded: {manifest['downloaded_count']}",
        f"- Blocked/manual: {manifest['blocked_or_manual_count']}",
        f"- Output root: `{manifest['output_root']}`",
        "",
        "| Status | Source | Value | Reason / Local path |",
        "|---|---|---|---|",
    ]
    for item in manifest["items"]:
        if item.get("status") in {"skipped_non_dataset", "context_required"}:
            continue
        reason = item.get("reason") or item.get("local_path") or ""
        value = str(item.get("value", "")).replace("|", "\\|")
        lines.append(f"| {item.get('status')} | `{item.get('source')}` | `{value[:140]}` | {reason} |")
    (ANALYSIS_ROOT / "dataset_download_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Download accessible datasets and update manifests.")
    parser.add_argument("--max-mb", type=int, default=200, help="Maximum size per downloaded data file.")
    parser.add_argument("--timeout", type=int, default=90, help="Network timeout in seconds per file.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.write:
        parser.error("Choose --write")
    print(json.dumps(run_write(args.max_mb, args.timeout), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
