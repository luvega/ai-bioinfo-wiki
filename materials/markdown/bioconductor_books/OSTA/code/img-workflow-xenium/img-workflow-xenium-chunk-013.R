spe
$
ol
 
<-
 
ol
$
discard


.plt_xy
(
spe
, 
"sum"
)
 
+
  


    
scale_color_viridis_c
(


        
"# counts"
, 


        trans
=
"log1p"
,


        breaks
=
range
(
spe
$
sum
)
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
 
+


.plt_xy
(
spe
, 
"detected"
)
 
+


    
scale_color_viridis_c
(


        
"# features"
, 


        breaks
=
range
(
spe
$
detected
)
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
 
+


.plt_xy
(
spe
[
, 
order
(
spe
$
ol
)
]
, 
"ol"
)
 
+
 


    
scale_color_manual
(


        
"low-quality"
,


        labels
=
c
(
"no"
, 
"yes"
)
,


        values
=
c
(
"lavender"
, 
"purple"
)
)
