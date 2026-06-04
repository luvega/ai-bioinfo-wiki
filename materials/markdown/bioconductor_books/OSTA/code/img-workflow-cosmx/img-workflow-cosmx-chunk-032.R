res
 
<-
 
localResults
(
sfe
)
[[
"localmoran"
]
]
[[
1
]
]


res
$
locClust
 
<-
 
with
(
res
, 
ifelse
(


    
`-log10p_adj`
 
>
 
-
log10
(
0.05
)
, 


    
as.character
(
mean
)
, 
"non-siginificant"
)
)


localResults
(
sfe
)
[[
"localmoran"
]
]
[[
1
]
]
 
<-
 
res




plotLocalResult
(
sfe
,


    features
=
gs
[
1
]
,


    name
=
"localmoran"
,


    attribute
=
"locClust"
,


    colGeometryName
=
"cellSeg"
)
