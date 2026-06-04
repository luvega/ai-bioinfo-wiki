# Code Index · Dimensionality Reduction

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 12 | True | `import lamindb as ln` |
| 5 | python | 4 | False | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 7 | python | 1 | False | `adata.X = adata.layers["scran_normalization"]` |
| 9 | python | 3 | False | `# setting highly variable as highly deviant to use scanpy 'use_highly_variable' argument in sc.pp.pca` |
| 10 | python | 1 | True | `sc.pl.pca_scatter(adata, color="total_counts")` |
| 13 | python | 1 | False | `sc.tl.tsne(adata, use_rep="X_pca")` |
| 14 | python | 1 | True | `sc.pl.tsne(adata, color="total_counts")` |
| 17 | python | 2 | False | `sc.pp.neighbors(adata)` |
| 18 | python | 1 | True | `sc.pl.umap(adata, color="total_counts")` |
| 21 | python | 4 | True | `sc.pl.umap(` |
| 23 | python | 6 | True | `af = ln.Artifact(` |
