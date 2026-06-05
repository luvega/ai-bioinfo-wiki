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
 
deg
, 


    use.assay.type 
=
 
"logcounts"
, statistics 
=
 
"mean"
)
