# cell area-based normalization


sf
 
<-
 
(
.
 
<-
 
sub
$
Area
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
