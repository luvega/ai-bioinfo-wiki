par
(
mfrow=
c
(
1
,
2
))


blocked.stats <-
 
dec.chimera
$
per.block


for
 (i 
in
 
colnames
(blocked.stats)) {


    current <-
 
blocked.stats[[i]]


    
plot
(current
$
mean, current
$
total, 
main=
i, 
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
(current)


    
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


}
