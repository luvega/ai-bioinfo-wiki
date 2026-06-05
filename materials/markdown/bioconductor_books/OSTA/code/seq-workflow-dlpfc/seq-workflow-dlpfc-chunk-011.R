# calculate per-spot QC metrics and store in colData


spe
 
<-
 
addPerCellQC
(
spe
, subsets
=
list
(
mito
=
is_mito
)
)
