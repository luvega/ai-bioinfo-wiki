# Code Index · Neighborhood analysis

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 3 | python | 5 | False | `import scanpy as sc` |
| 5 | python | 1 | False | `adata = sq.datasets.visium_hne_adata()` |
| 7 | python | 1 | True | `sq.gr.spatial_neighbors(adata)` |
| 9 | python | 1 | True | `sq.gr.nhood_enrichment(adata, cluster_key="cluster")` |
| 11 | python | 1 | True | `adata.uns["cluster_nhood_enrichment"]` |
| 14 | python | 1 | True | `sq.pl.nhood_enrichment(adata, cluster_key="cluster", method="average", figsize=(5, 5))` |
| 17 | python | 1 | True | `sq.gr.interaction_matrix(adata, cluster_key="cluster")` |
| 19 | python | 1 | True | `adata.uns["cluster_interactions"]` |
| 21 | python | 1 | True | `sq.pl.interaction_matrix(adata, cluster_key="cluster", method="average", figsize=(5, 5))` |
| 24 | python | 2 | True | `sq.gr.co_occurrence(adata, cluster_key="cluster")` |
