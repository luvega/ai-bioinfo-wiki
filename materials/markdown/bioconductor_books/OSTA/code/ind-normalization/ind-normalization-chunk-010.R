sizeFactors
(
spe
)
 
<-
 
spe
$
cell_area
 
/
 
median
(
spe
$
cell_area
)


spe
 
<-
 
logNormCounts
(
spe
, name
=
"normalized_by_area"
)
