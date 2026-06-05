# More resolved.


clust
.5
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
5
))


table
(clust
.5
)
