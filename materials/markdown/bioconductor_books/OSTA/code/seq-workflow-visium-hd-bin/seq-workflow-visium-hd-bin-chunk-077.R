# derive majority vote labels


ids
 
<-
 
names
(
ws
)
[
apply
(
ws
, 
1
, 
which.max
)
]


ids
 
<-
 
gsub
(
"\\.([A-z])"
, 
" \\1"
, 
ids
)


idx
 
<-
 
match
(
colnames
(
.vhd16
)
, 
rownames
(
ws
)
)


table
(
.vhd16
$
.DeconLabel1
 
<-
 
factor
(
ids
[
idx
]
)
)
