for
 (n 
in
 
names
(all.sce)) {


    g <-
 
buildSNNGraph
(all.sce[[n]], 
k=
10
, 
use.dimred=
'PCA'
)


    clust <-
 
igraph
::
cluster_walktrap
(g)
$
membership


    
colLabels
(all.sce[[n]])  <-
 
factor
(clust)


}
