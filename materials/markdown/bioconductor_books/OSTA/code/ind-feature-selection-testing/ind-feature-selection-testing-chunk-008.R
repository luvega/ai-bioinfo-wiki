# visualize mean-variance relationship


par
(
mar 
=
 
c
(
4
, 
4
, 
0
, 
0
)
)


fit
 
<-
 
metadata
(
dec
)


plot
(
fit
$
mean
, 
fit
$
var
, cex 
=
 
0.5
, xlab 
=
 
"mean expression"
, ylab 
=
 
"variance"
)


points
(
dec
[
hvg
, 
"mean"
]
, 
dec
[
hvg
, 
"total"
]
, cex 
=
 
0.5
, col 
=
 
"dodgerblue"
)


curve
(
fit
$
trend
(
x
)
, add 
=
 
TRUE
, lwd 
=
 
2
, col 
=
 
"tomato"
)
