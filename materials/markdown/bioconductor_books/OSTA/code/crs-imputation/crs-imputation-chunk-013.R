# filtering to keep cells with at


# least 10% of features detected


det
 
<-
 
colMeans
(
logcounts
(
obj
)
 
>
 
0
)


obj
 
<-
 
obj
[
, 
det
 
>=
 
0.1
]


# principal component analysis


# (w/o additional feature selection)


obj
 
<-
 
runPCA
(
obj
, name
=
".PCA"
)


# 'harmony' integration


# (keeping uncorrected PCs)


# note harmony requires max 2 cores


ncores
 
<-
 
2


pcs
 
<-
 
RunHarmony
(


    
reducedDim
(
obj
, 
".PCA"
)
,


    meta_data
=
obj
$
sample_id
,


    ncores
=
ncores
, verbose
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


# dimensionality reduction before/after 


# integration (for visualization only)


obj
 
<-
 
runUMAP
(
obj
, dimred
=
".PCA"
, name
=
".UMAP"
, BPPARAM
=
bp
)


obj
 
<-
 
runUMAP
(
obj
, dimred
=
"PCA"
, name
=
"UMAP"
, BPPARAM
=
bp
)
