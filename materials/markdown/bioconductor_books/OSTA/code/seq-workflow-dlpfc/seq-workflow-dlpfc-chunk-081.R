# add a variable for saving the manual annotations


spe
$
ManualAnnotation
 
<-
 
"NA"




# remove genes with no data


no_expr
 
<-
 
which
(
rowSums
(
counts
(
spe
)
)
 
==
 
0
)




# number of genes with no counts


length
(
no_expr
)
