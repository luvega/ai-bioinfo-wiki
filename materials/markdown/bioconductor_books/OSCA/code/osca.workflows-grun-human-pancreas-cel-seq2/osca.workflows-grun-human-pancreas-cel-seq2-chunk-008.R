library
(scran)


set.seed
(
1000
) 
# for irlba. 


clusters <-
 
quickCluster
(sce.grun)


sce.grun <-
 
computeSumFactors
(sce.grun, 
clusters=
clusters)


sce.grun <-
 
logNormCounts
(sce.grun)
