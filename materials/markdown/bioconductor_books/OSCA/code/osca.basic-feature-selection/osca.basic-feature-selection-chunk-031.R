# No need for explicit subset_row= specification in downstream operations.


sce.pbmc.hvg <-
 
runPCA
(sce.pbmc.hvg)




# Recover original data:


sce.pbmc.original <-
 
altExp
(sce.pbmc.hvg, 
"original"
, 
withColData=
TRUE
)
