lapply
(
names
(
ol
)
, \
(
.
)
 


    
plotCoords
(
spe
, annotate
=
.
)
 
+
 
ggtitle
(
.
)
)
 
|>


    
wrap_plots
(
nrow
=
1
, guides
=
"collect"
)
 
&


    
guides
(
col
=
guide_legend
(
override.aes
=
list
(
size
=
3
)
)
)
 
&


    
scale_color_manual
(
"discard"
, values
=
c
(
"lavender"
, 
"purple"
)
)
 
&


    
theme
(
plot.title
=
element_text
(
hjust
=
0.5
)
, legend.key.size
=
unit
(
0
, 
"lines"
)
)
