# Code Index · Batch correction

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 17 | True | `import warnings` |
| 8 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 11 | python | 1 | True | `sc.external.pp.harmony_integrate(adata=mdata["prot"], key="donor", random_state=0)` |
| 13 | python | 2 | False | `sc.pp.neighbors(mdata["prot"], n_pcs=20, use_rep="X_pca_harmony", random_state=0)` |
| 14 | python | 1 | True | `sc.pl.umap(mdata["prot"], color=["donor", "batch"])` |
| 16 | python | 2 | True | `sc.pl.umap(mdata["prot"], color=["CD4-1", "CD8", "CD3"])` |
| 18 | python | 6 | True | `af_batch_correction = ln.Artifact.from_mudata(` |
| 19 | python | 1 | True | `ln.finish()` |
