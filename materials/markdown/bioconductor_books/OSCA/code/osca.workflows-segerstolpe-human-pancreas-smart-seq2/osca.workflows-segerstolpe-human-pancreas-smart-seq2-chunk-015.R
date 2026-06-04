library
(BiocSingular)


set.seed
(
101011001
)


sce.seger <-
 
runPCA
(sce.seger, 
subset_row=
chosen.hvgs, 
ncomponents=
25
)


sce.seger <-
 
runTSNE
(sce.seger, 
dimred=
"PCA"
)
