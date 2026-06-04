block <-
 
paste0
(sce.muraro
$
plate, 
"_"
, sce.muraro
$
donor)


dec.muraro <-
 
modelGeneVarWithSpikes
(sce.muraro, 
"ERCC"
, 
block=
block)


top.muraro <-
 
getTopHVGs
(dec.muraro, 
prop=
0.1
)
