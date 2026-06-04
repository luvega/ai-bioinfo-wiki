# Code Index · Annotation

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 17 | True | `import warnings` |
| 7 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 10 | python | 1 | True | `sc.pl.umap(mdata["prot"], frameon=False, color="CD45")` |
| 12 | python | 1 | True | `mdata["prot"].var[mdata["prot"].var.gene_ids.str.contains("CD38")]` |
| 14 | python | 8 | False | `sc.tl.leiden(` |
| 16 | python | 5 | True | `sc.tl.rank_genes_groups(mdata["prot"], groupby="leiden")` |
| 18 | python | 1 | True | `sc.pl.umap(mdata["prot"], color="leiden")` |
| 20 | python | 2 | True | `# B cells` |
| 23 | python | 2 | True | `# T cells` |
| 25 | python | 3 | True | `# NKT cells are CD3+ and CD56+` |
| 26 | python | 2 | True | `# Monocytes` |
| 27 | python | 2 | True | `# Dendritic` |
| 28 | python | 2 | True | `# CD16 is expressed in NK cells and in CD16 monocytes, which are CD14-, CD16+ and CD11c+` |
| 30 | python | 15 | False | `mdata["prot"].obs["celltype"] = mdata["prot"].obs.leiden.copy()` |
| 31 | python | 7 | True | `sc.pl.umap(` |
| 33 | python | 6 | True | `af_annotation = ln.Artifact.from_mudata(` |
| 34 | python | 1 | True | `ln.finish()` |
