# Code Index · Clustering

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 10 | True | `import lamindb as ln` |
| 8 | python | 2 | False | `af = ln.Artifact.get(key="cellular_structure/s4d8_subset.h5ad", is_latest=True)` |
| 10 | python | 2 | False | `sc.pp.neighbors(adata, n_pcs=30)` |
| 12 | python | 1 | False | `sc.tl.leiden(adata, flavor="igraph", n_iterations=2)` |
| 15 | python | 9 | False | `sc.tl.leiden(` |
| 17 | python | 5 | True | `sc.pl.umap(` |
| 20 | python | 6 | True | `af = ln.Artifact.from_anndata(` |
