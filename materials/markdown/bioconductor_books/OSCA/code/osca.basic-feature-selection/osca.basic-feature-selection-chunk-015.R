plot
(dec.pois.pbmc
$
mean, dec.pois.pbmc
$
total, 
pch=
16
, 
xlab=
"Mean of log-expression"
,


    
ylab=
"Variance of log-expression"
)


curve
(
metadata
(dec.pois.pbmc)
$
trend
(x), 
col=
"dodgerblue"
, 
add=
TRUE
)
