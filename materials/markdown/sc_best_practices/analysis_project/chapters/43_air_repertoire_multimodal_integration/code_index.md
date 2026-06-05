# Code Index · Integrating AIR and transcriptomics

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 15 | False | `import warnings` |
| 5 | python | 8 | False | `path_data = "./data"` |
| 10 | python | 4 | False | `adata_tc = sc.read(path_gex_tcr)` |
| 12 | python | 2 | False | `sc.pp.neighbors(adata_tc)` |
| 14 | python | 2 | True | `sc.tl.umap(adata_tc)` |
| 17 | python | 4 | False | `adata_bc = sc.read(path_gex_bcr)` |
| 18 | python | 4 | True | `sc.pp.neighbors(adata_bc)` |
| 24 | python | 8 | True | `ir.pl.spectratype(` |
| 27 | python | 1 | True | `sc.pl.umap(adata_tc, color="IFNG")` |
| 29 | python | 3 | True | `adata_tc.obs["elevated_IFNG"] = adata_tc[:, "IFNG"].X.todense() > 3` |
| 31 | python | 28 | True | `from IPython.display import SVG` |
| 34 | python | 2 | False | `# TODO: remove clonotype definition once this is handled by clonotype chapter` |
| 36 | python | 3 | True | `# todo change once load clonotype annotated data` |
| 37 | python | 1 | False | `# TODO adapt to disease specific cells => Covid B cells against rest` |
| 41 | python | 1 | False | `adata_tc = adata_tc[~adata_tc.obs["IR_VDJ_1_junction_aa"].isna()].copy()` |
| 44 | python | 11 | True | `df_tcr = adata_tc.obs` |
| 46 | python | 3 | False | `n_genes = adata_tc.shape[1] // 10` |
| 48 | python | 11 | True | `count_mat = adata_tessa.X.A` |
| 50 | python | 13 | False | `settings_full = {` |
| 52 | python | 7 | True | `cmd_tessa = "source ~/.bashrc &&"` |
| 54 | python | 2 | False | `%%capture` |
| 56 | python | 4 | False | `tessa_embedding = pd.read_csv(f"{path_res}/TESSA_tcr_embedding.csv", index_col=0)` |
| 58 | python | 7 | True | `clustering = pd.read_csv(f"{path_res}/result_meta.csv", index_col=0)` |
| 60 | python | 9 | True | `sc.pp.neighbors(tessa_embedding)` |
| 62 | python | 7 | True | `mapping_dict = dict(` |
| 66 | python | 11 | False | `df_tcr = pd.read_csv(` |
| 67 | python | 6 | False | `cmd_conga_pp = (` |
| 68 | python | 2 | False | `%%capture` |
| 70 | python | 5 | False | `path_conga_gex = f"{path_tmp}/conga_gex.h5ad"` |
| 72 | python | 9 | False | `cmd_conga = f"cd {path_res} && "` |
| 73 | python | 2 | False | `%%capture` |
| 77 | python | 8 | False | `import sys` |
| 79 | python | 1 | False | `adata_mvtcr = adata_tc[~adata_tc.obs["IR_VJ_1_junction_aa"].isna()].copy()` |
| 80 | python | 4 | True | `# todo delete once data is unified` |
| 82 | python | 10 | False | `pad = max(` |
| 84 | python | 3 | False | `train, val = group_shuffle_split(adata_mvtcr, group_col="clonotype", val_split=0.2)` |
| 86 | python | 7 | False | `params_experiment = {` |
| 88 | python | 4 | False | `params_optimization = {` |
| 90 | python | 2 | True | `n_runs = 1` |
| 92 | python | 3 | False | `best_trial = 0` |
| 94 | python | 2 | False | `mvtcr_embedding = model.get_latent(adata_mvtcr, metadata=[])` |
| 96 | python | 4 | False | `top_10_clones = mvtcr_embedding.obs["clonotype"].value_counts().head(10).index` |
| 98 | python | 3 | True | `sc.pp.neighbors(mvtcr_embedding)` |
| 102 | python | 4 | True | `adata_benisse = adata_bc[~adata_bc.obs["IR_VDJ_1_junction_aa"].isna()]` |
| 103 | python | 9 | True | `df_bcr = adata_benisse.obs` |
| 105 | python | 14 | True | `sc.pp.highly_variable_genes(adata_benisse, n_top_genes=1000)` |
| 107 | python | 4 | False | `path_bcr_contigs = f"{path_data}/BCR_00_read_aligned.csv"` |
| 109 | python | 5 | False | `settings_embedding = {` |
| 110 | python | 7 | True | `cmd_bcr_embedding = "source ~/.bashrc && "` |
| 111 | python | 2 | False | `%%capture` |
| 113 | python | 14 | True | `max_iter = 100` |
| 115 | python | 2 | False | `%%capture` |
| 117 | python | 3 | True | `from IPython.display import IFrame` |
| 119 | python | 18 | True | `benisse_clusters = pd.read_csv(f"{path_res}/clone_annotation.csv", index_col=0)` |
| 122 | python | 18 | True | `%run ../src/lib.py` |
