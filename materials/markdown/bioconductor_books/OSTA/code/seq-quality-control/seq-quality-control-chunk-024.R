# detect local outliers based on library size, unique genes, mito. percentage


spe
 
<-
 
localOutliers
(
spe
, metric
=
"sum"
, direction
=
"lower"
, log
=
TRUE
)


spe
 
<-
 
localOutliers
(
spe
, metric
=
"detected"
, direction
=
"lower"
, log
=
TRUE
)


spe
 
<-
 
localOutliers
(
spe
, metric
=
"subsets_mito_percent"
, direction
=
"higher"
, log
=
FALSE
)
