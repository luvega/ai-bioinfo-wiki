# Code Index · Cell-cell communication

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 9 | python | 9 | False | `# python libs` |
| 10 | python | 6 | False | `# Setting up R dependencies` |
| 11 | r | 9 | False | `%%R` |
| 12 | python | 4 | False | `# figure settings` |
| 15 | python | 7 | False | `# Read in` |
| 17 | python | 2 | False | `sc.pp.filter_cells(adata, min_genes=200)` |
| 18 | python | 8 | False | `# Store the counts for later use` |
| 20 | python | 3 | False | `# log1p normalize the data` |
| 22 | python | 1 | True | `adata.obs["cell_type"].cat.categories` |
| 24 | python | 1 | True | `sc.pl.umap(adata, color=["condition", "cell_type"], frameon=False)` |
| 27 | python | 2 | True | `adata_stim = adata[adata.obs["condition"] == "stim"].copy()` |
| 28 | python | 2 | False | `# import cellphonedb method via liana` |
| 31 | python | 3 | True | `cellphonedb(` |
| 33 | python | 1 | True | `adata_stim.uns["liana_res"].head()` |
| 37 | python | 19 | True | `li.pl.dotplot(` |
| 42 | python | 1 | True | `li.method.show_methods()` |
| 44 | python | 1 | False | `from liana.method import rank_aggregate` |
| 45 | python | 3 | True | `rank_aggregate(` |
| 47 | python | 3 | True | `adata_stim.uns["liana_res"].drop_duplicates(` |
| 50 | python | 23 | True | `li.pl.dotplot(` |
| 56 | r | 5 | False | `%%R` |
| 57 | r | 7 | False | `%%R` |
| 60 | python | 2 | False | `sender_celltypes = ["CD4 T cells", "B cells", "FCGR3A+ Monocytes"]` |
| 62 | python | 19 | False | `# Helper function to obtain sufficiently expressed genes` |
| 63 | python | 14 | False | `sender_expressed = reduce(` |
| 65 | r | 13 | False | `%%R -i sender_expressed -i receiver_expressed` |
| 68 | python | 9 | False | `# Get pseudo-bulk profile` |
| 70 | python | 11 | True | `# Storing the raw counts` |
| 72 | python | 8 | False | `logFCs, pvals = dc.get_contrast(` |
| 74 | python | 2 | True | `# Visualize those for e.g. CD14+ Monocytes` |
| 75 | python | 5 | True | `# format results` |
| 77 | python | 7 | False | `# define background of sufficiently expressed genes` |
| 79 | r | 13 | True | `%%R -i geneset_oi -i background_genes -o ligand_activities` |
| 81 | r | 42 | False | `%%R -o vis_ligand_target` |
| 82 | python | 10 | True | `# convert dot to underscore and set ligand as index` |
| 84 | python | 3 | True | `fig, ax = plt.subplots(1, 1, figsize=(15, 5))` |
| 89 | python | 1 | False | `ligand_oi = ligand_activities.head(3)["test_ligand"].values` |
| 90 | python | 1 | True | `ligand_oi` |
| 91 | python | 21 | True | `li.pl.dotplot(` |
| 99 | python | 25 | True | `%run ../src/lib.py` |
| 102 | r | 2 | True | `%%R` |
| 103 | python | 1 | True | `session_info.show()` |
