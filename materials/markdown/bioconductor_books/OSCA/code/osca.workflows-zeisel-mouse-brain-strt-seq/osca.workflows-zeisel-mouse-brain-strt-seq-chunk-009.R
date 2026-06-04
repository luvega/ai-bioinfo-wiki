library
(scran)


set.seed
(
1000
)


clusters <-
 
quickCluster
(sce.zeisel)


sce.zeisel <-
 
computeSumFactors
(sce.zeisel, 
cluster=
clusters) 


sce.zeisel <-
 
logNormCounts
(sce.zeisel)
