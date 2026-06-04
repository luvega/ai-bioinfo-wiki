df
 
<-
 
data.frame
(
colData
(
cos
)
)


ys
 
<-
 
c
(
"detected"
, 
"total"
, 
"Area_um"
, 
"log2SignalDensity"
)


ys
 
<-
 
c
(
grepv
(
"Mean"
, 
names
(
df
)
)
, 
ys
)


fd
 
<-
 
pivot_longer
(
df
, 
ys
)
 
|>


    
mutate
(
value
=
case_when
(


        
grepl
(
"Mean"
, 
name
)
 
~
 
asinh
(
value
)
,


        
grepl
(
"total"
, 
name
)
 
~
 
log10
(
value
)
,


        
grepl
(
"^Area"
, 
name
)
 
~
 
log10
(
value
)
,


        
TRUE
 
~
 
value
)
, fov
=
factor
(
fov
)
)


ggplot
(
fd
, 
aes
(
fov
, 
value
, fill
=
fov
)
)
 
+
 


    
facet_wrap
(
~
name
, nrow
=
3
, scales
=
"free_y"
)
 
+


    
geom_boxplot
(
linewidth
=
0.2
, outlier.size
=
0.2
)
 
+


    
scale_x_discrete
(
breaks
=
c
(
1
, 
seq
(
10
, 
max
(
cos
$
fov
)
, 
10
)
)
)
 
+


    
theme_minimal
(
)
 
+
 
theme
(
legend.position
=
"none"
)
 
+


    
labs
(
x
=
"field of view (FOV)"
, y
=
NULL
)
