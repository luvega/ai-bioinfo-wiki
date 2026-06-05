idx
 
<-
 
rownames
(
ws
)


ids
 
<-
 
colnames
(
ws
)


pcs
 
<-
 
reducedDim
(
vis
, 
"PCA"
)


pcs
 
<-
 
pcs
[
idx
, 
seq_len
(
10
)
]


pcr
 
<-
 
lapply
(
ids
, \
(
id
)
 
{


    
fit
 
<-
 
summary
(
lm
(
pcs
 
~
 
ws
[[
id
]
]
)
)


    
r2
 
<-
 
sapply
(
fit
, \
(
.
)
 
.
$
adj.r.squared
)


    
data.frame
(
id
, pc
=
seq_along
(
r2
)
, 
r2
)


}
)
 
|>
 
do.call
(
what
=
rbind
)
