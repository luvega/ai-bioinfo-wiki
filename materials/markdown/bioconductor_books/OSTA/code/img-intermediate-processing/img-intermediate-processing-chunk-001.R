library
(
scran
)


library
(
scater
)


library
(
igraph
)


library
(
Banksy
)


library
(
ggplot2
)


library
(
ggspavis
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
SpatialExperiment
)


# set seed for random number generation


# in order to make results reproducible


set.seed
(
20000229
)


# load data from preceding 


# chapter (post quality control)


(
spe
 
<-
 
readRDS
(
"img-spe_qc.rds"
)
)
