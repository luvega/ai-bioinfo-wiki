df
 
<-
 
data.frame
(
colData
(
spe
)
, 
spatialCoords
(
spe
)
)


p1
 
<-
 
ggplot
(
df
, 
aes
(
y
=
library_size
)
)
 
+
 
ggtitle
(
"Library size factors"
)
 


p2
 
<-
 
ggplot
(
df
, 
aes
(
y
=
sizeFactor
)
)
 
+
 
ggtitle
(
"Area-derived factors"
)
 


(
p1
 
+
 
p2
)
 
&


    
geom_boxplot
(
aes
(
Label
, fill
=
Label
)
)
 
&


    
labs
(
x
=
"Cell type"
, y
=
"Size factor"
)
 
&


    
scale_fill_manual
(
values
=
unname
(
pals
::
tableau20
(
)
)
)
 
&


    
theme_bw
(
)
 
&
 
theme
(


        aspect.ratio
=
1
,


        legend.position
=
"none"
,


        panel.grid.minor
=
element_blank
(
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
,


        axis.text.x
=
element_text
(
angle
=
45
, hjust
=
1
)
)
