# Code Index · Gene regulatory networks

| Cell | Language | Lines | Has outputs | First line |
|---:|---|---:|---|---|
| 4 | python | 5 | False | `# the installation of this package is required for the proper execution of this notebook.` |
| 5 | python | 1 | False | `suppressMessages(library(FigR))` |
| 7 | python | 2 | False | `library(zellkonverter)` |
| 10 | python | 2 | False | `sce <- readH5AD("../../data/openproblems_bmmc_multiome_genes_filtered.h5ad")` |
| 12 | python | 3 | False | `ncells = -1 # if using all cells` |
| 14 | python | 2 | False | `RNA <- sce[1:13431,]` |
| 16 | python | 4 | True | `if(!file.exists('allTFs_hg38.txt'))` |
| 17 | python | 14 | False | `# subset by cells:` |
| 19 | python | 6 | False | `if(nfeatures_atac != -1){` |
| 20 | python | 2 | True | `print(c(dim(ATAC), dim(RNA)))` |
| 21 | python | 1 | False | `UMAP <- reducedDim(ATAC, 'GEX_X_umap')` |
| 22 | python | 3 | False | `# counts variable (for later functions)` |
| 24 | python | 2 | False | `# Remove genes with zero expression across all cells` |
| 28 | python | 2 | False | `if(!suppressMessages(require("cisTopic")))` |
| 29 | python | 1 | False | `suppressMessages(library(cisTopic))` |
| 31 | python | 1 | False | `nCores = 2` |
| 32 | python | 4 | True | `cistopic_bkp_path <- "../../data/openproblems_bmmc_multiome_genes_filtered_atac_s1d1_counts_cisTopic.rds"` |
| 34 | python | 29 | True | `overwrite = TRUE # to visualize plots, this will always execute. Modify to FALSE to avoid replacing output from previous runs.` |
| 36 | python | 2 | True | `cisAssign <- readRDS(cistopic_bkp_path)` |
| 38 | python | 2 | False | `library(dplyr)` |
| 39 | python | 3 | True | `set.seed(123)` |
| 41 | python | 1 | False | `colData(ATAC)$cellAnnot <- colData(ATAC)$cell_type` |
| 42 | python | 2 | False | `colData(ATAC)$UMAP1 <- UMAP[,1]` |
| 43 | python | 6 | True | `# Plot` |
| 45 | python | 7 | False | `# if the hg38 genome is not installed successfully during environment building, it can be installed here.` |
| 46 | python | 1 | False | `suppressMessages(library(BSgenome.Hsapiens.UCSC.hg38))` |
| 47 | python | 2 | True | `# check object dimensions` |
| 50 | python | 3 | True | `library(Matrix)` |
| 51 | python | 2 | False | `ATAC_df <- as.data.frame(as.matrix(counts(ATAC)))` |
| 52 | python | 3 | False | `ATAC_df$seqnames <- sapply(strsplit(rownames(ATAC_df),"-"), `[`, 1)` |
| 53 | python | 2 | True | `ATAC_df <- subset(ATAC_df, grepl('chr', rownames(ATAC_df)))` |
| 54 | python | 3 | False | `ATAC.se <- makeSummarizedExperimentFromDataFrame(ATAC_df)` |
| 56 | python | 16 | False | `# This snippet can be run interactively, but it takes a long time.` |
| 58 | python | 3 | True | `cisCorr.filt <- cisCorr %>% filter(pvalZ <= 0.05)` |
| 59 | python | 3 | False | `if(nrow(cisCorr.filt) == 0)` |
| 61 | python | 1 | False | `library(ggrepel)` |
| 62 | python | 8 | True | `# Determine DORC genes` |
| 64 | python | 1 | False | `stopifnot(length(dorcGenes) > 30)` |
| 66 | python | 2 | True | `dorcMat <- getDORCScores(ATAC.se, dorcTab=cisCorr.filt, geneList=dorcGenes, nCores=nCores)` |
| 67 | python | 1 | False | `stopifnot(nrow(cellkNN) == ncol(dorcMat))` |
| 68 | python | 1 | False | `rownames(cellkNN) <- colnames(dorcMat)` |
| 70 | python | 1 | False | `library(doParallel)` |
| 71 | python | 2 | True | `# Smooth dorc scores using cell KNNs (k=30)` |
| 72 | python | 1 | False | `stopifnot(nrow(cellkNN) == ncol(RNAmat))` |
| 73 | python | 1 | False | `rownames(cellkNN) <- colnames(RNAmat)` |
| 74 | python | 3 | True | `# Smooth RNA using cell KNNs` |
| 75 | python | 2 | False | `library(ggplot2)` |
| 76 | python | 2 | False | `# Visualize on pre-computed UMAP` |
| 78 | python | 2 | True | `print(length(dorcGenes))` |
| 80 | python | 1 | False | `marker_gene = 'NFIA'` |
| 81 | python | 2 | True | `dorcg <- plotMarker2D(umap.d,dorcMat.s,markers = c(marker_gene),maxCutoff = "q0.99",` |
| 82 | python | 2 | True | `rnag <- plotMarker2D(umap.d,RNAmat.s,markers = c(marker_gene),maxCutoff = "q0.99",` |
| 84 | python | 3 | True | `options(repr.plot.width=12, repr.plot.height=6)` |
| 86 | python | 1 | True | `dim(dorcMat.s)` |
| 87 | python | 6 | True | `figR.d <- runFigRGRN(ATAC.se = ATAC.se, # Must be the same input as used in runGenePeakcorr()` |
| 90 | python | 12 | True | `require(ggplot2)` |
| 92 | python | 3 | True | `drivers <- rankDrivers(figR.d, rankBy = "meanScore",interactive = FALSE)` |
| 94 | python | 2 | True | `options(repr.plot.width=10, repr.plot.height=10)` |
| 96 | python | 2 | False | `library(grid)` |
| 97 | python | 10 | True | `options(repr.plot.width=10, repr.plot.height=10)` |
| 99 | python | 3 | False | `library(networkD3)` |
| 100 | python | 5 | False | `# generate the network` |
| 101 | python | 2 | True | `# in a local session, the network can be manipulated interactively` |
| 103 | python | 8 | False | `# If pandoc if not found by R, here the bin path in the environment has to be provided e.g. `envs/best_practices_regulons_rnanatac/bin`` |
| 104 | python | 9 | False | `# the network is saved as an image and shown for online purposes.` |
| 105 | python | 2 | True | `im <- load.image('network_tutorial_rna_atac.png')` |
| 107 | python | 1 | True | `sessionInfo()` |
| 110 | python | 6 | True | `%run ../src/lib.py` |
| 112 | python | 3 | True | `%run ../src/lib.py` |
