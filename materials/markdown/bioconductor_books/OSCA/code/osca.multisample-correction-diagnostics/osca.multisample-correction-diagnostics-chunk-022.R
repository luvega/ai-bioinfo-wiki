# For the first batch.


tab <-
 
pairwiseRand
(
colLabels
(pbmc3k), clusters.mnn[mnn.out
$
batch
==
1
])


heat3k <-
 
pheatmap
(tab, 
cluster_row=
FALSE
, 
cluster_col=
FALSE
,


    
col=
rev
(viridis
::
magma
(
100
)), 
main=
"PBMC 3K probabilities"
, 
silent=
TRUE
)




# For the second batch.


tab <-
 
pairwiseRand
(
colLabels
(pbmc4k), clusters.mnn[mnn.out
$
batch
==
2
])


heat4k <-
 
pheatmap
(tab, 
cluster_row=
FALSE
, 
cluster_col=
FALSE
,


    
col=
rev
(viridis
::
magma
(
100
)), 
main=
"PBMC 4K probabilities"
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
