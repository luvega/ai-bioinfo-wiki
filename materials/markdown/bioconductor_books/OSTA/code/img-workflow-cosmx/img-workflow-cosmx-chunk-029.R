# convert to SFE & remove cells with NA labels


sfe
 
<-
 
as
(
sub
, 
"SpatialFeatureExperiment"
)


sfe
 
<-
 
sfe
[
, 
!
is.na
(
sfe
$
SingleR_label
)
]




# this is needed for Voyager's plotting functions


colnames
(
sfe
$
polygons
)
[
6
]
 
<-
 
"geometry"


st_geometry
(
sfe
$
polygons
)
 
<-
 
"geometry"


colGeometry
(
sfe
, 
"cellSeg"
)
 
<-
 
sfe
$
polygons




colGraph
(
sfe
, 
"poly2nb"
)
 
<-
 


    
findSpatialNeighbors
(
sfe
,


        type
=
"cellSeg"
, 


        method
=
"poly2nb"
, 


        style
=
"W"
, snap
=
50
)




plotColGraph
(
sfe
, 


    colGraphName
=
"poly2nb"
, 


    colGeometryName
=
"cellSeg"
)
 
+
 


    
theme_void
(
)
