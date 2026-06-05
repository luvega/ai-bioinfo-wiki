library
(batchelor)


set.seed
(
1011011
)


mnn.pancreas <-
 
quickCorrect
(
grun=
sce.grun, 
muraro=
sce.muraro, 


    
precomputed=
list
(dec.grun, dec.muraro))




corrected <-
 
mnn.pancreas
$
corrected


corrected
$
label <-
 
c
(sce.grun
$
label, sce.muraro
$
label)


plotExpression
(corrected, 
x=
"label"
, 
features=
"ENSG00000129965"
, 


    
exprs_values=
"reconstructed"
, 
other_fields=
"batch"
) 
+
 
facet_wrap
(
~
batch)
