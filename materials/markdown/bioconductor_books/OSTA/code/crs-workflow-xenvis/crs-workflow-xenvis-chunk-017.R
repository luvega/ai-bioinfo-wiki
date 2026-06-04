sub
 
<-
 
list
(
gs
=
intersect
(
rownames
(
vis
)
, 
rownames
(
xen
)
)
)


vis
 
<-
 
addPerCellQCMetrics
(
vis
, subsets
=
sub
)
