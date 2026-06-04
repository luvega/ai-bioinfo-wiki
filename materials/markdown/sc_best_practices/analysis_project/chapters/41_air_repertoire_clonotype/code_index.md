# Code Index · Clonotype analysis

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 6 | python | 15 | False | `import warnings` |
| 7 | python | 1 | True | `sc.logging.print_versions()` |
| 8 | python | 4 | False | `path_data = "/home/icb/juan.henao/BestPracticeStart/data"` |
| 10 | python | 13 | True | `adata = adata[` |
| 12 | python | 1 | False | `ir.pp.ir_dist(adata, sequence="aa")` |
| 14 | python | 3 | True | `ir.tl.define_clonotype_clusters(` |
| 16 | python | 1 | False | `ir.tl.clonotype_network(adata, min_cells=50, sequence="aa")` |
| 18 | python | 8 | True | `_ = ir.pl.clonotype_network(` |
| 19 | python | 1 | False | `adata.obs["cc_aa_identity"] = adata.obs["cc_aa_identity"].astype("str")` |
| 21 | python | 8 | True | `adata.obs.loc[adata.obs["cc_aa_identity"] == "0", :].groupby(` |
| 23 | python | 10 | True | `ir.tl.clonal_expansion(adata, target_col="cc_aa_identity")` |
| 25 | python | 3 | True | `_ = ir.pl.clonal_expansion(` |
| 27 | python | 3 | True | `_ = ir.pl.alpha_diversity(` |
| 30 | python | 7 | True | `_ = ir.pl.group_abundance(` |
| 32 | python | 21 | True | `# By condition` |
| 35 | python | 19 | True | `_ = ir.pl.group_abundance(` |
| 37 | python | 12 | True | `_ = ir.pl.group_abundance(` |
| 39 | python | 7 | True | `_ = ir.pl.vdj_usage(` |
| 41 | python | 1 | True | `adata.obs[adata.obs["IR_VDJ_1_d_call"] == "TRBD2"].cc_aa_identity.value_counts()` |
| 42 | python | 8 | True | `_ = ir.pl.vdj_usage(` |
| 45 | python | 8 | True | `_ = ir.pl.spectratype(` |
| 47 | python | 9 | True | `_ = ir.pl.spectratype(` |
| 49 | python | 13 | True | `_ = ir.pl.spectratype(` |
| 52 | python | 13 | False | `motif = compute_motif(` |
| 53 | python | 3 | False | `_ = svg_logo(` |
| 57 | python | 3 | False | `df, dst, lk = ir.tl.repertoire_overlap(` |
| 58 | python | 1 | True | `df` |
| 59 | python | 1 | True | `dst` |
| 60 | python | 1 | True | `lk` |
| 62 | python | 3 | True | `ir.pl.repertoire_overlap(` |
| 64 | python | 6 | True | `_ = ir.pl.repertoire_overlap(` |
| 67 | python | 17 | False | `import warnings` |
| 68 | python | 1 | True | `sc.logging.print_versions()` |
| 70 | python | 4 | False | `path_data = "/home/icb/juan.henao/BestPracticeStart/data"` |
| 71 | python | 1 | False | `adata = adata_bcr[adata_bcr.obs["patient_id"].isin(["COVID-064", "COVID-014"])].copy()` |
| 73 | python | 2 | True | `vdjx = ddl.from_scirpy(adata)` |
| 75 | python | 10 | False | `vdjx.data["v_call"].replace("", np.nan, inplace=True)` |
| 77 | python | 2 | True | `ddl.pp.calculate_threshold(vdjx, model="hh_s5f", plot=False)` |
| 79 | python | 1 | True | `ddl.tl.define_clones(vdjx, key_added="changeo_clone_id", model="hh_s5f")` |
| 81 | python | 3 | True | `ddl.tl.generate_network(` |
| 83 | python | 15 | True | `ddl.tl.transfer(adata, vdjx, clone_key="changeo_clone_id", expanded_only=True)` |
| 85 | python | 2 | False | `ddl.tl.clone_size(vdjx, clone_key="changeo_clone_id")` |
| 86 | python | 10 | True | `sc.set_figure_params(figsize=[10, 10])` |
| 88 | python | 2 | False | `ddl.tl.clone_size(vdjx, clone_key="changeo_clone_id", max_size=50)` |
| 89 | python | 9 | True | `_ = ddl.pl.clone_network(` |
| 91 | python | 8 | True | `mpl.rcParams.update(mpl.rcParamsDefault)` |
| 93 | python | 14 | True | `_ = (` |
| 95 | python | 7 | True | `_ = ddl.pl.barplot(` |
| 97 | python | 11 | True | `_ = ddl.pl.spectratype(` |
| 99 | python | 1 | False | `ddl.tl.transfer(adata, vdjx, clone_key="changeo_clone_id")` |
| 100 | python | 9 | False | `motif = compute_motif(` |
| 101 | python | 3 | False | `_ = svg_logo(` |
| 103 | python | 9 | False | `motif = compute_motif(` |
| 104 | python | 3 | False | `_ = svg_logo(` |
