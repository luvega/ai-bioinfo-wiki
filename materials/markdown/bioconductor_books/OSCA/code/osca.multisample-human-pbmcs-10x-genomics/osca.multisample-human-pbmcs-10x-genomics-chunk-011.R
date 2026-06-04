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
 (n 
in
 
names
(all.dec)) {


    curdec <-
 
all.dec[[n]]


    
plot
(curdec
$
mean, curdec
$
total, 
pch=
16
, 
cex=
0.5
, 
main=
n,


        
xlab=
"Mean of log-expression"
, 
ylab=
"Variance of log-expression"
)


    curfit <-
 
metadata
(curdec)


    
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
