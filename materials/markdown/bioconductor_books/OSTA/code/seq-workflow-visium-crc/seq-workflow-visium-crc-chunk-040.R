lapply
(
c
(
"detected"
, 
"log_sum"
, 
"subsets_mt_percent"
)
, \
(
.
)


    
plotColData
(
spe
, x
=
.
, y
=
"Leiden"
, color_by
=
"discard"
, point_size
=
0.1
)
 
+


    
scale_x_discrete
(
limits
=
names
(
sort
(
by
(
spe
[[
.
]
]
, 
spe
$
Leiden
, 
median
)
)
)
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
3
)
)
)
 
&


    
theme_minimal
(
)
 
&
 
theme
(


        panel.grid.minor
=
element_blank
(
)
, 


        legend.key.size
=
unit
(
0
, 
"lines"
)
)
