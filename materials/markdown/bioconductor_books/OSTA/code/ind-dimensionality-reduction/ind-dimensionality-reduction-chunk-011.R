pcs
 
<-
 
reducedDim
(
spe
, 
"PCA_tx"
)
[
, 
seq
(
3
)
]


pcs
 
<-
 
sweep
(
pcs
, 
2
, 
colMins
(
pcs
)
, 
`-`
)


pcs
 
<-
 
sweep
(
pcs
, 
2
, 
colMaxs
(
pcs
)
, 
`/`
)


rgb
 
<-
 
apply
(
pcs
, 
1
, \
(
.
)
 
rgb
(
.
[
1
]
, 
.
[
2
]
, 
.
[
3
]
)
)


df
 
<-
 
data.frame
(
colData
(
spe
)
, 
spatialCoords
(
spe
)
, 
rgb
)
