# determine outliers based on 


# - low log-library size


# - few uniquely detected features


# - high mitochondrial count fraction


.vhd16
 
<-
 
localOutliers
(
.vhd16
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


.vhd16
 
<-
 
localOutliers
(
.vhd16
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


.vhd16
 
<-
 
localOutliers
(
.vhd16
, metric
=
"subsets_mt_percent"
, direction
=
"higher"
, log
=
TRUE
)


.vhd16
$
discard
 
<-
 


    
.vhd16
$
sum_outliers
 
|
 


    
.vhd16
$
detected_outliers
 
|
 


    
.vhd16
$
subsets_mt_percent_outliers


# tabulate number of bins retained 


# vs. removed by any criterion 


table
(
.vhd16
$
discard
)
