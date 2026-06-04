library
(scater)


set.seed
(
0010101010
)


mnn.out <-
 
runTSNE
(mnn.out, 
dimred=
"corrected"
)




mnn.out
$
batch <-
 
factor
(mnn.out
$
batch)


plotTSNE
(mnn.out, 
colour_by=
"batch"
)
