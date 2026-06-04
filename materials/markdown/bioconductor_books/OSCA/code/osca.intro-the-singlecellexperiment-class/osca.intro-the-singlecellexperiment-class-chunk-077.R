sce <-
 
scater
::
logNormCounts
(sce)


sce <-
 
scater
::
runPCA
(sce)


dim
(
reducedDim
(sce, 
"PCA"
))
