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
scater
)


library
(
scuttle
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
anndataR
)


library
(
patchwork
)


library
(
reticulate
)


library
(
BiocParallel
)


library
(
SpatialExperiment
)


# load data from previous chapter


# (past quality control & clustered)


spe
 
<-
 
readRDS
(
"img-spe_cl.rds"
)


# specify whether/how to 


# perform parallelization


bp
 
<-
 
MulticoreParam
(
4
)
