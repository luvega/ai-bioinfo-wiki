library
(scater)


is.mito <-
 
grep
(
"^MT-"
, 
rowData
(sce.pbmc)
$
Symbol)


stats <-
 
perCellQCMetrics
(sce.pbmc, 
subsets=
list
(
Mito=
is.mito))




high.mito <-
 
isOutlier
(stats
$
subsets_Mito_percent, 
type=
"higher"
)


low.adt <-
 
stats
$
`
altexps_Antibody Capture_detected
`
 
<
 
nrow
(
altExp
(sce.pbmc))
/
2




discard <-
 
high.mito 
|
 
low.adt


sce.pbmc <-
 
sce.pbmc[,
!
discard]
