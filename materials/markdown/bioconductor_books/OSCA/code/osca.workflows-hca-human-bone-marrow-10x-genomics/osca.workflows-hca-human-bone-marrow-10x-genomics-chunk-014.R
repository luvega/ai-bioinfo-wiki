set.seed
(
01010100
)


sce.bone <-
 
runUMAP
(sce.bone, 
dimred=
"MNN"
,


    
external_neighbors=
TRUE
, 


    
BNPARAM=
AnnoyParam
(),


    
BPPARAM=
bpp,


    
n_threads=
bpnworkers
(bpp))
