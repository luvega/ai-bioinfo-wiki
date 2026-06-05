# aggregate estimates by cluster


# (separately for sender/receiver)


mu
 
<-
 
aggregateAcrossCells
(
sce
, 


    ids
=
sce
$
Leiden
, 


    statistics
=
"mean"
,


    use.assay.type
=
assayNames
(
sce
)
)
