dec.pbmc <-
 
modelGeneVar
(sce.pbmc)


chosen <-
 
getTopHVGs
(dec.pbmc, 
prop=
0.1
)


str
(chosen)
