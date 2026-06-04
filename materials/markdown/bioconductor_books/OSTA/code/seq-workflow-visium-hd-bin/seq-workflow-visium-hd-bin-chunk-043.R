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
 
2
]
)


top
 
<-
 
unique
(
unlist
(
top
)
)


# average expression by clusters


pbs
 
<-
 
aggregateAcrossCells
(
.vhd16
, 


    ids
=
.vhd16
$
Banksy
, subset.row
=
top
, 


    use.assay.type
=
"logcounts"
, statistics
=
"mean"
)
