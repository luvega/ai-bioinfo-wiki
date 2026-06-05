#--- data-loading ---#


library
(scRNAseq)


sce.grun.hsc <-
 
GrunHSCData
(
ensembl=
TRUE
)




#--- gene-annotation ---#


library
(AnnotationHub)


ens.mm.v97 <-
 
AnnotationHub
()[[
"AH73905"
]]


anno <-
 
select
(ens.mm.v97, 
keys=
rownames
(sce.grun.hsc), 


    
keytype=
"GENEID"
, 
columns=
c
(
"SYMBOL"
, 
"SEQNAME"
))


rowData
(sce.grun.hsc) <-
 
anno[
match
(
rownames
(sce.grun.hsc), anno
$
GENEID),]




#--- quality-control ---#


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
