library
(scran)


dec.chimera <-
 
modelGeneVar
(sce.chimera, 
block=
sce.chimera
$
sample)


chosen.hvgs <-
 
dec.chimera
$
bio 
>
 
0
