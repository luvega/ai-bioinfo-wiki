df
 
<-
 
data.frame
(
spatialCoords
(
sqe
)
, 
colData
(
sqe
)
)


round
(
100
*
with
(
df
, 
prop.table
(
table
(
k
, 
ctx
)
, 
2
)
)
, 
2
)
