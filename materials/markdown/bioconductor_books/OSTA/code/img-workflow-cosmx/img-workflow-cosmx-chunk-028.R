gs
 
<-
 
c
(
"Mbp"
, 
"Calm1"
, 
"Calm2"
, 
"Snap25"
)


ps
 
<-
 
lapply
(
gs
, \
(
g
)
 
{


    
sub
[[
g
]
]
 
<-
 
logcounts
(
sub
)
[
g
, 
]


    
plotPolygons
(
sub
, colourBy
=
g
)
 
+
 
ggtitle
(
g
)


}
)
 


dy
 
<-
 
range
(
logcounts
(
sub
)
[
gs
, 
]
)


wrap_plots
(
ps
, guides
=
"collect"
)
 
&


    
scale_fill_viridis_c
(


        
"expression"
, 


        limits
=
dy
, breaks
=
dy
,


        labels
=
c
(
"low"
, 
"high"
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
