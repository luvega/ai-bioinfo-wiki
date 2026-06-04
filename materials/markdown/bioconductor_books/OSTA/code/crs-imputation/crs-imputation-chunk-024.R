# get top markers per cell type


top
 
<-
 
lapply
(
names
(
mgs
)
, \
(
k
)
 
{


    
df
 
<-
 
mgs
[[
k
]
]
[
, 
c
(
"FDR"
, 
"summary.AUC"
)
]


    
g
 
<-
 
head
(
rownames
(
df
)
, 
20
)


    
data.frame
(
k
, 
g
, 
df
[
g
, 
]
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


rownames
(
top
)
 
<-
 
NULL


head
(
top
)
