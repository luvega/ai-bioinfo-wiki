# set seed for random number generation


# in order to make results reproducible


set.seed
(
123
)




# run PCA on the sample


sfe
 
<-
 
runPCA
(
sfe
, exprs_values
=
"logcounts"
, ncomponents
=
50
)




# cluster based on first 10 PC's 


# using Leiden community detection


pcs
 
<-
 
reducedDim
(
sfe
, 
"PCA"
)
[
, 
1
:
10
]


params
 
<-
 
KNNGraphParam
(


    k
=
20
,


    cluster.fun
=
"leiden"
,


    cluster.args
=
list
(


        resolution
=
0.3
,


        objective_function
=
"modularity"
)
)


colData
(
sfe
)
$
cluster
 
<-
 
clusterRows
(
pcs
, BLUSPARAM
=
params
)




# visualize cluster assignments


plotSpatialFeature
(
sfe
, 


    features
=
"cluster"
, colGeometryName
=
"centroids"
)
 
+


    
guides
(
col
=
guide_legend
(
override.aes
=
list
(
size
=
2
)
)
)
