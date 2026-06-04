library
(BiocParallel)


bpp <-
 
MulticoreParam
(
8
)


sce.bone <-
 
unfiltered <-
 
addPerCellQC
(sce.bone, 
BPPARAM=
bpp,


    
subsets=
list
(
Mito=
which
(
rowData
(sce.bone)
$
Chr
==
"MT"
)))




qc <-
 
quickPerCellQC
(
colData
(sce.bone), 
batch=
sce.bone
$
Donor,


    
sub.fields=
"subsets_Mito_percent"
)


sce.bone <-
 
sce.bone[,
!
qc
$
discard]
