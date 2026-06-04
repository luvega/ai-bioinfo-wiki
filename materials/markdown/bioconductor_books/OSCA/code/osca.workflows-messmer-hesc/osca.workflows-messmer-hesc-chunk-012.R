dec <-
 
modelGeneVarWithSpikes
(sce.mess, 
"ERCC"
, 
block =
 sce.mess
$
`
experiment batch
`
)


top.hvgs <-
 
getTopHVGs
(dec, 
prop =
 
0.1
)
