# Code Index · Lineage tracing

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 10 | bash | 1 | True | `!wget "https://zenodo.org/record/5847462/files/KPTracer-Data.tar.gz?download=1"` |
| 11 | bash | 1 | False | `!tar -xvzf KPTracer-Data.tar.gz?download=1` |
| 13 | python | 6 | False | `import cassiopeia as cas` |
| 15 | python | 5 | True | `allele_table = pd.read_csv(` |
| 17 | python | 8 | False | `all_tumors = allele_table["Tumor"].unique()` |
| 20 | python | 4 | True | `primary_nt_allele_table.groupby(["Tumor"]).agg({"intBC": "nunique"}).plot(kind="bar")` |
| 23 | python | 7 | True | `primary_nt_allele_table.groupby(["Tumor"]).agg({"cellBC": "nunique"}).sort_values(` |
| 26 | python | 5 | True | `indel_priors = cas.pp.compute_empirical_indel_priors(` |
| 27 | python | 1 | True | `indel_priors.sort_values(by="count").head(5)` |
| 29 | python | 122 | False | `# utility functions for computing summary statistics` |
| 31 | python | 1 | False | `tumor_clone_statistics = summarize_tumor_quality(primary_nt_allele_table)` |
| 32 | python | 44 | True | `NUM_CELLS_THRESH = 100` |
| 35 | python | 10 | True | `tumor = "3726_NT_T1"` |
| 36 | python | 9 | True | `(` |
| 38 | python | 1 | False | `tree = cas.data.CassiopeiaTree(character_matrix=character_matrix, priors=priors)` |
| 39 | python | 1 | False | `greedy_solver = cas.solver.VanillaGreedySolver()` |
| 41 | python | 3 | True | `greedy_solver.solve(tree)` |
| 45 | python | 1 | False | `cas.tl.compute_expansion_pvalues(tree, min_clade_size=(0.15 * tree.n_cell), min_depth=1)` |
| 46 | python | 8 | False | `# this specifies a p-value for identifying expansions unlikely to have occurred` |
| 47 | python | 1 | True | `cas.pl.plot_matplotlib(tree, clade_colors={expanding_nodes[6]: "red"})` |
| 50 | python | 20 | True | `kptracer_adata = sc.read_h5ad("KPTracer-Data/expression/adata_processed.nt.h5ad")` |
| 52 | python | 5 | True | `tree.cell_meta = pd.DataFrame(` |
| 54 | python | 5 | True | `parsimony = cas.tl.score_small_parsimony(tree, meta_item="Cluster-Name")` |
| 56 | python | 21 | False | `# compute plasticities for each node in the tree` |
| 57 | python | 16 | True | `cas.pl.plot_matplotlib(tree, meta_data=["scPlasticity"])` |
