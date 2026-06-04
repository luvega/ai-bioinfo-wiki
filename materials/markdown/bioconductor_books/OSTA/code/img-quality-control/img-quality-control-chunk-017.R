.p
 
<-
 \
(
df
, 
xs
)
 
{


    
fd
 
<-
 
pivot_longer
(
df
, 
all_of
(
xs
)
)


    
mu
 
<-
 
summarise_at
(
group_by
(
fd
, 
name
)
, 
"value"
, 
median
)


    
ggplot
(
fd
, 
aes
(
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
 


        
geom_histogram
(
bins
=
50
, linewidth
=
0.1
, fill
=
"gray"
)
 
+
 


        
geom_vline
(
data
=
mu
, 
aes
(
xintercept
=
value
)
, col
=
"blue"
)
 
+
 


        
geom_text
(


            hjust
=
-
0.1
, size
=
3
, col
=
"blue"
, 


            data
=
mu
, 
aes
(
value
, 
0
, label
=
round
(
value
)
)
)
 
+
 


        
scale_x_continuous
(
NULL
, trans
=
"log10"
)
 
+
 
ylab
(
"# cells"
)
 
+
 


        
theme_minimal
(
)
 
+
 
theme
(
panel.grid.minor
=
element_blank
(
)
)


}


df_cos
 
<-
 
data.frame
(
colData
(
cos
)
, 
spatialCoords
(
cos
)
)


df_xen
 
<-
 
data.frame
(
colData
(
xen
)
, 
spatialCoords
(
xen
)
)


p2
 
<-
 
.p
(
df_cos
, 
c
(
"Area_um"
, 
"total"
)
)


p1
 
<-
 
.p
(
df_xen
, 
c
(
"cell_area"
, 
"total_counts"
)
)


p1
 
+
 
ggtitle
(
"CosMx"
)
 
|
 
p2
 
+
 
ggtitle
(
"Xenium"
)
