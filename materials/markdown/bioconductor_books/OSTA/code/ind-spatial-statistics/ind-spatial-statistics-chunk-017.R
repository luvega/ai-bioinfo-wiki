resJc
 
<-
 
joincount.multi
(
as.factor
(
sfe
$
cluster
)
, 
colGraph
(
sfe
, 
"knn6"
)
)


resJc
 
<-
 
resJc
[
order
(
resJc
[
, 
"z-value"
]
, decreasing
=
TRUE
)
, 
]


head
(
resJc
, 
20
)
