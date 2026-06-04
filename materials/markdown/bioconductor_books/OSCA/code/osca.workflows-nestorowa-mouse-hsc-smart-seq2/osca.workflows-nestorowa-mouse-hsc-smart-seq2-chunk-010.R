library
(scran)


set.seed
(
101000110
)


clusters <-
 
quickCluster
(sce.nest)


sce.nest <-
 
computeSumFactors
(sce.nest, 
clusters=
clusters)


sce.nest <-
 
logNormCounts
(sce.nest)
