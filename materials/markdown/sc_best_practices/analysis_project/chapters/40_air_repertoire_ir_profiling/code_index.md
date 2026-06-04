# Code Index · Immune Receptor Profiling

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 9 | python | 3 | False | `path_data = "data/"` |
| 10 | bash | 2 | True | `! wget -O $path_bcr_input -nc https://figshare.com/ndownloader/files/35574338` |
| 12 | python | 13 | False | `import warnings` |
| 14 | python | 4 | False | `path_bcr_out = f"{path_data}/BCR_01_preprocessed.h5ad"` |
| 16 | python | 7 | True | `df_bcr_raw = pd.read_csv(path_bcr_input, index_col=0)` |
| 20 | python | 10 | True | `columns = [` |
| 22 | python | 4 | True | `columns += ["cdr3", "cdr3_nt"]` |
| 24 | python | 5 | True | `df_tcr_raw = pd.read_csv(path_tcr_input, sep="\t")` |
| 26 | python | 1 | True | `df_tcr_raw["full_length"].value_counts()` |
| 27 | python | 1 | True | `df_tcr_raw["productive"].value_counts()` |
| 29 | python | 2 | True | `adata_tcr = ir.io.read_10x_vdj(path_tcr_csv)` |
| 31 | python | 1 | True | `adata_tcr.obs.head(5)` |
| 33 | python | 31 | True | `patient_information = [` |
| 35 | python | 2 | True | `adata_tcr.obs[df_patient.columns] = df_patient` |
| 37 | python | 2 | True | `adata_bcr = ir.io.read_10x_vdj(path_bcr_input)` |
| 39 | python | 8 | True | `patient_information = ["barcode", "patient_id"]` |
| 41 | python | 2 | True | `adata_bcr.obs[df_patient.columns] = df_patient` |
| 44 | python | 1 | False | `ir.tl.chain_qc(adata_tcr)` |
| 45 | python | 1 | False | `ir.tl.chain_qc(adata_bcr)` |
| 49 | python | 1 | True | `_ = ir.pl.group_abundance(adata_tcr, groupby="Centre", target_col="chain_pairing")` |
| 51 | python | 3 | True | `_ = ir.pl.group_abundance(` |
| 53 | python | 6 | True | `_ = ir.pl.group_abundance(` |
| 55 | python | 1 | True | `adata_tcr.obs["chain_pairing"].value_counts()` |
| 57 | python | 9 | True | `adata_bcr_tmp = adata_bcr[` |
| 59 | python | 6 | True | `_ = ir.pl.group_abundance(` |
| 64 | python | 1 | True | `adata_bcr_tmp.obs["chain_pairing"].value_counts()` |
| 65 | python | 16 | True | `print(f"Amount of all B cells:\t\t\t\t{len(adata_bcr)}")` |
| 67 | python | 1 | True | `adata_bcr_tmp.obs["chain_pairing"].value_counts()` |
| 69 | python | 1 | True | `adata_tcr.obs["chain_pairing"].value_counts()` |
| 70 | python | 16 | True | `print(f"Amount of all T cells:\t\t\t\t{len(adata_tcr)}")` |
| 71 | python | 1 | True | `adata_tcr_tmp.obs["chain_pairing"].value_counts()` |
| 73 | python | 2 | False | `sc.write(adata=adata_tcr, filename=path_tcr_out)` |
| 75 | python | 18 | True | `%run ../src/lib.py` |
