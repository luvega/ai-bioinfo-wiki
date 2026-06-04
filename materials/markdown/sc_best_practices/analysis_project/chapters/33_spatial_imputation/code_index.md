# Code Index · Imputation

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 9 | False | `import matplotlib.pyplot as plt` |
| 6 | python | 5 | True | `adata_sc = sc.read(` |
| 8 | python | 4 | True | `sc.pp.neighbors(adata_sc)` |
| 10 | python | 5 | True | `adata_st = sc.read(` |
| 11 | python | 3 | True | `sc.pl.spatial(` |
| 13 | python | 2 | True | `markers = list(set.intersection(set(adata_sc.var_names), set(adata_st.var_names)))` |
| 15 | python | 1 | True | `tg.pp_adatas(adata_sc, adata_st, genes=markers)` |
| 17 | python | 4 | True | `assert "training_genes" in adata_sc.uns` |
| 19 | python | 8 | True | `ad_map = tg.map_cells_to_space(` |
| 21 | python | 1 | True | `ad_map` |
| 24 | python | 9 | True | `# Project the cell annotation to spatial locations` |
| 25 | python | 2 | True | `#  To get a deeper sense, Tangram also computes several scores, which are readily plotted` |
| 27 | python | 2 | True | `ad_ge = tg.project_genes(adata_map=ad_map, adata_sc=adata_sc)` |
| 29 | python | 2 | True | `genes = ["tek", "stab2", "hc"]` |
| 30 | python | 1 | True | `ad_ge` |
| 31 | python | 8 | True | `# The comparison between original measurements on predicted ones is easily done with tangram` |
| 33 | python | 8 | True | `genes = ["rp1", "sox17", "mrpl15"]` |
| 36 | python | 18 | False | `control_markers = [` |
| 37 | python | 32 | True | `fig, ax = plt.subplots(1, len(control_markers), figsize=(25, 6.8), sharey=True)` |
