# NOTE: conversion to SCE is a temporary fix for a 'Statial' bug 


# reported here: https://github.com/SydneyBioX/Statial/issues/16


tmp
 
<-
 
as
(
.vhd8
, 
"SingleCellExperiment"
)


tmp
 
<-
 
getDistances
(
tmp
, 


    cellType
=
".DeconLabel1"
, imageID
=
"sample_id"
,


    spatialCoords
=
names
(
xy
)
, maxDist
=
200
, nCores
=
4
)


reducedDim
(
.vhd8
, 
"distances"
)
 
<-
 
reducedDim
(
tmp
, 
"distances"
)
