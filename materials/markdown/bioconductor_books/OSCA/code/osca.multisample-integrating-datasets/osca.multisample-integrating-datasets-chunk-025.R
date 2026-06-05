set.seed
(
10001
)


residuals <-
 
regressBatches
(pbmc3k, pbmc4k, 
d=
50
,


    
subset.row=
chosen.hvgs, 
correct.all=
TRUE
,


    
BSPARAM=
BiocSingular
::
RandomParam
())
