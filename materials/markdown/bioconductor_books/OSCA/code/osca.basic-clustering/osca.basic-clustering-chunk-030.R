set.seed
(
100
)


clust.mbkmeans <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
,


    
BLUSPARAM=
MbkmeansParam
(
centers=
10
))


table
(clust.mbkmeans)
