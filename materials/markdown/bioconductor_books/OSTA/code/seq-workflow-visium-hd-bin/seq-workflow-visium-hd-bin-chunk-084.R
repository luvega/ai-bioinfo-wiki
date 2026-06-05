.vhd8
 
<-
 
.vhd8
[
, 
!
is.na
(
.vhd8
$
.DeconLabel1
)
]


xy
 
<-
 
data.frame
(
spatialCoords
(
.vhd8
)
)


colData
(
.vhd8
)
[
names
(
xy
)
]
 
<-
 
xy


.vhd8
 
<-
 
getAbundances
(
.vhd8
, 


    spatialCoords
=
names
(
xy
)
,


    cellType
=
".DeconLabel1"
, 


    imageID
=
"sample_id"
, 


    r
=
200
, nCores
=
4
)
