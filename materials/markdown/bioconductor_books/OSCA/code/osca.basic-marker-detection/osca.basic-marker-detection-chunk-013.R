cohen.only <-
 
chosen[,
grepl
(
"logFC.cohen"
, 
colnames
(chosen))]


cohen.only[
order
(cohen.only
$
mean.logFC.cohen,
decreasing=
TRUE
),]
