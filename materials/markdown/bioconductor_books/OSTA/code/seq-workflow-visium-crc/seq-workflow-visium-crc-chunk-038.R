cd
 
<-
 
data.frame
(
colData
(
spe
)
)


df
 
<-
 
as.data.frame
(
with
(
cd
, 
table
(
RCTD
, 
Leiden
)
)
)


fd
 
<-
 
as.data.frame
(
with
(
cd
, 
table
(
Domain
, 
Leiden
)
)
)


ggplot
(
df
, 
aes
(
Freq
, 
RCTD
, fill
=
Leiden
)
)
 
+
 
ggtitle
(
"RCTD"
)
 
+


ggplot
(
fd
, 
aes
(
Freq
, 
Domain
, fill
=
Leiden
)
)
 
+
 
ggtitle
(
"Domain"
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


    
labs
(
x
=
"Proportion"
, y
=
NULL
)
 
&


    
coord_cartesian
(
expand
=
FALSE
)
 
&


    
geom_col
(
width
=
1
, col
=
"white"
, position
=
"fill"
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
trubetskoy
(
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
aspect.ratio
=
1
,


        legend.key.size
=
unit
(
2
/
3
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
