"""Week 05: 数据读取与整理.

Small teaching script for checking the source-controlled dataset. It is not a
clinical or biological analysis workflow.
"""
from __future__ import annotations

import csv
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "datasets" / "week05_raw_glucose_table.csv"


def load_rows() -> list[dict[str, str]]:
    with DATA.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = load_rows()
    print(f"week=05; rows={len(rows)}; columns={list(rows[0]) if rows else []}")
    for row in rows[:3]:
        print(row)


if __name__ == "__main__":
    main()
