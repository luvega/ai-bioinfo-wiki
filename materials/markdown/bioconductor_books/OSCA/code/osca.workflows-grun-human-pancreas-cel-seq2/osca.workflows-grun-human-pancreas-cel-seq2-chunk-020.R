snn.gr <-
 
buildSNNGraph
(merged.grun, 
use.dimred=
"corrected"
)


colLabels
(merged.grun) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
