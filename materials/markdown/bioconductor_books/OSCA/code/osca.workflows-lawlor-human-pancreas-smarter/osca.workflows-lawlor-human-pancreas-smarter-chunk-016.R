snn.gr <-
 
buildSNNGraph
(sce.lawlor, 
use.dimred=
"PCA"
)


colLabels
(sce.lawlor) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
