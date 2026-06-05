# cell area-based normalization


sf
 
<-
 
(
.
 
<-
 
sub
$
cell_area
)
 
/
 
median
(
.
)


sub
 
<-
 
logNormCounts
(
sub
, size.factors
=
sf
)
