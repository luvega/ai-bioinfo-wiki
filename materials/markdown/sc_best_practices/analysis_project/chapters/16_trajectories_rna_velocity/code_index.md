# Code Index · RNA velocity

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 18 | python | 3 | False | `import warnings` |
| 19 | python | 5 | True | `import lamindb as ln` |
| 21 | python | 1 | False | `scv.settings.set_figure_params("scvelo")` |
| 24 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 27 | python | 1 | True | `scv.pp.filter_and_normalize(adata, min_shared_counts=20, n_top_genes=2000)` |
| 29 | python | 3 | True | `sc.tl.pca(adata)` |
| 31 | python | 1 | True | `scv.pl.scatter(adata, basis="umap", color="clusters")` |
| 34 | python | 1 | True | `scv.tl.velocity(adata, mode="deterministic")` |
| 36 | python | 2 | True | `scv.tl.velocity_graph(adata, n_jobs=8)` |
| 39 | python | 1 | True | `scv.tl.recover_dynamics(adata, n_jobs=8)` |
| 41 | python | 2 | True | `top_genes = adata.var["fit_likelihood"].sort_values(ascending=False).index` |
| 43 | python | 3 | True | `scv.tl.velocity(adata, mode="dynamical")` |
