# cluster cells by neighborhood compositions


ctx
 
<-
 
kmeans
(
sqe
$
aggregatedNeighbors
, centers
=
5
)


table
(
sqe
$
ctx
 
<-
 
factor
(
ctx
$
cluster
)
)
