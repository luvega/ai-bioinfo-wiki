snn.gr <-
 
buildSNNGraph
(residuals, 
use.dimred=
"corrected"
)


clusters.resid <-
 
igraph
::
cluster_walktrap
(snn.gr)
$
membership


tab.resid <-
 
table
(
Cluster=
clusters.resid, 
Batch=
residuals
$
batch)


tab.resid
