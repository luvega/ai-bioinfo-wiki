dec.zeisel <-
 
modelGeneVarWithSpikes
(sce.zeisel, 
"ERCC"
)


top.hvgs <-
 
getTopHVGs
(dec.zeisel, 
prop=
0.1
)
