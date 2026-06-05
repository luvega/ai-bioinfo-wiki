# select for a few markers per cluster


top
 
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
top
 
<-
 
unique
(
unlist
(
top
)
)
)
