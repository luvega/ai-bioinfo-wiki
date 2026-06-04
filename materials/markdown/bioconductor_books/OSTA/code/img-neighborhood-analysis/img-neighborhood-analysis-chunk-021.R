df
 
<-
 
data.frame
(
colData
(
sqe
)
, k
=
spe
$
k
, 
spatialCoords
(
spe
)
)


vs
 
<-
 
c
(
"perplexity"
, 
"entropy"
)


fd
 
<-
 
df
 
|>


    
pivot_longer
(
all_of
(
vs
)
)
 
|>


    
group_by
(
name
)
 
|>
 
mutate_at
(
"value"
, 
scale
)
 


# threshold at 2 SDs for clearer visualization


fd
$
value
[
i
]
 
<-
 
2
*
sign
(
fd
$
value
[
i
 
<-
 
abs
(
fd
$
value
)
 
>
 
2
]
)


ggplot
(
fd
, 
aes
(
x_centroid
, 
y_centroid
, col
=
value
)
)
 
+


    
facet_grid
(
~
name
)
 
+
 
geom_point
(
shape
=
16
, size
=
0
)
 
+
 


    
theme_xy
 
+
 
theme
(
legend.key.size
=
unit
(
0.5
, 
"lines"
)
)
 
+


    
scale_color_gradient2
(
"z-scaled\nvalue"
, low
=
"cyan"
, mid
=
"navy"
, high
=
"magenta"
)
