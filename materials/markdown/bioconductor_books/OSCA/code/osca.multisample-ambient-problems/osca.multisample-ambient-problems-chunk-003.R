library
(scran)


summed.tal1 <-
 
aggregateAcrossCells
(sce.tal1, 


    
ids=
DataFrame
(
sample=
sce.tal1
$
sample,


        
label=
sce.tal1
$
celltype.mapped)


)


summed.tal1
$
block <-
 
summed.tal1
$
sample 
%%
 
2
 
==
 
0
 
# Add blocking factor.




# Subset to our neural crest cells.


summed.neural <-
 
summed.tal1[,summed.tal1
$
label
==
"Neural crest"
]


summed.neural
