# Performing PCA only on the chosen HVGs.


library
(scater)


sce.pbmc <-
 
runPCA
(sce.pbmc, 
subset_row=
chosen)


reducedDimNames
(sce.pbmc)
