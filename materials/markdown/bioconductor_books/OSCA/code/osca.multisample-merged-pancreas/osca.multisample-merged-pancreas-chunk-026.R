set.seed
(
1010100
)


multiout <-
 
fastMNN
(combined, 
batch=
combined
$
donor, 


    
subset.row=
chosen.genes, 
weights=
donors.per.batch)




# Renaming metadata fields for easier communication later.


multiout
$
dataset <-
 
combined
$
batch


multiout
$
donor <-
 
multiout
$
batch


multiout
$
batch <-
 
NULL
