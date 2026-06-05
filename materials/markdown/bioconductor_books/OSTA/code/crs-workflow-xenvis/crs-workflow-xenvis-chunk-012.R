# get cell indices and number of cells per spot


vis
$
n_cells
 
<-
 
rowSums
(
(
idx
 
<-
 
nns
$
nn.idx
)
 
>
 
0
)


plotCoords
(
vis
, annotate
=
"n_cells"
)
