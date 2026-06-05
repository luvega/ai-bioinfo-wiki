library
(scran)


set.seed
(
101000110
)


clusters <-
 
quickCluster
(sce.paul)


sce.paul <-
 
computeSumFactors
(sce.paul, 
clusters=
clusters)


sce.paul <-
 
logNormCounts
(sce.paul)
