# calculate per-cell QC metrics


mt
 
<-
 
grepl
(
"^MT-"
, 
rownames
(
.vhd16
)
)


.vhd16
 
<-
 
addPerCellQCMetrics
(
.vhd16
, subsets
=
list
(
mt
=
mt
)
)
