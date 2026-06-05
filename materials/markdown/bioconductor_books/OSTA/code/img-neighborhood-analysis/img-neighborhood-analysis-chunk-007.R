# test search


.i
 
<-
 
sample
(
which
(
i
)
, 
1e3
)


ns
 
<-
 
nn2
(


    
xy
[
j
, 
]
, 
xy
[
.i
, 
]
, 


    k
=
round
(
sum
(
j
)
/
2
)
, 


    searchtype
=
"radius"
, r
=
r
)


(
.k
 
<-
 
max
(
rowSums
(
ns
$
nn.idx
 
>
 
0
)
)
)
