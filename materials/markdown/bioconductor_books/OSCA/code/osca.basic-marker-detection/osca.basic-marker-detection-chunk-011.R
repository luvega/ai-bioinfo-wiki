auc.only <-
 
chosen[,
grepl
(
"AUC"
, 
colnames
(chosen))]


auc.only[
order
(auc.only
$
mean.AUC,
decreasing=
TRUE
),]
