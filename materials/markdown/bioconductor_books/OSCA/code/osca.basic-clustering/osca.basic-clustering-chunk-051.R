# Repeating modelling and PCA on the subset.


memory <-
 
6L


sce.memory <-
 
sce.pbmc[,clust.full
==
memory]


dec.memory <-
 
modelGeneVar
(sce.memory)


sce.memory <-
 
denoisePCA
(sce.memory, 
technical=
dec.memory,


    
subset.row=
getTopHVGs
(dec.memory, 
n=
5000
))
