library
(scran)


set.seed
(
101000110
)


clusters <-
 
quickCluster
(sce.grun.hsc)


sce.grun.hsc <-
 
computeSumFactors
(sce.grun.hsc, 
clusters=
clusters)


sce.grun.hsc <-
 
logNormCounts
(sce.grun.hsc)
