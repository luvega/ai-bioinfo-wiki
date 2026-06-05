par
(
mfrow=
c
(
1
,
3
))


for
 (i 
in
 
seq_along
(dec
$
per.block)) {


    current <-
 
dec
$
per.block[[i]]


    
plot
(current
$
mean, current
$
total, 
xlab=
"Mean log-expression"
, 


        
ylab=
"Variance"
, 
pch=
16
, 
cex=
0.5
, 
main=
paste
(
"Batch"
, i))




    fit <-
 
metadata
(current)


    
points
(fit
$
mean, fit
$
var, 
col=
"red"
, 
pch=
16
)


    
curve
(fit
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


}
