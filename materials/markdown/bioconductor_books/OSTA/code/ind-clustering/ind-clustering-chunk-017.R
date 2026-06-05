pcs
 
<-
 
reducedDim
(
spe
, 
"PCA_tx"
)


ids
 
<-
 
c
(
"total_counts"
, 
"cell_area"
, 
ks
)


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
 
spe
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
