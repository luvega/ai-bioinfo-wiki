p
 
<-
 
plotStateChanges
(


    cells
=
.vhd8
, 


    image
=
"sample01"
, 


    from
=
"Tumor"
, 


    to
=
"Fibroblast"
,


    marker
=
"FTH1"
, 


    cellType
=
".DeconLabel1"
, 


    imageID
=
"sample_id"
,


    spatialCoords
=
c
(
"array_col"
, 
"array_row"
)
)


p
$
image
 
+
 
facet_null
(
)
 
|
 
p
$
scatter
