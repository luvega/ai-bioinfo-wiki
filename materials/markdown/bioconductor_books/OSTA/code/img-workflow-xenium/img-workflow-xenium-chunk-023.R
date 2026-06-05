gs
 
<-
 
c
(
"PIGR"
, 
"IGHG3"
, 
"CEACAM6"
)


es
 
<-
 
scale
(
logcounts
(
sub
)
)


es
 
<-
 
t
(
as.matrix
(
es
[
gs
, 
]
)
)


colData
(
sub
)
 
<-
 
cbind
(
colData
(
sub
)
, 
es
)


ps
 
<-
 
lapply
(
gs
, \
(
.
)
 
.plt_xy
(
sub
, 
.
)
 
+
 
ggtitle
(
.
)
)


wrap_plots
(
ps
, nrow
=
1
)
 
&


    
scale_color_gradientn
(
NULL
, 


        labels
=
c
(
"low"
, 
"high"
)
, 


        colors
=
rev
(
hcl.colors
(
9
, 
"PuRd"
)
)
,


        limits
=
rng
, breaks
=
rng
 
<-
 
range
(
es
)
)
 
&
 


    
theme
(
plot.title
=
element_text
(
hjust
=
0.5
)
)
