gs
 
<-
 
c
(
"Snap25"
, 
"Calm1"
)


sfe
 
<-
 
runUnivariate
(
sfe
,


    features
=
gs
,


    type
=
"localmoran"
,


    zero.policy
=
TRUE
,


    colGraphName
=
"poly2nb"
,


    colGeometryName
=
"cellSeg"
)




plotLocalResult
(
sfe
, 


    name
=
"localmoran"
,


    features
=
gs
, ncol
=
2
,


    colGeometryName
=
"cellSeg"
,


    divergent
=
TRUE
, diverge_center
=
0
)
