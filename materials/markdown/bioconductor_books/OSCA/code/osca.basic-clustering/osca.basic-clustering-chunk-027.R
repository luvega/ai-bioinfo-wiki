set.seed
(
100
)


clust.kmeans2 <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
KmeansParam
(
centers=
20
))


table
(clust.kmeans2)
