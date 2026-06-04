cd
 
<-
 
data.frame
(
colData
(
vis
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
anno
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
RCTD_no_stroma
, 
anno
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
anno
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
RCTD_no_stroma
, fill
=
anno
)
)
 
+
 


    
ggtitle
(
"RCTD_no_stroma"
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
