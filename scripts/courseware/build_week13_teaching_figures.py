"""Generate Week 13 teaching SVG figures from fixed simulated data.

The outputs are teaching-only assets under outputs/ and are intentionally not
tracked in Git. They support PCA, clustering, heatmap, and UMAP explanation
without using external copyrighted figures.
"""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "teaching_figures" / "week_13"

SAMPLES = [
    ("Ctrl_1", "Control", -1.9, 0.2, -1.8, 0.1),
    ("Ctrl_2", "Control", -1.7, -0.1, -1.5, -0.2),
    ("Ctrl_3", "Control", -2.0, 0.0, -1.7, 0.3),
    ("Drug_1", "Drug", 1.8, 0.1, 1.6, 0.0),
    ("Drug_2", "Drug", 1.6, -0.3, 1.3, -0.4),
    ("Drug_3", "Drug", 2.2, 0.1, 1.9, 0.2),
]

MATRIX = [
    ("Ctrl_1", [10, 8, 4, 5, 7]),
    ("Ctrl_2", [11, 7, 5, 4, 6]),
    ("Ctrl_3", [9, 8, 4, 5, 7]),
    ("Drug_1", [17, 5, 8, 6, 4]),
    ("Drug_2", [16, 4, 9, 7, 5]),
    ("Drug_3", [18, 5, 8, 6, 4]),
]


def svg_shell(width: int, height: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n'
        '<rect width="100%" height="100%" fill="white"/>\n'
        '<style>text{font-family:Arial,"Microsoft YaHei",sans-serif;font-size:13px}'
        '.small{font-size:11px}.title{font-size:16px;font-weight:700}</style>\n'
        f"{body}\n</svg>\n"
    )


def scale_point(x: float, y: float, width: int = 520, height: int = 340) -> tuple[float, float]:
    sx = 70 + (x + 2.5) / 5.0 * (width - 130)
    sy = height - 60 - (y + 0.8) / 1.6 * (height - 120)
    return sx, sy


def scatter_svg(title: str, x_index: int, y_index: int, x_label: str, y_label: str) -> str:
    body = [
        f'<text x="20" y="28" class="title">{title}</text>',
        '<line x1="70" y1="280" x2="470" y2="280" stroke="#444"/>',
        '<line x1="70" y1="280" x2="70" y2="55" stroke="#444"/>',
        f'<text x="230" y="325">{x_label}</text>',
        f'<text x="12" y="170" transform="rotate(-90 12 170)">{y_label}</text>',
    ]
    for label, group, pc1, pc2, umap1, umap2 in SAMPLES:
        values = (label, group, pc1, pc2, umap1, umap2)
        x, y = scale_point(float(values[x_index]), float(values[y_index]))
        color = "#1f77b4" if group == "Control" else "#d62728"
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{color}" opacity="0.85"/>')
        body.append(f'<text x="{x + 9:.1f}" y="{y + 4:.1f}" class="small">{label}</text>')
    body.append('<text x="320" y="58" class="small">generated teaching example</text>')
    body.append('<text x="320" y="76" class="small">Observation only; not mechanism evidence</text>')
    return svg_shell(520, 340, "\n".join(body))


def heatmap_svg() -> str:
    values = [value for _, row in MATRIX for value in row]
    low, high = min(values), max(values)
    genes = ["GeneA", "GeneB", "GeneC", "GeneD", "GeneE"]
    body = ['<text x="20" y="28" class="title">Week 13 teaching heatmap</text>']
    for c, gene in enumerate(genes):
        body.append(f'<text x="{105 + c * 58}" y="55" class="small">{gene}</text>')
    for r, (sample, row) in enumerate(MATRIX):
        y = 70 + r * 36
        body.append(f'<text x="20" y="{y + 22}" class="small">{sample}</text>')
        for c, value in enumerate(row):
            ratio = (value - low) / (high - low)
            red = int(250 * ratio)
            blue = int(230 * (1 - ratio))
            fill = f"rgb({red + 5},70,{blue + 20})"
            x = 100 + c * 58
            body.append(f'<rect x="{x}" y="{y}" width="48" height="28" fill="{fill}" stroke="white"/>')
            body.append(f'<text x="{x + 16}" y="{y + 19}" class="small" fill="white">{value}</text>')
    body.append('<text x="20" y="310" class="small">Color is a teaching scale; real heatmaps require normalization notes.</text>')
    return svg_shell(460, 335, "\n".join(body))


def cluster_svg() -> str:
    body = [
        '<text x="20" y="28" class="title">Week 13 teaching cluster diagram</text>',
        '<text x="20" y="52" class="small">z-score matrix + Euclidean distance + complete linkage</text>',
    ]
    labels = ["Ctrl_1", "Ctrl_2", "Ctrl_3", "Drug_1", "Drug_2", "Drug_3"]
    for i, label in enumerate(labels):
        y = 82 + i * 34
        body.append(f'<text x="30" y="{y + 5}" class="small">{label}</text>')
        body.append(f'<line x1="90" y1="{y}" x2="160" y2="{y}" stroke="#555"/>')
    body.extend(
        [
            '<path d="M160 82 V150 M160 82 H190 M160 116 H190 M160 150 H190" stroke="#1f77b4" fill="none"/>',
            '<path d="M160 184 V252 M160 184 H190 M160 218 H190 M160 252 H190" stroke="#d62728" fill="none"/>',
            '<path d="M190 116 H250 V218 H190" stroke="#555" fill="none"/>',
            '<text x="270" y="120" class="small">Cluster labels are candidate groups</text>',
            '<text x="270" y="140" class="small">They depend on distance and linkage</text>',
            '<text x="270" y="240" class="small">Not diagnosis or mechanism evidence</text>',
        ]
    )
    return svg_shell(560, 320, "\n".join(body))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "week13_pca.svg").write_text(scatter_svg("Week 13 teaching PCA", 2, 3, "PC1", "PC2"), encoding="utf-8")
    (OUT / "week13_umap.svg").write_text(scatter_svg("Week 13 teaching UMAP preview", 4, 5, "UMAP1", "UMAP2"), encoding="utf-8")
    (OUT / "week13_heatmap.svg").write_text(heatmap_svg(), encoding="utf-8")
    (OUT / "week13_cluster.svg").write_text(cluster_svg(), encoding="utf-8")
    print(f"Wrote 4 SVG teaching figures to {OUT}")


if __name__ == "__main__":
    main()
