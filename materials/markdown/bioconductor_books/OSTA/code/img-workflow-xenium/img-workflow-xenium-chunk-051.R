# select top-ranked genes for every cluster


top
 
<-
 
unique
(
unlist
(
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
)
)


plotGroupedHeatmap
(
sub
, 


    features
=
top
, group
=
"Level1"
, 


    scale
=
TRUE
, center
=
TRUE
, fontsize
=
6
)
