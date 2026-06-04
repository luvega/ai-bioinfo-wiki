plotExpression
(combined, 
x=
I
(
factor
(clusters.mnn)), 
swap_rownames=
"Symbol"
,


    
features=
c
(
"CD3D"
, 
"CD8B"
), 
colour_by=
"batch"
) 
+
 
facet_wrap
(Feature
~
colour_by)
