# identify mitochondrial genes


nms
 
<-
 
rowData
(
spe
)
$
gene_name


is_mito
 
<-
 
grepl
(
"(^MT-)|(^mt-)"
, 
nms
)


table
(
is_mito
)
