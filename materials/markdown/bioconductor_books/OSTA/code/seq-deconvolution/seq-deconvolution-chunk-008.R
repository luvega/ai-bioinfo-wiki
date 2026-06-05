vis
$
log_sum
 
<-
 
log1p
(
vis
$
sum
)


plotCoords
(
vis
, 


    annotate
=
"log_sum"
)
 
+
 


    
ggtitle
(
"log library size"
)
 
+
 


plotCoords
(
vis
, 


    annotate
=
"subsets_mt_percent"
)
 
+
 


    
ggtitle
(
"% mitochondrial"
)
 
+
 


ggplot
(


    
data.frame
(
colData
(
vis
)
)
, 


    
aes
(
x
=
sum
, y
=
subsets_mt_percent
)
)
 
+
 


    
geom_point
(
)
 
+
 
geom_density_2d
(
)
 
+


    
scale_x_log10
(
)
 
+
 
scale_y_sqrt
(
)
 
+


    
theme
(
aspect.ratio
=
2
/
3
)
 
+


plot_layout
(
nrow
=
1
)
 
&
 
theme
(


    legend.key.width
=
unit
(
0.5
, 
"lines"
)
, 


    legend.key.height
=
unit
(
1
, 
"lines"
)
)
 
&
 


    
scale_color_gradientn
(
colors
=
pals
::
jet
(
)
)
