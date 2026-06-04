colLabels
(sce.pbmc) <-
 
clust.kmeans


plotReducedDim
(sce.pbmc, 
"TSNE"
, 
colour_by=
"label"
)
