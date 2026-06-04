# scale weights such that they sum to 1


ws
 
<-
 
assay
(
res
)


ws
 
<-
 
sweep
(
ws
, 
2
, 
colSums
(
ws
)
, 
`/`
)




ws_rctd
 
<-
 
data.frame
(
t
(
as.matrix
(
ws
)
)
)


round
(
ws_rctd
[
1
:
5
, 
1
:
5
]
, 
2
)
