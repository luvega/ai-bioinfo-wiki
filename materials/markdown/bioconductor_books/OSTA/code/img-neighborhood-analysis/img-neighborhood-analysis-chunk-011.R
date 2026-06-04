library
(
imcRtools
)


# construct kNN-graph based on Euclidean distances


sqe
 
<-
 
buildSpatialGraph
(
spe
, 


    coords
=
spatialCoordsNames
(
spe
)
,


    img_id
=
"sample_id"
, type
=
"knn"
, k
=
10
)


# compute cluster frequencies among each cell's kNNs


sqe
 
<-
 
aggregateNeighbors
(
sqe
, 


    colPairName
=
"knn_interaction_graph"
, 


    aggregate_by
=
"metadata"
, count_by
=
"k"
)


# view composition of 1st cell's kNNs


unlist
(
sqe
$
aggregatedNeighbors
[
1
, 
]
)
