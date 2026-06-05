g <-
 
buildSNNGraph
(merged.pbmc, 
use.dimred=
"corrected"
)


colLabels
(merged.pbmc) <-
 
factor
(igraph
::
cluster_louvain
(g)
$
membership)


table
(
colLabels
(merged.pbmc), merged.pbmc
$
batch)
