g <-
 
buildSNNGraph
(sce.pbmc, 
k=
10
, 
use.dimred =
 
'PCA'
)


clust <-
 
igraph
::
cluster_walktrap
(g)
$
membership


colLabels
(sce.pbmc) <-
 
factor
(clust)
