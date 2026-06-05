gs
 
<-
 
intersect
(
rownames
(
spe
)
, 
rownames
(
sqe
)
)


imp
 
<-
 
as.matrix
(
t
(
logcounts
(
sqe
[
gs
, 
]
)
)
)


obs
 
<-
 
as.matrix
(
t
(
logcounts
(
spe
[
gs
, 
]
)
)
)


cm
 
<-
 
cor
(
imp
, 
obs
, method
=
"pearson"
)


df
 
<-
 
data.frame
(
g
=
gs
, p
=
diag
(
cm
)
)


df
$
g
 
<-
 
factor
(
df
$
g
, 
df
$
g
[
order
(
-
df
$
p
)
]
)


ggplot
(
df
, 
aes
(
g
, 
p
, fill
=
p
 
>
 
0.5
)
)
 
+
 
geom_col
(
)
 
+


    
labs
(
x
=
"correlation (observed vs. imputed)"
, y
=
NULL
)
 
+


    
geom_hline
(
yintercept
=
0.5
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
,


        panel.grid
=
element_blank
(
)
,


        axis.text.x
=
element_text
(
angle
=
90
, vjust
=
0.5
, hjust
=
1
)
)
