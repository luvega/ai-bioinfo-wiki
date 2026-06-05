df
 
<-
 
res
$
gene_results


gs
 
<-
 
df
$
gene_id
[
rank
(
df
$
PValue
, ties.method
=
"min"
)
 
==
 
1
]


mu
 
<-
 
t
(
apply
(
counts
(
sub
)
[
gs
, 
]
, 
1
, 
tapply
, 
sub
$
SingleR_label
, 
mean
)
)




pheatmap
(
t
(
mu
)
, 


    scale
=
"column"
, show_colnames
=
FALSE
,


    cluster_rows
=
TRUE
, cluster_cols
=
TRUE
, 


    main
=
"Average expression of top SVGs per cell type"
)
