g.adt <-
 
buildSNNGraph
(
altExp
(sce.pbmc), 
k=
10
, 
d=
NA
)


clust.adt <-
 
igraph
::
cluster_walktrap
(g.adt)
$
membership


colLabels
(
altExp
(sce.pbmc)) <-
 
factor
(clust.adt)
