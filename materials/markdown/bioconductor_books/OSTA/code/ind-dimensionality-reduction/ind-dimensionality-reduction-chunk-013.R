.plot_umap
 
<-
 \
(
dr
)
 
plotReducedDim
(


    object
=
spe
, dimred
=
dr
, colour_by
=
"Label"
, 


    point_shape
=
16
, point_size
=
0
)
 
+
 
ggtitle
(
dr
)


.plot_umap
(
"UMAP_tx"
)
 
+


.plot_umap
(
"UMAP_sp"
)
 
+


    
plot_layout
(
guides
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
alpha
=
1
, size
=
2
)
)
)
 
&


    
theme_void
(
)
 
&
 
theme
(
aspect.ratio
=
1
, 


        legend.key.size
=
unit
(
0
, 
"lines"
)
,


        plot.title
=
element_text
(
hjust
=
0.5
)
)
