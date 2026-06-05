detect.only <-
 
chosen[,
grepl
(
"logFC.detected"
, 
colnames
(chosen))]


detect.only[
order
(detect.only
$
mean.logFC.detected,
decreasing=
TRUE
),]
