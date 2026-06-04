library
(pheatmap)




# For the first batch:


heat3k <-
 
pheatmap
(tab3k
$
proportions, 
cluster_row=
FALSE
, 
cluster_col=
FALSE
,


                   
main=
"PBMC 3K comparison"
, 
silent=
TRUE
)




# For the second batch:


tab4k <-
 
nestedClusters
(
ref=
paste
(
"before"
, 
colLabels
(pbmc4k)),


                        
alt=
paste
(
"after"
, clusters.mnn[mnn.out
$
batch
==
2
]))


heat4k <-
 
pheatmap
(tab4k
$
proportions, 
cluster_row=
FALSE
, 
cluster_col=
FALSE
,


                   
main=
"PBMC 4K comparison"
, 
silent=
TRUE
)




gridExtra
::
grid.arrange
(heat3k[[
4
]], heat4k[[
4
]])
