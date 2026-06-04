plotExpression
(
logNormCounts
(summed.filt), 


    
features=
"Slc22a18"
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
