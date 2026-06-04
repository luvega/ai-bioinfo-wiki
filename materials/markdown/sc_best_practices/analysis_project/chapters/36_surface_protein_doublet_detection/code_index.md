# Code Index · Doublet detection

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 5 | python | 17 | True | `import warnings` |
| 8 | python | 5 | True | `af = ln.Artifact.connect("theislab/sc-best-practices").get(` |
| 11 | python | 1 | True | `sc.pl.scatter(mdata["prot"], x="CD3", y="CD19-1", color="log1p_total_counts")` |
| 14 | python | 1 | True | `sc.pl.scatter(mdata["prot"], x="CD3", y="CD14-1", color="log1p_total_counts")` |
| 16 | python | 2 | False | `genes2filter = ["CD3", "CD19-1", "CD14-1"]` |
| 17 | python | 7 | False | `mdata["prot"].obs["doublets_markers"] = [` |
| 19 | python | 1 | True | `sc.pl.violin(mdata["prot"], keys="log1p_total_counts", groupby="doublets_markers")` |
| 21 | python | 2 | True | `mdata = mdata[mdata["prot"].obs["doublets_markers"] == "False"].copy()` |
| 23 | python | 6 | True | `af_doublet_detection = ln.Artifact.from_mudata(` |
| 24 | python | 1 | True | `ln.finish()` |
