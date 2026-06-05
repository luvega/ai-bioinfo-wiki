set.seed
(
100
)


clust.kmeans <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
KmeansParam
(
centers=
10
))


table
(clust.kmeans)
