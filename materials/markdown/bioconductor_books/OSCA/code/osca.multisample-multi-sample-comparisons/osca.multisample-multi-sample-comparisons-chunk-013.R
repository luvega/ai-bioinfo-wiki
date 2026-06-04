# Using 'label' and 'sample' as our two factors; each column of the output


# corresponds to one unique combination of these two factors.


summed <-
 
aggregateAcrossCells
(merged, 


    
id=
colData
(merged)[,
c
(
"celltype.mapped"
, 
"sample"
)])


summed
