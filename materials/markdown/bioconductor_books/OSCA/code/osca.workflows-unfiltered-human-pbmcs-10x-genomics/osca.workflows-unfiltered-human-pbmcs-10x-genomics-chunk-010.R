library
(scran)


set.seed
(
1000
)


clusters <-
 
quickCluster
(sce.pbmc)


sce.pbmc <-
 
computeSumFactors
(sce.pbmc, 
cluster=
clusters)


sce.pbmc <-
 
logNormCounts
(sce.pbmc)
