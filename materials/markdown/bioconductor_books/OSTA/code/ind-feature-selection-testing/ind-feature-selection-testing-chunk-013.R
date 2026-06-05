# select for a few markers per cluster


deg
 
<-
 
lapply
(
mgs
, \
(
df
)
 
rownames
(
df
)
[
df
$
Top
 
<=
 
3
]
)


length
(
deg
 
<-
 
unique
(
unlist
(
deg
)
)
)
