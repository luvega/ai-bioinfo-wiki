set.seed
(
11000
)


reducedDim
(sce.pbmc, 
"force"
) <-
 
igraph
::
layout_with_fr
(nn.clust.info
$
objects
$
graph)


plotReducedDim
(sce.pbmc, 
colour_by=
"label"
, 
dimred=
"force"
)
