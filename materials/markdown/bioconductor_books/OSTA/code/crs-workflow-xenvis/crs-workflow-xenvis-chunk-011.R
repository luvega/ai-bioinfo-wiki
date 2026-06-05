# do a fixed-radius search to get cell 


# centroids that fall on a given spot


nns
 
<-
 
nn2
(


    searchtype
=
"radius"
, radius
=
55
/
2
/
0.2125
, k
=
200
,


    data
=
spatialCoords
(
xen
)
, query
=
spatialCoords
(
vis
)
)
