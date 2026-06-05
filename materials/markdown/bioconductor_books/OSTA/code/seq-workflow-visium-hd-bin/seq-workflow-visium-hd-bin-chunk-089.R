n_tum
 
<-
 
table
(
.vhd8
$
.DeconLabel1
)
[
"Tumor"
]


n_fib
 
<-
 
table
(
.vhd8
$
.DeconLabel1
)
[
"Fibroblast"
]


fd
$
p
 
<-
 
ifelse
(
fd
$
target
 
==
 
"Tumor"
, 
fd
$
n
/
n_tum
, 
fd
$
n
/
n_fib
)


ggplot
(
fd
, 
aes
(
x
=
CT
, y
=
n
, fill
=
target
)
)
 
+
 


    
labs
(
y
=
"# cells within 200px"
)
 
+


ggplot
(
fd
, 
aes
(
x
=
CT
, y
=
p
, fill
=
target
)
)
 
+
 


    
labs
(
y
=
"relative abundance"
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
 


    
geom_boxplot
(
key_glyph
=
"point"
)
 
&
 


    
scale_fill_manual
(
values
=
c
(
"yellow"
, 
"pink"
)
)
 
&
 


    
guides
(
fill
=
guide_legend
(
override.aes
=
list
(
shape
=
21
, size
=
2
)
)
)
 
&


    
theme_classic
(
)
 
&
 
theme
(


        axis.title.x
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
