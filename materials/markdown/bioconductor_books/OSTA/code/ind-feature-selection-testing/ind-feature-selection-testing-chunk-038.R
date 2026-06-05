# subset data for the 113 genes nnSVG is based on


sub_gene
 
<-
 
rowData
(
sub
)
$
gene_id


sub_DESpace
 
<-
 
res_DESpace
[
sub_gene
, 
]
 


sub_HVG
 
<-
 
as.data.frame
(
dec
[
sub_gene
, 
]
)




# aggregate DEGs for each spatial domain


subset_mgs
 
<-
 
lapply
(
mgs
, \
(
x
)
 
x
[
sub_gene
, 
1
:
3
]
 
|>
 
as.data.frame
(
)
)


sub_DEG
 
<-
 
do.call
(
cbind
, 
subset_mgs
)
 


top_cols
 
<-
 
sub_DEG
 
|>
 
select
(
ends_with
(
".Top"
)
)


sub_DEG
$
Top
 
<-
 
do.call
(
pmin
, 
c
(
top_cols
, na.rm 
=
 
TRUE
)
)




# compute ranks 


sub_DESpace
$
rank
 
<-
 
rank
(
sub_DESpace
$
FDR
, ties.method 
=
 
"first"
)


sub_HVG
$
rank
 
<-
 
rank
(
-
1
 
*
 
sub_HVG
$
bio
, ties.method 
=
 
"first"
)


sub_DEG
$
rank
 
<-
 
rank
(
sub_DEG
$
Top
, ties.method 
=
 
"first"
)




# combine 'rank' column for each method


res_all
 
<-
 
list
(


    nnSVG 
=
 
as.data.frame
(
res_nnSVG
)
,


    DESpace 
=
 
sub_DESpace
, HVGs 
=
 
sub_HVG
, DEGs 
=
 
sub_DEG


)


rank_all
 
<-
 
do.call
(
cbind
, 
lapply
(
res_all
, 
`[[`
, 
"rank"
)
)


rank_all
 
<-
 
data.frame
(
gene_id 
=
 
sub_gene
, 
rank_all
)
