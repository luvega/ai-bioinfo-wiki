library
(scran)


all.dec <-
 
lapply
(all.sce, modelGeneVar)


all.hvgs <-
 
lapply
(all.dec, getTopHVGs, 
prop=
0.1
)
