# visualize averages z-scaled across clusters


pheatmap
(


    mat
=
t
(
assay
(
pbs
)
)
, scale
=
"column"
, breaks
=
seq
(
-
2
, 
2
, length
=
101
)
, 


    cellwidth
=
10
, cellheight
=
10
, treeheight_row
=
5
, treeheight_col
=
5
)
