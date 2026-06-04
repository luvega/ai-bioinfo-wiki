library
(bluster)




set.seed
(
1000
)


colLabels
(sce.bone) <-
 
clusterRows
(
reducedDim
(sce.bone, 
"MNN"
),


    
TwoStepParam
(
KmeansParam
(
centers=
1000
), 
NNGraphParam
(
k=
5
)))




table
(
colLabels
(sce.bone))
