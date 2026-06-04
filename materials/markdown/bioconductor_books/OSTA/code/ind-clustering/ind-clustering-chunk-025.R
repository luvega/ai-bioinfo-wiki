# average expression by clusters


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
Leiden
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
