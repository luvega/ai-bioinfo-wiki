proposed <-
 
c
(
rep
(
NA
, 
ncol
(sce.grun)), 


    sce.muraro
$
label,


    sce.lawlor
$
`
cell type
`
,


    sce.seger
$
CellType)




proposed <-
 
tolower
(proposed)


proposed[proposed
==
"gamma/pp"
] <-
 "gamma"


proposed[proposed
==
"pp"
] <-
 "gamma"


proposed[proposed
==
"duct"
] <-
 "ductal"


proposed[proposed
==
"psc"
] <-
 "stellate"


table
(proposed, clusters)
