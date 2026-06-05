library
(scran)


set.seed
(
100
)


clust.zeisel <-
 
quickCluster
(sce.zeisel) 


table
(clust.zeisel)
