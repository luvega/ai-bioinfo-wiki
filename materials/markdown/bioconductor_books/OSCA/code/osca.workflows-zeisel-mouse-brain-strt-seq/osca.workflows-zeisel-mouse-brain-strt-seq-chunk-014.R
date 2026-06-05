plot
(dec.zeisel
$
mean, dec.zeisel
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
(dec.zeisel)


points
(curfit
$
mean, curfit
$
var, 
col=
"red"
, 
pch=
16
)


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
