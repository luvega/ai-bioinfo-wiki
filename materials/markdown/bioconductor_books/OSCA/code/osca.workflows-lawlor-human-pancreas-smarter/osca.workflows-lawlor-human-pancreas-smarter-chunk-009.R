library
(scran)


set.seed
(
1000
)


clusters <-
 
quickCluster
(sce.lawlor)


sce.lawlor <-
 
computeSumFactors
(sce.lawlor, 
clusters=
clusters)


sce.lawlor <-
 
logNormCounts
(sce.lawlor)
