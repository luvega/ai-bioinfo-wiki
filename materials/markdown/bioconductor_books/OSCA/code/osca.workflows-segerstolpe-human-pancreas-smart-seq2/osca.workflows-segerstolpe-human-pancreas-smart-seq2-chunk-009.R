library
(scran)


clusters <-
 
quickCluster
(sce.seger)


sce.seger <-
 
computeSumFactors
(sce.seger, 
clusters=
clusters)


sce.seger <-
 
logNormCounts
(sce.seger)
