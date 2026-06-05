plot
(dec.nest
$
mean, dec.nest
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
(dec.nest)


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


points
(curfit
$
mean, curfit
$
var, 
col=
"red"
)
