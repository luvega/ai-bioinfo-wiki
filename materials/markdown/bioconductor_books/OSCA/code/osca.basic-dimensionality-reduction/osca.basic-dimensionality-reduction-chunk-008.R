library
(BiocSingular)


set.seed
(
1000
)


sce.zeisel <-
 
fixedPCA
(sce.zeisel, 
subset.row=
top.zeisel, 


    
BSPARAM=
RandomParam
(), 
name=
"randomized"
)


reducedDimNames
(sce.zeisel)
