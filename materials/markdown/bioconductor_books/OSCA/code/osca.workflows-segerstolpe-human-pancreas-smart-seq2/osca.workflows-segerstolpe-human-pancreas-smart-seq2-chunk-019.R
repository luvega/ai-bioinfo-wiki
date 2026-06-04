library
(batchelor)




set.seed
(
10001010
)


corrected <-
 
fastMNN
(sce.seger, 
batch=
sce.seger
$
Donor, 
subset.row=
chosen.hvgs)




set.seed
(
10000001
)


corrected <-
 
runTSNE
(corrected, 
dimred=
"corrected"
)




colLabels
(corrected) <-
 
clusterRows
(
reducedDim
(corrected, 
"corrected"
), 
NNGraphParam
())




tab <-
 
table
(
Cluster=
colLabels
(corrected), 
Donor=
corrected
$
batch)


tab
