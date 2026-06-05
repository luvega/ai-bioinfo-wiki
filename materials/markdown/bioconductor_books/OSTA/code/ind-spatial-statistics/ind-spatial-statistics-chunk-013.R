sfe
 
<-
 
runBivariate
(


    
sfe
,


    type
=
"locallee"
,


    colGraphName
=
 
"knn6"
,


    feature1
=
c
(
"EPCAM"
, 
"KRT7"
)
)


plotLocalResult
(


    
sfe
,


    name
=
"locallee"
,


    features
=
"KRT7__EPCAM"
,


    colGeometryName
=
"centroids"
,


    divergent
=
TRUE
, diverge_center
=
0
)
