from pathlib import Path
import importlib.util
import sys


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "convert" / "ingest_bioconductor_books.py"
spec = importlib.util.spec_from_file_location("ingest_bioconductor_books", MODULE_PATH)
ingest = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ingest
spec.loader.exec_module(ingest)


PACKAGES_FIXTURE = """Package: OSTA
Version: 1.2.0
License: CC BY 4.0
MD5sum: 89ceba272612bd2568b182050118bc5f
NeedsCompilation: no

Package: OSCA
Version: 1.22.0
License: CC BY 4.0
MD5sum: 8395f439cac3b696db6d0f9a7aa1b08c
NeedsCompilation: no
"""


HTML_FIXTURE = """<!doctype html>
<html>
<body>
<main id="quarto-document-content">
<h1>Quality control for Visium workflows</h1>
<p>Example body text.</p>
<img src="seq-quality-control_files/figure-html/quality-plot-1.png" alt="QC plot">
<pre class="sourceCode r"><code>library(scater)
plotColData(spe, y = "sum")</code></pre>
<pre><code class="language-python">import pandas as pd
pd.read_csv("counts.csv")</code></pre>
</main>
</body>
</html>
"""


def test_parse_bioconductor_packages_metadata():
    records = ingest.parse_packages(PACKAGES_FIXTURE, "https://bioconductor.org/packages/3.23/books/src/contrib/")

    osta = records["OSTA"]
    assert osta.version == "1.2.0"
    assert osta.license == "CC BY 4.0"
    assert osta.md5 == "89ceba272612bd2568b182050118bc5f"
    assert osta.tarball_url == "https://bioconductor.org/packages/3.23/books/src/contrib/OSTA_1.2.0.tar.gz"


def test_extract_page_content_images_and_code_chunks():
    page = ingest.extract_page_content(
        HTML_FIXTURE,
        "https://bioconductor.org/books/release/OSTA/seq-quality-control.html",
        "OSTA",
    )

    assert page.title == "Quality control for Visium workflows"
    assert page.slug == "seq-quality-control"
    assert len(page.images) == 1
    assert page.images[0].original_url == (
        "https://bioconductor.org/books/release/OSTA/"
        "seq-quality-control_files/figure-html/quality-plot-1.png"
    )
    assert {chunk.language for chunk in page.code_chunks} == {"r", "python"}
    assert "plotColData" in page.code_chunks[0].code


def test_rewrite_images_to_local_raw_asset_paths():
    page = ingest.extract_page_content(
        HTML_FIXTURE,
        "https://bioconductor.org/books/release/OSTA/seq-quality-control.html",
        "OSTA",
    )

    rewritten = ingest.rewrite_images_to_local_assets(page.markdown, page.images)

    assert "materials/raw/bioconductor_books/assets/OSTA/seq-quality-control/quality-plot-1.png" in rewritten
    assert page.images[0].original_url.endswith("quality-plot-1.png")


def test_workflow_chapters_map_to_case_weeks_without_status_changes():
    weeks = ingest.map_workflow_weeks("Visium quality control and spatial transcriptomics workflow")

    assert weeks == [14, 16, 17]
