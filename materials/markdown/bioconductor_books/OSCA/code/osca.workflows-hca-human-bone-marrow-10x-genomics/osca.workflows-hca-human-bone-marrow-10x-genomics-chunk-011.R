library
(batchelor)


library
(BiocNeighbors)




set.seed
(
1010001
)


merged.bone <-
 
fastMNN
(sce.bone, 
batch =
 sce.bone
$
Donor, 
subset.row =
 top.bone,


     
BSPARAM=
BiocSingular
::
RandomParam
(
deferred =
 
TRUE
), 


     
BNPARAM=
AnnoyParam
(),


     
BPPARAM=
bpp)




reducedDim
(sce.bone, 
'MNN'
) <-
 
reducedDim
(merged.bone, 
'corrected'
)
