mito <-
 
which
(
rowData
(sce
.416
b)
$
SEQNAME
==
"MT"
)


stats <-
 
perCellQCMetrics
(sce
.416
b, 
subsets=
list
(
Mt=
mito))


qc <-
 
quickPerCellQC
(stats, 
percent_subsets=
c
(
"subsets_Mt_percent"
,


    
"altexps_ERCC_percent"
), 
batch=
sce
.416
b
$
block)


sce
.416
b <-
 
sce
.416
b[,
!
qc
$
discard]
