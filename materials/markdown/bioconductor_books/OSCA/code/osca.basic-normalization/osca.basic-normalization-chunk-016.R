to.plot <-
 
data.frame
(


    
DeconvFactor=
calculateSumFactors
(sce.richard),


    
SpikeFactor=
sizeFactors
(sce.richard),


    
Stimulus=
sce.richard
$
stimulus, 


    
Time=
sce.richard
$
time


)




ggplot
(to.plot, 
aes
(
x=
DeconvFactor, 
y=
SpikeFactor, 
color=
Time)) 
+


    
geom_point
() 
+
 
facet_wrap
(
~
Stimulus) 
+
 
scale_x_log10
() 
+
 


    
scale_y_log10
() 
+
 
geom_abline
(
intercept=
0
, 
slope=
1
, 
color=
"red"
)
