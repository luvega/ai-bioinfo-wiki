sfe
 
<-
 
runUnivariate
(
sfe
, 


    type
=
"localmoran"
, 


    features
=
topGenes
, 


    colGraphName
=
"knn6"
, 


    BPPARAM
=
bp
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
topGenes
,


    colGeometryName
=
"centroids"
,


    divergent
=
TRUE
,


    diverge_center
=
0
,


    ncol
=
3
)
