# use gene symbols as feature names


mtx
 
<-
 
t
(
assay
(
pbs
)
)


colnames
(
mtx
)
 
<-
 
rowData
(
pbs
)
$
gene_name


# using pheatmap package


pheatmap
(
mat 
=
 
mtx
, scale 
=
 
"column"
)
