# Code Index · Quality control

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 6 | python | 22 | True | `import warnings` |
| 8 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 12 | python | 1 | False | `sc.pp.calculate_qc_metrics(mdata["prot"], inplace=True, percent_top=None)` |
| 14 | python | 1 | True | `sns.displot(mdata["prot"].obs.n_genes_by_counts)` |
| 16 | python | 3 | True | `sns.displot(` |
| 19 | python | 1 | True | `sns.displot(mdata["prot"].obs.total_counts)` |
| 21 | python | 3 | True | `sns.displot(` |
| 23 | python | 4 | True | `sc.pp.filter_cells(mdata["prot"], max_counts=100000)` |
| 26 | python | 1 | True | `sns.boxplot(y=mdata["prot"].obs.total_counts, x=mdata["prot"].obs["donor"])` |
| 28 | python | 6 | False | `def is_outlier(adata, metric: str, nmads: int):` |
| 29 | python | 8 | True | `outliers = []` |
| 30 | python | 1 | False | `mdata["prot"].obs["outliers"] = pd.concat(outliers)` |
| 31 | python | 1 | True | `mdata["prot"].obs.head()` |
| 33 | python | 2 | True | `mdata = mdata[~mdata["prot"].obs["outliers"]].copy()` |
| 35 | python | 1 | True | `sns.boxplot(y=mdata["prot"].obs.total_counts, x=mdata["prot"].obs["donor"])` |
| 37 | python | 6 | True | `af_quality_control = ln.Artifact.from_mudata(` |
| 38 | python | 1 | True | `ln.finish()` |
