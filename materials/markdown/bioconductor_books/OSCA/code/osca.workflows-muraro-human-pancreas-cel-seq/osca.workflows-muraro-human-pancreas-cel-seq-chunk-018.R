snn.gr <-
 
buildSNNGraph
(merged.muraro, 
use.dimred=
"corrected"
)


colLabels
(merged.muraro) <-
 
factor
(igraph
::
cluster_walktrap
(snn.gr)
$
membership)
