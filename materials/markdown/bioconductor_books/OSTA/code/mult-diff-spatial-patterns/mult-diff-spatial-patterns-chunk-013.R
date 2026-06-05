# top DSP gene for cluster 2


top_dsp
 
<-
 
dsp_clu2
$
gene_id
[
1
]




# get gene symbols from Ensembl identifiers


idx
 
<-
 
match
(
top_dsp
, 
rowData
(
spe
)
$
gene_name
)


(
.gs
 
<-
 
rowData
(
spe
)
$
gene_id
[
idx
]
)
