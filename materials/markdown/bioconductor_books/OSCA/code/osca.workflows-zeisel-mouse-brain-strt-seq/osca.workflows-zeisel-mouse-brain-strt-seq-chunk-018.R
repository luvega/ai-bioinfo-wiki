snn.gr <-
 
buildSNNGraph
(sce.zeisel, 
use.dimred=
"PCA"
)


colLabels
(sce.zeisel) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
