.obj
 
<-
 
obj
[
, 
obj
$
sample_id
 
==
 
"Chromium"
]


plotUMAP
(
obj
, colour_by
=
"sample_id"
, point_size
=
0
, dimred
=
".UMAP"
)
 
+
 
ggtitle
(
"uncorrected"
)
 
+


plotUMAP
(
obj
, colour_by
=
"sample_id"
, point_size
=
0
)
 
+
 
ggtitle
(
"corrected"
)
 
+


plotUMAP
(
.obj
, colour_by
=
"Annotation"
, point_size
=
0
)
 
+
 
ggtitle
(
"Chromium"
)
 
+


plot_layout
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
"pt"
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
