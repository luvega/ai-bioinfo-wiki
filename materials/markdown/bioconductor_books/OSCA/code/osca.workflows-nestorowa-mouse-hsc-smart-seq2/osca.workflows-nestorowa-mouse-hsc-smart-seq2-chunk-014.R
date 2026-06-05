set.seed
(
00010101
)


dec.nest <-
 
modelGeneVarWithSpikes
(sce.nest, 
"ERCC"
)


top.nest <-
 
getTopHVGs
(dec.nest, 
prop=
0.1
)
