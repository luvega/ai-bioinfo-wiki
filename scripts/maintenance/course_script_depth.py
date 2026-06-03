"""Report lecture-script depth for AI_Course week scripts."""
from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def count_cjk(text: str) -> int:
    return sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")


def depth_label(cjk_count: int) -> str:
    if cjk_count >= 6500:
        return "full-lecture"
    if cjk_count >= 3500:
        return "pilot-script"
    if cjk_count >= 800:
        return "scaffold"
    return "placeholder"


def script_status(text: str) -> str:
    for line in text.splitlines()[:12]:
        if line.startswith("status:"):
            return line.split(":", 1)[1].strip()
    return ""


def build_report(root: Path) -> str:
    rows = [
        "# Course Script Depth Report",
        "",
        "This report only measures `script.md` frontmatter status and CJK character depth. It does not promote the whole week to `pilot_ready` or `formal_ready`; `materials.md`, `outline.md`, storyboard review, evidence review, and PPT visual QA are tracked separately.",
        "",
        "| Week | Status | CJK chars | Depth | Path |",
        "|---:|---|---:|---|---|",
    ]
    for week in range(1, 19):
        path = root / "course" / "weeks" / f"week_{week:02d}" / "script.md"
        if not path.exists():
            rows.append(f"| {week:02d} | missing | 0 | missing | `{path.as_posix()}` |")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        cjk = count_cjk(text)
        rows.append(
            f"| {week:02d} | {script_status(text)} | {cjk} | {depth_label(cjk)} | `{path.relative_to(root).as_posix()}` |"
        )
    return "\n".join(rows) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", type=Path, help="Optional report path to write.")
    args = parser.parse_args()
    root = args.root.resolve()
    report = build_report(root)
    if args.write:
        path = args.write if args.write.is_absolute() else root / args.write
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report, encoding="utf-8")
        print(path)
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
