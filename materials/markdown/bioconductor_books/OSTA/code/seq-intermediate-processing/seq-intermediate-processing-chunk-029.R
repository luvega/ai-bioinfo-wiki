# using plotting functions from ggspavis package


# and formatting using patchwork package


plotCoords
(
spe
, annotate 
=
 
"ground_truth"
)
 
+
 


plotCoords
(
spe
, annotate 
=
 
"BayesSpace"
)
 
+
 


  
plot_layout
(
)
 
&
 


  
theme
(
legend.key.size 
=
 
unit
(
0
, 
"lines"
)
)
 
&
 


  
scale_color_manual
(
values 
=
 
unname
(
pals
::
trubetskoy
(
)
)
)
