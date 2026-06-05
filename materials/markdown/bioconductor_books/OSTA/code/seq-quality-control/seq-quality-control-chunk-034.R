# load DLPFC artifact samples from SpotSweeper package


data
(
DLPFC_artifact
)


spe.hangnail
 
<-
 
DLPFC_artifact




# identify mitochondrial genes


is_mito
 
<-
 
grepl
(
"(^MT-)|(^mt-)"
, 
rowData
(
spe.hangnail
)
$
gene_name
)


table
(
is_mito
)


rowData
(
spe.hangnail
)
$
gene_name
[
is_mito
]




# calculate per-spot QC metrics and store in colData


spe.hangnail
 
<-
 
addPerCellQC
(
spe.hangnail
, subsets
=
list
(
mito 
=
 
is_mito
)
)
