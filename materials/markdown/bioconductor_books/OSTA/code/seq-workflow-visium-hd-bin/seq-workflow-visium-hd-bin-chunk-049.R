fq
 
<-
 
prop.table
(
table
(
sce
$
Level1
, 
sce
$
Level2
)
, 
2
)


pheatmap
(
fq
, cellwidth
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
