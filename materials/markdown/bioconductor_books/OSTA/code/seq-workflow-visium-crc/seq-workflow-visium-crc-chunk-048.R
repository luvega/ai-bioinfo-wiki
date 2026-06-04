for
 
(
.
 
in
 
c
(
"Leiden"
, 
"RCTD"
)
)
 
{


    
# aggregate AUC values by cluster


    
mu
 
<-
 
aggregateAcrossCells
(
auc
[
top
, 
]
, 
spe
[[
.
]
]
, 


        use.assay.type
=
"AUC"
, statistics
=
"mean"
)


    
# visualize as (cluster x set) heatmap


    
pheatmap
(


        mat
=
t
(
assay
(
mu
)
)
, scale
=
"column"
, col
=
pals
::
coolwarm
(
)
, main
=
.
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


}
