# Code Index · Dimensionality Reduction

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 17 | True | `import warnings` |
| 8 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 10 | python | 1 | False | `del mdata["prot"].layers["counts"]` |
| 12 | python | 1 | True | `mdata["prot"].var.index[:50]` |
| 13 | python | 4 | False | `isotype_controls = ["Mouse-IgG1", "Mouse-IgG2a", "Mouse-IgG2b", "Rat-IgG2b"]` |
| 15 | python | 1 | False | `mu.pp.filter_var(data=mdata["prot"], var=temp.tolist())` |
| 17 | python | 1 | True | `mdata["prot"].var.index[:50]` |
| 18 | python | 1 | True | `mdata["prot"]` |
| 21 | python | 1 | False | `sc.pp.pca(mdata["prot"], svd_solver="arpack", random_state=0)` |
| 23 | python | 1 | True | `sc.pl.pca_variance_ratio(mdata["prot"], n_pcs=50)` |
| 25 | python | 1 | False | `sc.pp.neighbors(mdata["prot"], n_pcs=20, random_state=0)` |
| 26 | python | 1 | False | `sc.tl.umap(mdata["prot"], random_state=0)` |
| 28 | python | 1 | True | `sc.pl.umap(mdata["prot"], color=["donor", "batch"])` |
| 30 | python | 1 | True | `sc.pl.umap(mdata["prot"], color=["CD4-1", "CD8", "CD3"])` |
| 32 | python | 6 | True | `af_dimensionality_reduction = ln.Artifact.from_mudata(` |
| 33 | python | 1 | True | `ln.finish()` |
