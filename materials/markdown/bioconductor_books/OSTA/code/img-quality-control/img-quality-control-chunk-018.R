lapply
(
c
(
"cell_area"
, 
"total_counts"
)
, \
(
.
)
 
{


    
# crop very low/high values for clearer visualization


    
val
 
<-
 
xen
[[
.
]
]


    
qs
 
<-
 
quantile
(
val
, 
c
(
0.01
, 
0.99
)
)


    
val
 
<-
 
ifelse
(
val
 
<
 
qs
[
1
]
, 
qs
[
1
]
, 
ifelse
(
val
 
>
 
qs
[
2
]
, 
qs
[
2
]
, 
val
)
)


    
xen
[[
.
]
]
 
<-
 
val


    
plotCoords
(
xen
, annotate
=
.
, point_size
=
0
, y_reverse 
=
 
FALSE
)
 
+


        
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
)
 
+


        
scale_color_gradientn
(
colors
=
unname
(
pals
::
jet
(
)
)
, trans
=
"log10"
)


}
)
 
|>
 
wrap_plots
(
nrow
=
1
)
