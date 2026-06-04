library
(scran)


dec.pbmc <-
 
modelGeneVar
(sce.pbmc)




# Visualizing the fit:


fit.pbmc <-
 
metadata
(dec.pbmc)


plot
(fit.pbmc
$
mean, fit.pbmc
$
var, 
xlab=
"Mean of log-expression"
,


    
ylab=
"Variance of log-expression"
)


curve
(fit.pbmc
$
trend
(x), 
col=
"dodgerblue"
, 
add=
TRUE
, 
lwd=
2
)
