library
(scater)


set.seed
(
00101010
)


quick.sce <-
 
runTSNE
(quick.sce, 
dimred=
"corrected"
)


quick.sce
$
batch <-
 
factor
(quick.sce
$
batch)


plotTSNE
(quick.sce, 
colour_by=
"batch"
)
