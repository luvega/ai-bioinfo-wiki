cos
 
<-
 
computeSpatialOutlier
(
cos
, computeBy
=
"total"
, method
=
"mc"
)


cos
 
<-
 
computeSpatialOutlier
(
cos
, computeBy
=
"Area_um"
, method
=
"mc"
)


plotMetricHist
(
cos
, metric
=
"total"
, useFences
=
"total_outlier_mc"
)
 
+


plotMetricHist
(
cos
, metric
=
"Area_um"
, useFences
=
"Area_um_outlier_mc"
)
