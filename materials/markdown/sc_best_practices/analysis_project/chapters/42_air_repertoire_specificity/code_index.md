# Code Index · Specificity analysis

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 12 | False | `import warnings` |
| 6 | python | 3 | False | `path_data = "data"` |
| 7 | python | 2 | False | `# TODO final decision sampling: prosponed until remaining chapters are fixed` |
| 9 | python | 2 | True | `vdjdb = ir.datasets.vdjdb()` |
| 11 | python | 3 | True | `vdjdb[vdjdb.obs["antigen.species"] == "SARS-CoV-2"].obs[` |
| 12 | python | 3 | True | `vdjdb[vdjdb.obs["antigen.species"] == "SARS-CoV-2"].obs[` |
| 16 | python | 6 | True | `print(f"Amount of samples in VDJDB: {len(vdjdb)}")` |
| 18 | python | 4 | True | `adata_tcr.obs["has_vdjdb_overlap"] = adata_tcr.obs["IR_VDJ_1_junction_aa"].isin(` |
| 20 | python | 9 | False | `def assign_disease(cdr3beta):` |
| 22 | python | 6 | True | `adata_tcr.obs["antigen.species_manual"] = (` |
| 25 | python | 3 | False | `metric = "identity"` |
| 27 | python | 8 | True | `ir.tl.ir_query(` |
| 29 | python | 8 | True | `ir.tl.ir_query_annotate(` |
| 32 | python | 17 | True | `ir.tl.ir_query(` |
| 35 | python | 17 | True | `ir.tl.ir_query(` |
| 40 | python | 1 | False | `from tcrdist.repertoire import TCRrep` |
| 42 | python | 28 | False | `adata_tcrdist = adata_tcr[` |
| 44 | python | 17 | True | `dict_rename_tcrdist = {` |
| 46 | python | 1 | True | `tr = TCRrep(cell_df=df_tcrdist, organism="human", chains=["alpha", "beta"])` |
| 48 | python | 3 | False | `dist_total = tr.pw_alpha + tr.pw_beta` |
| 50 | python | 20 | True | `import scipy.cluster.hierarchy as hc` |
| 52 | python | 6 | False | `df_tcrdist_alpha = pd.DataFrame(` |
| 54 | python | 21 | False | `from scipy.sparse import csr_matrix` |
| 56 | python | 7 | True | `ir.tl.define_clonotype_clusters(` |
| 58 | python | 13 | True | `adata_tcrdist.obs["antigen.species"] = adata_tcrdist.obs["antigen.species"].astype(str)` |
| 61 | python | 11 | True | `adata_tcrmatch = adata_tcr[` |
| 63 | python | 8 | True | `df_tcrmatch["CDR3b_trimmed"] = df_tcrmatch["IR_VDJ_1_junction_aa"].str[1:-1]` |
| 65 | python | 2 | False | `cmd_tcrmatch = "cd TCRMatch/ &&"` |
| 67 | bash | 1 | False | `!$cmd_tcrmatch` |
| 69 | python | 11 | True | `dist_tcrmatch = pd.read_csv("tmp/tcrmatch_output.csv", sep="\t")` |
| 71 | python | 13 | True | `linkage = hc.linkage(sp.distance.squareform(dist_tcrmatch), method="average")` |
| 73 | python | 1 | False | `add_dists(adata_tcrmatch, None, dist_tcrmatch, "tcrmatch", 0.05)` |
| 74 | python | 22 | True | `ir.tl.define_clonotype_clusters(` |
| 77 | python | 1 | False | `adata_tcr_align = adata_tcr[adata_tcr.obs["patient_id"] == "AP6"].copy()` |
| 79 | python | 3 | True | `metric = "alignment"` |
| 80 | python | 8 | True | `ir.tl.ir_query(` |
| 81 | python | 9 | True | `ir.tl.ir_query_annotate(` |
| 85 | python | 13 | False | `adata_ergo = adata_tcr[` |
| 87 | python | 9 | False | `dict_rename = {` |
| 89 | python | 5 | False | `df_ergo["Peptide"] = "KLGGALQAK"  #'YLQPRTFLL'` |
| 91 | python | 5 | False | `cmd_ergo = "source ~/.bashrc &&"` |
| 92 | bash | 1 | True | `!$cmd_ergo` |
| 94 | python | 2 | True | `df_tcr_ergo = pd.read_csv("ERGO-II/results.csv", index_col=0)` |
| 96 | python | 1 | True | `sb.distplot(df_tcr_ergo["Score"])` |
| 97 | python | 3 | True | `import numpy as np` |
| 100 | python | 3 | False | `path_data = "data"` |
| 101 | python | 5 | False | `adata_bcr = adata_bcr[` |
| 104 | bash | 1 | True | `!wget -O tmp/CoV-AbDab.csv http://opig.stats.ox.ac.uk/webapps/covabdab/static/downloads/CoV-AbDab_200422.csv` |
| 106 | python | 3 | True | `cov_abdab = pd.read_csv("tmp/CoV-AbDab.csv")` |
| 108 | python | 10 | False | `dict_rename_cov_abdab = {` |
| 110 | python | 3 | False | `cov_abdab["has_ir"] = "True"` |
| 112 | python | 3 | False | `cov_abdab["Binding"] = cov_abdab["Binding"].apply(` |
| 114 | python | 2 | False | `cov_abdab["IR_VJ_1_junction_aa"] = "C" + cov_abdab["IR_VJ_1_junction_aa"] + "F"` |
| 116 | python | 3 | True | `cov_abdab = sc.AnnData(obs=cov_abdab)` |
| 118 | python | 16 | True | `metric = "identity"` |
| 120 | python | 17 | True | `ir.tl.ir_query(` |
| 123 | python | 21 | True | `metric = "hamming"` |
| 128 | python | 17 | True | `%run ../src/lib.py` |
