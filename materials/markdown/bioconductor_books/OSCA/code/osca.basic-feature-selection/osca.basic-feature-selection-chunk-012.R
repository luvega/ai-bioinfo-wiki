plot
(dec.spike
.416
b
$
mean, dec.spike
.416
b
$
total, 
xlab=
"Mean of log-expression"
,


    
ylab=
"Variance of log-expression"
)


fit.spike
.416
b <-
 
metadata
(dec.spike
.416
b)


points
(fit.spike
.416
b
$
mean, fit.spike
.416
b
$
var, 
col=
"red"
, 
pch=
16
)


curve
(fit.spike
.416
b
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
