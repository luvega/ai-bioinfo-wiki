library
(scran)


set.seed
(
101000110
)


clusters <-
 
quickCluster
(sce.mam)


sce.mam <-
 
computeSumFactors
(sce.mam, 
clusters=
clusters)


sce.mam <-
 
logNormCounts
(sce.mam)
