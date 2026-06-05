# Synchronizing the metadata for cbind()ing.


# 
TODO
: replace with combineCols when that comes out.


rowData
(pbmc3k) <-
 
rowData
(pbmc4k)


pbmc3k
$
batch <-
 "3k"


pbmc4k
$
batch <-
 "4k"


uncorrected <-
 
cbind
(pbmc3k, pbmc4k)




# Using RandomParam() as it is more efficient for file-backed matrices.


library
(scater)


set.seed
(
0010101010
)


uncorrected <-
 
runPCA
(uncorrected, 
subset_row=
chosen.hvgs,


    
BSPARAM=
BiocSingular
::
RandomParam
())
