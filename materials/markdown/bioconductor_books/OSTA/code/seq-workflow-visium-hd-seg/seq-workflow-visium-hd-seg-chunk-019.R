# get cell areas = 4x number of 2um bins


sfe
$
um2
 
<-
 
4
*
sapply
(
sfe
$
map
, 
nrow
)


# get fraction of 2um bins that are nuclear


sfe
$
nuc
 
<-
 
sapply
(
sfe
$
map
, \
(
.
)
 
mean
(
.
$
in_nucleus
)
)


# get nucleus areas = cell area x nuclear fraction


sfe
$
nuc_um2
 
<-
 
sfe
$
um2
*
sfe
$
nuc
