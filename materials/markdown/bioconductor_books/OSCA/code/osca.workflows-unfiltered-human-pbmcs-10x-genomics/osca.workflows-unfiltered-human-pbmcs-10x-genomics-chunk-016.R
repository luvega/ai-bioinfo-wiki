set.seed
(
10000
)


sce.pbmc <-
 
denoisePCA
(sce.pbmc, 
subset.row=
top.pbmc, 
technical=
dec.pbmc)




set.seed
(
100000
)


sce.pbmc <-
 
runTSNE
(sce.pbmc, 
dimred=
"PCA"
)




set.seed
(
1000000
)


sce.pbmc <-
 
runUMAP
(sce.pbmc, 
dimred=
"PCA"
)
