snn.gr <-
 
buildSNNGraph
(sce.grun.hsc, 
use.dimred=
"PCA"
)


colLabels
(sce.grun.hsc) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
