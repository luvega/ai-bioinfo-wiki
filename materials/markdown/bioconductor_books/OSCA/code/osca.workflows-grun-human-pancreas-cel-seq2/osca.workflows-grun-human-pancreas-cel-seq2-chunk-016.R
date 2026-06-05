library
(batchelor)


set.seed
(
1001010
)


merged.grun <-
 
fastMNN
(sce.grun, 
subset.row=
top.grun, 
batch=
sce.grun
$
donor)
