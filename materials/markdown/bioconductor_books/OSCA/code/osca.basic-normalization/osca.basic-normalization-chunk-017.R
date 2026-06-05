# See below for explanation of logNormCounts().


sce.richard.deconv <-
 
logNormCounts
(sce.richard, 
size_factors=
to.plot
$
DeconvFactor)


sce.richard.spike <-
 
logNormCounts
(sce.richard, 
size_factors=
to.plot
$
SpikeFactor)




gridExtra
::
grid.arrange
(


    
plotExpression
(sce.richard.deconv, 
x=
"stimulus"
, 


        
colour_by=
"time"
, 
features=
"ENSMUSG00000092341"
) 
+
 


        
theme
(
axis.text.x =
 
element_text
(
angle =
 
90
)) 
+
 


        
ggtitle
(
"After deconvolution"
),


    
plotExpression
(sce.richard.spike, 
x=
"stimulus"
, 


        
colour_by=
"time"
, 
features=
"ENSMUSG00000092341"
) 
+
 


        
theme
(
axis.text.x =
 
element_text
(
angle =
 
90
)) 
+


        
ggtitle
(
"After spike-in normalization"
),


    
ncol=
2


)
