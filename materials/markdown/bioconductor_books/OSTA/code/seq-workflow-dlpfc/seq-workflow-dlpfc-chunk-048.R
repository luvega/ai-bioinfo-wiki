spe
 
<-
 
runUMAP
(
spe
, dimred
=
"PCA"
)


colnames
(
reducedDim
(
spe
, 
"UMAP"
)
)
 
<-
 
paste0
(
"UMAP"
, 
1
:
2
)




# embeddings are matrices with


# rows = cells, columns = dims.


sapply
(
reducedDims
(
spe
)
, 
dim
)
