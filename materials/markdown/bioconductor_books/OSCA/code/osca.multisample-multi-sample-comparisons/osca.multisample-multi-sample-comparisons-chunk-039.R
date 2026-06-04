# Removing all pseudo-bulk samples with 'insufficient' cells.


summed.filt <-
 
summed[,summed
$
ncells 
>=
 
10
]




library
(scran)


de.results <-
 
pseudoBulkDGE
(summed.filt, 


    
label=
summed.filt
$
celltype.mapped,


    
design=
~
factor
(pool) 
+
 
tomato,


    
coef=
"tomatoTRUE"
,


    
condition=
summed.filt
$
tomato 


)
