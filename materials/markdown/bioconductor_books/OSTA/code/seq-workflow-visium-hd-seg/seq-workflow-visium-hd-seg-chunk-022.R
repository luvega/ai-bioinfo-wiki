sub
 
<-
 
list
(
mt
=
grep
(
"^MT-"
, 
rownames
(
sfe
)
)
)


sfe
 
<-
 
addPerCellQCMetrics
(
sfe
, subsets
=
sub
)
