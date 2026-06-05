set.seed
(
00010101
)


dec.mam <-
 
modelGeneVarByPoisson
(sce.mam)


top.mam <-
 
getTopHVGs
(dec.mam, 
prop=
0.1
)
