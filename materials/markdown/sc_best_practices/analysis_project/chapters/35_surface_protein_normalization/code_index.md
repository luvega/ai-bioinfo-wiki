# Code Index · Normalization

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 16 | True | `import warnings` |
| 8 | python | 6 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 10 | python | 6 | True | `af_raw = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 13 | python | 10 | True | `sc.pp.calculate_qc_metrics(mdata_raw["rna"], inplace=True, percent_top=None)` |
| 15 | python | 1 | False | `isotype_controls = ["Mouse-IgG1", "Mouse-IgG2a", "Mouse-IgG2b", "Rat-IgG2b"]` |
| 16 | python | 3 | False | `mdata["prot"].layers["counts"] = mdata[` |
| 18 | python | 1 | False | `mu.prot.pp.dsb(mdata, mdata_raw, isotype_controls=isotype_controls, random_state=0)` |
| 20 | python | 1 | True | `pd.Series(mdata["prot"].layers["counts"][:100, :100].toarray().flatten()).value_counts()` |
| 22 | python | 1 | True | `pd.Series(mdata["prot"].X[:100, :100].flatten()).value_counts()` |
| 24 | python | 3 | True | `sns.histplot(mdata["prot"].layers["counts"].sum(axis=1), bins=50)` |
| 26 | python | 3 | True | `sns.histplot(mdata["prot"].X.sum(axis=1), bins=50)` |
| 30 | python | 2 | False | `mdata_clr_normalize = mdata.copy()` |
| 32 | python | 1 | False | `mu.prot.pp.clr(mdata_clr_normalize["prot"])` |
| 34 | python | 1 | True | `pd.Series(mdata["prot"].layers["counts"][:100, :100].toarray().flatten()).value_counts()` |
| 35 | python | 1 | True | `pd.Series(mdata_clr_normalize["prot"].X[:100, :100].toarray().flatten()).value_counts()` |
| 37 | python | 3 | True | `sns.histplot(mdata_clr_normalize["prot"].X.sum(axis=1), bins=50)` |
| 40 | python | 6 | True | `af_normalization = ln.Artifact.from_mudata(` |
| 41 | python | 1 | True | `ln.finish()` |
