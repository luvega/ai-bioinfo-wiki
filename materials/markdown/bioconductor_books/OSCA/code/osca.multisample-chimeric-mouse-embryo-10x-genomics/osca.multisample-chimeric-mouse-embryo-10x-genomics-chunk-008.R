library
(batchelor)


set.seed
(
01001001
)


merged <-
 
correctExperiments
(sce.chimera, 


    
batch=
sce.chimera
$
sample, 


    
subset.row=
chosen.hvgs,


    
PARAM=
FastMnnParam
(


        
merge.order=
list
(


            
list
(
1
,
3
,
5
), 
# WT (3 replicates)


            
list
(
2
,
4
,
6
)  
# td-Tomato (3 replicates)


        )


    )


)
