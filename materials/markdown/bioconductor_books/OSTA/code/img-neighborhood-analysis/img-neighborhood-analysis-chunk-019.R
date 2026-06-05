library
(
pheatmap
)


cor
 
<-
 
plotColocal
(
sqe
, pm_cols
=
colnames
(
grp
)
, return_matrix
=
TRUE
)


pal
 
<-
 
colorRampPalette
(
rev
(
hcl.colors
(
9
, 
"Roma"
)
)
)
(
100
)


pheatmap
(
cor
, 


    cellwidth
=
15
, cellheight
=
15
, 


    treeheight_row
=
5
, treeheight_col
=
5
,


    col
=
pal
, breaks
=
seq
(
-
1
, 
1
, length
=
100
)
)
