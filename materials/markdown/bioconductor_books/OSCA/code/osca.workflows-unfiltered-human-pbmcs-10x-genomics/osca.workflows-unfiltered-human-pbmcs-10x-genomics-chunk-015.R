plot
(dec.pbmc
$
mean, dec.pbmc
$
total, 
pch=
16
, 
cex=
0.5
,


    
xlab=
"Mean of log-expression"
, 
ylab=
"Variance of log-expression"
)


curfit <-
 
metadata
(dec.pbmc)


curve
(curfit
$
trend
(x), 
col=
'dodgerblue'
, 
add=
TRUE
, 
lwd=
2
)
