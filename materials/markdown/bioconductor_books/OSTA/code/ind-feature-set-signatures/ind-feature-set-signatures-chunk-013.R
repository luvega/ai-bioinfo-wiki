lapply
(
c
(
"hypoxia"
, 
"apoptosis"
, 
"myogenesis"
)
, \
(
.
)
 
{


    
q
 
<-
 
quantile
(
x
 
<-
 
spe
[[
.
]
]
, 
c
(
0.01
, 
0.99
)
)


    
x
 
<-
 
(
x
-
q
[
1
]
)
/
diff
(
q
)
 
# 01-quantile scaling


    
x
[
x
 
<
 
0
]
 
<-
 
0
; 
x
[
x
 
>
 
1
]
 
<-
 
1
; 
spe
[[
.
]
]
 
<-
 
x


    
plt
 
<-
 
plotCoords
(
spe
, annotate
=
.
, point_size 
=
 
0.01
)
 


    
plt


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
 


    
scale_color_gradientn
(


        
"q-scaled\nAUCell"
, 


        colors
=
hcl.colors
(
9
, 
"Plasma"
)
)
 
&


    
theme
(


        legend.key.height
=
unit
(
1
, 
"lines"
)
,


        legend.key.width
=
unit
(
0.5
, 
"lines"
)
,


        panel.background
=
element_rect
(
fill
=
"black"
)
)
