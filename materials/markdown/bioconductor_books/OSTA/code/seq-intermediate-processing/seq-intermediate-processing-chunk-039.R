# compute cluster-wise averages


pbs
 
<-
 
aggregateAcrossCells
(
spe
, 


    ids 
=
 
spe
$
BayesSpace
, subset.row 
=
 
top
, 


    use.assay.type 
=
 
"logcounts"
, statistics 
=
 
"mean"
)
