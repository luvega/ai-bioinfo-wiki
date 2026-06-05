# wrangling


df
 
<-
 
data.frame
(
colData
(
sfe
)
)


df
 
<-
 
filter
(
df
, 
!
is.na
(
Level0
)
)


fd
 
<-
 
pivot_longer
(
df
, 
ends_with
(
"um2"
)
)


fd
$
name
 
<-
 
factor
(
fd
$
name
, labels
=
c
(
"nuc."
, 
"cell"
)
)


ws
 
<-
 
c
(
nlevels
(
df
$
Level0
)
, 
nlevels
(
df
$
Level1
)
)


# plotting


ggplot
(
fd
, 
aes
(
reorder
(
Level0
, 
value
)
, 
value
, col
=
name
)
)
 
+


ggplot
(
fd
, 
aes
(
reorder
(
Level1
, 
value
)
, 
value
, col
=
name
)
)
 
+
 


plot_layout
(
nrow
=
1
, widths
=
ws
, guides
=
"collect"
)
 
&


    
geom_boxplot
(
key_glyph
=
"point"
, outlier.size
=
0
)
 
&


    
labs
(
col
=
"area (um2)"
)
 
&
 


    
theme_bw
(
)
 
&
 
theme
(


        axis.title
=
element_blank
(
)
,


        legend.key.size
=
ggplot2
::
unit
(
0
, 
"pt"
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
