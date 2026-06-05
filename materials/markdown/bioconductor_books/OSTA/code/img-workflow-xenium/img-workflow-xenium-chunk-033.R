# restrict to Xenium targets


sce
 
<-
 
sce
[
rowData
(
sce
)
$
ID
 
%in%
 
rowData
(
sub
)
$
ID
, 
]


# set gene symbols as feature names


rownames
(
sce
)
 
<-
 
rowData
(
sce
)
$
Symbol


# perform label transfer at the single cell-level,


# using pseudo-bulk Chromium profiles as reference


res
 
<-
 
SingleR
(


    test
=
sub
, ref
=
sce
, 


    labels
=
sce
$
Level2
, 


    aggr.ref
=
TRUE
, BPPARAM
=
bp
)
