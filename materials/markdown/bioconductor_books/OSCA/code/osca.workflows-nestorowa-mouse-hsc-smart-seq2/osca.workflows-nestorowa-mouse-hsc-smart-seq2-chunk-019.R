snn.gr <-
 
buildSNNGraph
(sce.nest, 
use.dimred=
"PCA"
)


colLabels
(sce.nest) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
