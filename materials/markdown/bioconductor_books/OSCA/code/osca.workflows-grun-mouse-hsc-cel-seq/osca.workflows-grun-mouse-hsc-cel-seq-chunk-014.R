set.seed
(
00010101
)


dec.grun.hsc <-
 
modelGeneVarByPoisson
(sce.grun.hsc) 


top.grun.hsc <-
 
getTopHVGs
(dec.grun.hsc, 
prop=
0.1
)
