library
(BiocSingular)


set.seed
(
101010011
)


sce.mam <-
 
denoisePCA
(sce.mam, 
technical=
dec.mam, 
subset.row=
top.mam)


sce.mam <-
 
runTSNE
(sce.mam, 
dimred=
"PCA"
)
