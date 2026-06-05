library
(scran)


top.zeisel <-
 
getTopHVGs
(dec.zeisel, 
n=
2000
)




set.seed
(
100
) 
# See below.


sce.zeisel <-
 
fixedPCA
(sce.zeisel, 
subset.row=
top.zeisel) 


reducedDimNames
(sce.zeisel)
