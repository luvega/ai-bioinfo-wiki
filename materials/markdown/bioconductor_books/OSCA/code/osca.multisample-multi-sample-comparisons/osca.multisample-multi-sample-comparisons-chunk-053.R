sizeFactors
(summed.filt) <-
 
NULL


plotExpression
(
logNormCounts
(summed.filt),


    
features=
"Rbp4"
,


    
x=
"tomato"
, 
colour_by=
"tomato"
,


    
other_fields=
"celltype.mapped"
) 
+


    
facet_wrap
(
~
celltype.mapped)
