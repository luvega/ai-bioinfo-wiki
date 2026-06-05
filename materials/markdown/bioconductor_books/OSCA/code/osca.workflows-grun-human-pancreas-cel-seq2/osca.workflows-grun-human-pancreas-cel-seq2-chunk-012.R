block <-
 
paste0
(sce.grun
$
sample, 
"_"
, sce.grun
$
donor)


dec.grun <-
 
modelGeneVarWithSpikes
(sce.grun, 
spikes=
"ERCC"
, 
block=
block)


top.grun <-
 
getTopHVGs
(dec.grun, 
prop=
0.1
)
