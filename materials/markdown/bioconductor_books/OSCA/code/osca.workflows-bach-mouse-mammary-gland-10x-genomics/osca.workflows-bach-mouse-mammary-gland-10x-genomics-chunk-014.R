plot
(dec.mam
$
mean, dec.mam
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
(dec.mam)


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
