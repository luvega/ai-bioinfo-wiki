# estimate threshold on counts per area


# (3 MADs from the median, using log2 scale)


nc
 
<-
 
xen
$
total_counts
 
/
 
xen
$
cell_area


ol
 
<-
 
isOutlier
(
nc
, log
=
TRUE
, type
=
"lower"
, nmads
=
3
)


(
th
 
<-
 
attr
(
ol
, 
"threshold"
)
[
1
]
)
