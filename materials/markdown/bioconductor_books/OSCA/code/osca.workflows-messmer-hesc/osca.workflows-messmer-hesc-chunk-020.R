gridExtra
::
grid.arrange
(


    
plotReducedDim
(target, 
"cPCA+TSNE"
, 
colour_by =
 
"phase"
) 
+
 
ggtitle
(
"After cPCA"
),


    
plotReducedDim
(target, 
"scPCA+TSNE"
, 
colour_by =
 
"phase"
) 
+
 
ggtitle
(
"After scPCA"
),


    
ncol=
2


)
