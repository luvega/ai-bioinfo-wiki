# convert from SPE to SFE


sfe
 
<-
 
toSpatialFeatureExperiment
(
spe
)


# add cell segmentation boundaries


seg
 
<-
 
metadata
(
spe
)
$
cellseg


i
 
<-
 
colnames
(
spe
)


j
 
<-
 
match
(
i
, 
seg
$
cell_id
)


seg
 
<-
 
seg
[
j
, 
]
; 
rownames
(
seg
)
 
<-
 
i


colGeometries
(
sfe
)
 
<-
 
list
(
cellseg
=
seg
)
