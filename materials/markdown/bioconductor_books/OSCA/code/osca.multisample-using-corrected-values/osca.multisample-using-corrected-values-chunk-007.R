library
(scater)


gridExtra
::
grid.arrange
(


    
plotExpression
(sce.grun, 
x=
"label"
, 
features=
"ENSG00000129965"
) 
+
 
ggtitle
(
"Grun"
),


    
plotExpression
(sce.muraro, 
x=
"label"
, 
features=
"ENSG00000129965"
) 
+
 
ggtitle
(
"Muraro"
)


)
