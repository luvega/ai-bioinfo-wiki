df
 
<-
 
data.frame
(


    n_cells
=
xem
$
ncells
,


    Xenium
=
xem
$
subsets_gs_sum
,


    Visium
=
vis
[
, 
colnames
(
xem
)
]
$
subsets_gs_sum
)


ggplot
(
df
, 
aes
(
Xenium
, 
Visium
, col
=
n_cells
)
)
 
+
 


    
scale_color_gradientn
(
colors
=
rev
(
hcl.colors
(
9
, 
"Mako"
)
)
)
 
+


    
geom_point
(
alpha
=
0.5
)
 
+
 
theme_bw
(
)
 
+
 
theme
(
aspect.ratio
=
1
)
