library
(scran)




set.seed
(
10000
)


clusters <-
 
quickCluster
(sce.mess)


sce.mess <-
 
computeSumFactors
(sce.mess, 
cluster=
clusters)


sce.mess <-
 
logNormCounts
(sce.mess)
