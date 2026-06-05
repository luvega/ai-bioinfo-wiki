hm
 
<-
 \
(
mat
, 
string
)
 
pheatmap
(


    
mat
, show_rownames
=
TRUE
, show_colnames
=
TRUE
, main
=
string
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


hm
(
prop.table
(
table
(
vis
$
anno
, 
vis
$
RCTD
)
, 
2
)
, string
=
"RCTD"
)


hm
(
prop.table
(
table
(
vis
$
anno
, 
vis
$
RCTD_no_stroma
)
, 
2
)
, string
=
"RCTD_no_stroma"
)
