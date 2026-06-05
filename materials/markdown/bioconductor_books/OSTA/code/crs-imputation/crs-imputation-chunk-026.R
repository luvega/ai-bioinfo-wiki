# find k-nearest neighbors across embeddings


# (from Xenium to Chromium cells)


idx
 
<-
 
split
(
colnames
(
obj
)
, 
obj
$
sample_id
)


pcs
 
<-
 
reducedDim
(
obj
, 
"PCA"
)


ref
 
<-
 
pcs
[
idx
$
Chromium
, 
]


que
 
<-
 
pcs
[
idx
$
Xenium
, 
]


knn
 
<-
 
nn2
(
data
=
ref
, query
=
que
, k
=
k
 
<-
 
20
)


# create adjacency matrix


el
 
<-
 
cbind
(


    
rep
(
idx
$
Xenium
, each
=
k
)
, 


    
idx
$
Chromium
[
c
(
t
(
knn
$
nn.idx
)
)
]
)


g
 
<-
 
graph_from_edgelist
(
el
, directed
=
TRUE
)


A
 
<-
 
as_adjacency_matrix
(
g
)


# average Chromium across Xenium neighbors


gs
 
<-
 
unique
(
top
$
g
)


cs
 
<-
 
intersect
(
rownames
(
A
)
, 
idx
$
Chromium
)


ws
 
<-
 
A
[
idx
$
Xenium
, 
cs
]
*
(
1
/
k
)


y
 
<-
 
logcounts
(
sce
)
[
gs
, 
cs
]
 
%*%
 
t
(
ws
)
