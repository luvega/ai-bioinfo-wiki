library
(scran)


nn.clusters <-
 
clusterCells
(sce.pbmc, 
use.dimred=
"PCA"
)


table
(nn.clusters)
