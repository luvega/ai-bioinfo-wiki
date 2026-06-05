clust.jaccard <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 


    
BLUSPARAM=
NNGraphParam
(
type=
"jaccard"
))


table
(clust.jaccard)
