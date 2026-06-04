set.seed
(
1001
)


dec.pbmc <-
 
modelGeneVarByPoisson
(sce.pbmc)


top.pbmc <-
 
getTopHVGs
(dec.pbmc, 
prop=
0.1
)
