library
(
dplyr
)


library
(
Banksy
)


library
(
scater
)


library
(
ggplot2
)


library
(
OSTA.data
)


library
(
patchwork
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


# load Xenium data post quality control


spe
 
<-
 
readRDS
(
"img-spe_qc.rds"
)
