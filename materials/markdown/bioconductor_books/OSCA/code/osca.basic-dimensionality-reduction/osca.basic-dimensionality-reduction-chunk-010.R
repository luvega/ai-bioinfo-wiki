percent.var <-
 
attr
(
reducedDim
(sce.zeisel), 
"percentVar"
)


plot
(percent.var, 
log=
"y"
, 
xlab=
"PC"
, 
ylab=
"Variance explained (%)"
)
