library
(batchelor)


sce.mess <-
 
correctExperiments
(sce.mess, 


    
PARAM =
 
RegressParam
(


        
design =
 
model.matrix
(
~
sce.mess
$
phenotype 
+
 
sce.mess
$
`
experiment batch
`
),


        
keep =
 
1
:
2
 


    )


)
