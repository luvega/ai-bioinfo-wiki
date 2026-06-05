# principal component analysis


# (w/o additional feature selection)


obj
 
<-
 
runPCA
(
obj
)


# 'harmony' integration


pcs
 
<-
 
RunHarmony
(


    data_mat
=
reducedDim
(
obj
, 
"PCA"
)
, 


    meta_data
=
obj
$
sample_id
, 


    verbose
=
FALSE
)


reducedDim
(
obj
, 
"PCA"
)
 
<-
 
pcs


# dimensionality reduction


map
 
<-
 
calculateUMAP
(
t
(
pcs
)
)


reducedDim
(
obj
, 
"UMAP"
)
 
<-
 
map
