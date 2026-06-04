library
(scuttle)


stats <-
 
perCellQCMetrics
(sce.grun.hsc)


qc <-
 
quickPerCellQC
(stats, 
batch=
sce.grun.hsc
$
protocol,


    
subset=
grepl
(
"sorted"
, sce.grun.hsc
$
protocol))


sce.grun.hsc <-
 
sce.grun.hsc[,
!
qc
$
discard]
