# Less resolved.


clust
.50
 <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
, 
BLUSPARAM=
NNGraphParam
(
k=
50
))


table
(clust
.50
)
