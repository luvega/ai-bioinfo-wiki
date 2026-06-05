gridExtra
::
grid.arrange
(


    
plotTSNE
(sce.mess, 
colour_by =
 
"phenotype"
) 
+
 
ggtitle
(
"By phenotype"
),


    
plotTSNE
(sce.mess, 
colour_by =
 
"experiment batch"
) 
+
 
ggtitle
(
"By batch "
),


    
plotTSNE
(sce.mess, 
colour_by =
 
"CDK1"
, 
swap_rownames=
"SYMBOL"
) 
+
 
ggtitle
(
"By CDK1"
),


    
plotTSNE
(sce.mess, 
colour_by =
 
"phase"
) 
+
 
ggtitle
(
"By phase"
),


    
ncol =
 
2


)
