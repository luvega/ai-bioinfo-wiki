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


altExp
(sce.pbmc) <-
 
computeMedianFactors
(
altExp
(sce.pbmc))


sce.pbmc <-
 
applySCE
(sce.pbmc, logNormCounts)
