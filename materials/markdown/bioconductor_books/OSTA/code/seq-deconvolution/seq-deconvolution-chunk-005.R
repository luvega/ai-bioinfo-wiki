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
vis
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
