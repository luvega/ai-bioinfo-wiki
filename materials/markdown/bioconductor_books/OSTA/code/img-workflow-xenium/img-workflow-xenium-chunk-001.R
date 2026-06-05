library
(
dplyr
)


library
(
tidyr
)


library
(
scran
)


library
(
igraph
)


library
(
scater
)


library
(
scuttle
)


library
(
SingleR
)


library
(
ggplot2
)


library
(
patchwork
)


library
(
OSTA.data
)


library
(
BayesSpace
)


library
(
BiocParallel
)


library
(
DropletUtils
)


library
(
SpatialExperiment
)


library
(
SpatialExperimentIO
)


# set parallelization


bp
 
<-
 
MulticoreParam
(
4
)


# set seed for random number generation


# in order to make results reproducible


set.seed
(
112358
)
