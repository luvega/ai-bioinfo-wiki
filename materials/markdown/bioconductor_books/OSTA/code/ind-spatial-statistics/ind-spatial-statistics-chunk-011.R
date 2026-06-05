# select the 20 highest values in the res matrix


val
 
<-
 
tail
(
sort
(
res
)
, 
20
)
[
1
]


genePairs
 
<-
 
which
(
res
 
>=
 
val
, arr.ind
=
TRUE
)


# keep only pairs containing different genes


genePairs
 
<-
 
genePairs
[
genePairs
[
,
1
]
 
!=
 
genePairs
[
,
2
]
, 
]


data.frame
(


    val
=
res
[
genePairs
]
,


    i
=
rownames
(
res
)
[
genePairs
[
,
1
]
]
, 


    j
=
colnames
(
res
)
[
genePairs
[
,
2
]
]
)
