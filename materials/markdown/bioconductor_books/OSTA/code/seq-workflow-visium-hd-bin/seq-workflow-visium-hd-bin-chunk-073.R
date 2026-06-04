# counts rejected observations


ws
 
<-
 
assay
(
res
, 
"weights"
)


table
(
colSums
(
ws
)
 
==
 
0
)
