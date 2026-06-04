# identify mitochondrial genes


is_mito
 
<-
 
grepl
(
"(^MT-)|(^mt-)"
, 
rowData
(
spe
)
$
gene_name
)


table
(
is_mito
)
