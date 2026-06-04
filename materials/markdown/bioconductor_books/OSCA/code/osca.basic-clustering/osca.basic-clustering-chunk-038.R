hclust
.416
b <-
 
clusterCells
(sce
.416
b, 
use.dimred=
"PCA"
,


    
BLUSPARAM=
HclustParam
(
method=
"ward.D2"
), 
full=
TRUE
)


tree
.416
b <-
 
hclust
.416
b
$
objects
$
hclust




# Making a prettier dendrogram.


library
(dendextend)


tree
.416
b
$
labels <-
 
seq_along
(tree
.416
b
$
labels)


dend <-
 
as.dendrogram
(tree
.416
b, 
hang=
0.1
)




combined.fac <-
 
paste0
(sce
.416
b
$
block, 
"."
, 


    
sub
(
" .*"
, 
""
, sce
.416
b
$
phenotype))


labels_colors
(dend) <-
 
c
(


    
"20160113.wild"
=
"blue"
,


    
"20160113.induced"
=
"red"
,


    
"20160325.wild"
=
"dodgerblue"
,


    
"20160325.induced"
=
"salmon"


)[combined.fac][
order.dendrogram
(dend)]




plot
(dend)
