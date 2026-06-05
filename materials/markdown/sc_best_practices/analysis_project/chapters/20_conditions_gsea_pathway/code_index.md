# Code Index · Gene set enrichment and pathway analysis

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 20 | python | 9 | False | `from __future__ import annotations` |
| 21 | python | 3 | False | `sc.settings.set_figure_params(dpi=200, frameon=False)` |
| 22 | python | 9 | False | `# Filtering warnings from current version of matplotlib` |
| 23 | python | 6 | False | `# Setting up R dependencies` |
| 24 | r | 4 | False | `%%R` |
| 25 | python | 4 | True | `adata = sc.read(` |
| 26 | python | 8 | False | `# Storing the counts for later use` |
| 27 | python | 4 | False | `# Finding highly variable genes using count data` |
| 28 | python | 1 | True | `adata` |
| 30 | python | 3 | True | `sc.pp.pca(adata)` |
| 31 | python | 6 | True | `sc.pl.umap(` |
| 33 | python | 1 | False | `adata.obs["group"] = adata.obs.condition.astype("string") + "_" + adata.obs.cell_type` |
| 34 | python | 2 | False | `# find DE genes by t-test` |
| 36 | python | 1 | False | `celltype_condition = "stim_FCGR3A+ Monocytes"  # 'stimulated_B',  'stimulated_CD8 T', 'stimulated_CD14 Mono'` |
| 37 | python | 15 | True | `# extract scores` |
| 42 | python | 5 | False | `# Downloading reactome pathways` |
| 43 | python | 15 | False | `def gmt_to_decoupler(pth: Path) -> pd.DataFrame:` |
| 44 | python | 1 | False | `reactome = gmt_to_decoupler("c2.cp.reactome.v7.5.1.symbols.gmt")` |
| 46 | python | 1 | True | `reactome` |
| 49 | python | 3 | False | `# Filtering genesets to match behaviour of fgsea` |
| 51 | python | 12 | False | `scores, norm, pvals = decoupler.run_gsea(` |
| 53 | python | 11 | True | `(` |
| 56 | python | 1 | True | `gsea_results.head(10)` |
| 60 | python | 8 | True | `%%time` |
| 61 | python | 1 | True | `adata` |
| 63 | python | 7 | False | `ifn_pathways = [` |
| 65 | python | 7 | True | `sc.pl.umap(` |
| 71 | python | 84 | False | `def subsampled_summation(` |
| 72 | python | 4 | True | `pb_data = subsampled_summation(` |
| 73 | python | 2 | False | `# Does PC1 captures a meaningful biological or technical fact?` |
| 75 | python | 1 | False | `pb_data.layers["counts"] = pb_data.X.copy()` |
| 76 | python | 3 | False | `sc.pp.normalize_total(pb_data)` |
| 77 | python | 1 | True | `sc.pl.pca(pb_data, color=["cell_type", "condition", "lib_size"], ncols=1, size=250)` |
| 80 | python | 1 | False | `groups = pb_data.obs.condition.astype("string") + "_" + pb_data.obs.cell_type` |
| 81 | r | 4 | True | `%%R -i groups` |
| 82 | r | 2 | True | `%%R` |
| 83 | r | 10 | False | `%%R ` |
| 85 | python | 1 | False | `log_norm_X = pb_data.to_df().T` |
| 86 | r | 5 | True | `%%R -i log_norm_X -i reactome` |
| 88 | r | 3 | False | `%%R` |
| 91 | r | 2 | False | `%%R -o fry_results` |
| 93 | python | 1 | True | `fry_results.head()` |
| 94 | python | 11 | True | `(` |
| 96 | r | 2 | False | `%%R -o fry_results_negative_ctrl` |
| 97 | python | 11 | True | `(` |
| 100 | python | 1 | False | `counts_df = pb_data.to_df(layer="counts").T` |
| 101 | r | 4 | True | `%%R -i counts_df` |
| 102 | r | 2 | False | `%%R -o logCPM` |
| 103 | python | 1 | False | `pb_data.uns["logCPM_FLE"] = logCPM.T  # FLE for filter low exprs` |
| 104 | python | 1 | False | `pb_data.obsm["logCPM_FLE_pca"] = sc.pp.pca(logCPM.T.to_numpy(), return_info=False)` |
| 105 | python | 1 | True | `sc.pl.embedding(pb_data, "logCPM_FLE_pca", color=pb_data.obs, ncols=1, size=250)` |
| 111 | python | 32 | True | `%run ../src/lib.py` |
| 113 | r | 2 | True | `%%R` |
| 114 | python | 1 | True | `session_info.show()` |
