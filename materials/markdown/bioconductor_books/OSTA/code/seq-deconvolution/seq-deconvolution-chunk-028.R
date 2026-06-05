ws
 
<-
 
ws_rctd


# derive majority vote label


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


names
(
ids
)
 
<-
 
rownames
(
ws
)


vis
$
RCTD
 
<-
 
factor
(
ids
[
colnames
(
vis
)
]
)




# derive majority vote excluding stromal cells


ws_no_stroma
 
<-
 
ws
[
, 
colnames
(
ws
)
 
!=
 
"stromal"
]


ids_no_stroma
 
<-
 
names
(
ws_no_stroma
)
[
apply
(
ws_no_stroma
, 
1
, 
which.max
)
]


names
(
ids_no_stroma
)
 
<-
 
rownames
(
ws
)


vis
$
RCTD_no_stroma
 
<-
 
factor
(
ids_no_stroma
[
colnames
(
vis
)
]
)
