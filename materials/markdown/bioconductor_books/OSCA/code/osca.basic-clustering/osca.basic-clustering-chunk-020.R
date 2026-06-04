clust.none <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
KNNGraphParam
())


table
(clust.none)
