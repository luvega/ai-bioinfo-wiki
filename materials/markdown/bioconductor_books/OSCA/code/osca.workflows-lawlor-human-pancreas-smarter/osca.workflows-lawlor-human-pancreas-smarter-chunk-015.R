library
(BiocSingular)


set.seed
(
101011001
)


sce.lawlor <-
 
runPCA
(sce.lawlor, 
subset_row=
chosen.genes, 
ncomponents=
25
)


sce.lawlor <-
 
runTSNE
(sce.lawlor, 
dimred=
"PCA"
)
