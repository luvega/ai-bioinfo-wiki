library
(scran)


set.seed
(
1000
)


clusters <-
 
quickCluster
(sce.muraro)


sce.muraro <-
 
computeSumFactors
(sce.muraro, 
clusters=
clusters)


sce.muraro <-
 
logNormCounts
(sce.muraro)
