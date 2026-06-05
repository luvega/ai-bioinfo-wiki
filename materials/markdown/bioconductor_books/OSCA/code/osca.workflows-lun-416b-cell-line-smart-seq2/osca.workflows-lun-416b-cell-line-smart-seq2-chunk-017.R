my.dist <-
 
dist
(
reducedDim
(sce
.416
b, 
"PCA"
))


my.tree <-
 
hclust
(my.dist, 
method=
"ward.D2"
)




library
(dynamicTreeCut)


my.clusters <-
 
unname
(
cutreeDynamic
(my.tree, 
distM=
as.matrix
(my.dist),


    
minClusterSize=
10
, 
verbose=
0
))


colLabels
(sce
.416
b) <-
 
factor
(my.clusters)
