library
(scater)


stats <-
 
high.mito <-
 
list
()


for
 (n 
in
 
names
(all.sce)) {


    current <-
 
all.sce[[n]]


    is.mito <-
 
grep
(
"MT"
, 
rowData
(current)
$
Symbol_TENx)


    stats[[n]] <-
 
perCellQCMetrics
(current, 
subsets=
list
(
Mito=
is.mito))


    high.mito[[n]] <-
 
isOutlier
(stats[[n]]
$
subsets_Mito_percent, 
type=
"higher"
)


    all.sce[[n]] <-
 
current[,
!
high.mito[[n]]]


}
