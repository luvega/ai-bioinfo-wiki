library
(
RANN
)


k
 
<-
 
10
 
# num. neighbors


r
 
<-
 
50
 
# dist. threshold


i
 
<-
 
spe
$
k
 
==
 
1
 
# source


j
 
<-
 
spe
$
k
 
==
 
4
 
# target


xy
 
<-
 
spatialCoords
(
spe
)


# k-NN search: all cells have k neighbors


ns_k
 
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
i
, 
]
, k
=
k
)


is_k
 
<-
 
ns_k
$
nn.idx


all
(
rowSums
(
is_k
 
>
 
0
)
 
==
 
k
)
 


# w/ fixed-radius: cells have 0-k neighbors


ns_r
 
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
i
, 
]
, k
=
k
, searchtype
=
"radius"
, r
=
r
)


is_r
 
<-
 
ns_r
$
nn.idx


range
(
rowSums
(
is_r
 
>
 
0
)
)
