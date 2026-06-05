clust.num <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
type=
"number"
))


table
(clust.num)
