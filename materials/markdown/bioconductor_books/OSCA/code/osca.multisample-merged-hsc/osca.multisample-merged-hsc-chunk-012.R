set.seed
(
1000010
)


merged <-
 
fastMNN
(normed.sce, 
subset.row=
hvgs, 
auto.merge=
TRUE
)
