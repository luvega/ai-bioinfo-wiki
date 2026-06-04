snn.gr <-
 
buildSNNGraph
(sce.mam, 
use.dimred=
"PCA"
, 
k=
25
)


colLabels
(sce.mam) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
