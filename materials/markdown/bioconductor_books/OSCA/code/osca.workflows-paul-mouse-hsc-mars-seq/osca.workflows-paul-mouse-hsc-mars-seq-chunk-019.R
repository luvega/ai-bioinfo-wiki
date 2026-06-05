snn.gr <-
 
buildSNNGraph
(sce.paul, 
use.dimred=
"PCA"
, 
type=
"jaccard"
)


colLabels
(sce.paul) <-
 
factor
(igraph
::
cluster_louvain
(snn.gr)
$
membership)
