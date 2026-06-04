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
)
