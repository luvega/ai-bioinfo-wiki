lab
 
<-
 
grep
(
"Label"
, 
names
(
cd
 
<-
 
colData
(
vhd8
)
)
, value
=
TRUE
)


pal
 
<-
 
hcl.colors
(
length
(
unique
(
unlist
(
cd
[
lab
]
)
)
)
, 
"Spectral"
)


lapply
(
lab
, \
(
.
)
 
{


  
plotCoords
(
vhd8
, annotate
=
.
, point_size
=
0.2
, point_shape
=
15
)
 
+
 
ggtitle
(
.
)


}
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
NULL
, values
=
pal
)
 
&


  
theme
(
legend.key.size
=
unit
(
0
, 
"lines"
)
)
