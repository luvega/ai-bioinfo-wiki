# specify colors for sender/receiver signals


pal
 
<-
 
list
(


    s
=
c
(
"grey90"
, 
"gold"
, 
"black"
)
, 


    r
=
c
(
"grey90"
, 
"turquoise"
, 
"black"
)
)




# get variables names of the form: x, s-x-y, r-x-y, y


.f
 
<-
 \
(
i
, 
j
)
 
c
(
i
, 
paste
(
c
(
"s"
,
"r"
)
, 
i
,
j
, sep
=
"-"
)
, 
j
)


xs
 
<-
 
.f
(
"CXCL12"
, 
"CXCR4"
)




# visualize expression & signaling side-by-side


lapply
(
seq_along
(
xs
)
, \
(
.
)
 
{


    
typ
 
<-
 
ifelse
(
.
 
<
 
3
, 
"s"
, 
"r"
)


    
plotCoords
(
sub
, point_size
=
0.5
,


        annotate
=
xs
[
.
]
, assay_name
=
"logcounts"
)
 
+
 


        
scale_color_gradientn
(
typ
, colors
=
pal
[[
typ
]
]
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


    
theme
(
legend.key.width
=
unit
(
0.5
, 
"lines"
)
)
