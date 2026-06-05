set.seed
(
00010101
)


dec.paul <-
 
modelGeneVarByPoisson
(sce.paul)


top.paul <-
 
getTopHVGs
(dec.paul, 
prop=
0.1
)
