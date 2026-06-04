# construct (K=6)NN-graph using cell centroids


knn6
 
<-
 
findSpatialNeighbors
(
sfe
, type
=
"centroids"
, method
=
"knearneigh"
, k
=
6
)


colGraph
(
sfe
, 
"knn6"
)
 
<-
 
knn6


# visualize across tissue section


plotColGraph
(
sfe
, 


    colGraphName
=
"knn6"
, 


    colGeometryName
=
"centroids"
, 


    segment_size
=
0.1
,


    geometry_size
=
0.1
)
 
+
 


    
theme_void
(
)
