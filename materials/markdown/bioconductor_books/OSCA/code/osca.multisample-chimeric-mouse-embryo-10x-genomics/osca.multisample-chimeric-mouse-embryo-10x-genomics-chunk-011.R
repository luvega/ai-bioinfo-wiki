g <-
 
buildSNNGraph
(merged, 
use.dimred=
"corrected"
)


clusters <-
 
igraph
::
cluster_louvain
(g)


colLabels
(merged) <-
 
factor
(clusters
$
membership)
