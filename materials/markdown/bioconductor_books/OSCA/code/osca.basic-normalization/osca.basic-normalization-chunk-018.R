set.seed
(
100
)


clust.zeisel <-
 
quickCluster
(sce.zeisel) 


sce.zeisel <-
 
computeSumFactors
(sce.zeisel, 
cluster=
clust.zeisel, 
min.mean=
0.1
)


sce.zeisel <-
 
logNormCounts
(sce.zeisel)


assayNames
(sce.zeisel)
