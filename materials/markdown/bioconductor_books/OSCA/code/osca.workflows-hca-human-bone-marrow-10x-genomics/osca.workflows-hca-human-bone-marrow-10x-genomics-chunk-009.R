library
(scran)


set.seed
(
1010010101
)


dec.bone <-
 
modelGeneVarByPoisson
(sce.bone, 


    
block=
sce.bone
$
Donor, 
BPPARAM=
bpp)


top.bone <-
 
getTopHVGs
(dec.bone, 
n=
5000
)
