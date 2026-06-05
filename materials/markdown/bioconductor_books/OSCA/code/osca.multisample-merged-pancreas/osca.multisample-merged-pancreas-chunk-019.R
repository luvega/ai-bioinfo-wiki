set.seed
(
1011110
)


mnn.pancreas <-
 
fastMNN
(normed.pancreas)




# Bumping up 'k' to get broader clusters for this demonstration. 


snn.gr <-
 
buildSNNGraph
(mnn.pancreas, 
use.dimred=
"corrected"
, 
k=
20
)


clusters <-
 
igraph
::
cluster_walktrap
(snn.gr)
$
membership


clusters <-
 
factor
(clusters)


tab <-
 
table
(
Cluster=
clusters, 
Batch=
mnn.pancreas
$
batch)


tab
