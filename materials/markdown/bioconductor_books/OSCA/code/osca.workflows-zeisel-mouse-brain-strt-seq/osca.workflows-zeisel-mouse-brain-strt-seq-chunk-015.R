library
(BiocSingular)


set.seed
(
101011001
)


sce.zeisel <-
 
denoisePCA
(sce.zeisel, 
technical=
dec.zeisel, 
subset.row=
top.hvgs)


sce.zeisel <-
 
runTSNE
(sce.zeisel, 
dimred=
"PCA"
)
