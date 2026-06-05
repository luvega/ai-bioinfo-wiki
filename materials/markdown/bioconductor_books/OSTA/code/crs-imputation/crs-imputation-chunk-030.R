.p
 
<-
 \
(
obj
, 
col
)
 
{


    
plotCoords
(
obj
, 


        point_size
=
0
,


        annotate
=
col
, 


        assay_name
=
"logcounts"
)


}


pal
 
<-
 
scale_color_gradient2
(
"obs."
, high
=
"red"
)


qal
 
<-
 
scale_color_gradient2
(
"imp."
, high
=
"blue"
)


.p
(
spe
, 
"ACTA2"
)
 
+
 
pal
 
+


.p
(
sqe
, 
"ACTA2"
)
 
+
 
qal
 
+


.p
(
sqe
, 
"KRT17"
)
 
+
 
qal
 
+


    
plot_layout
(
nrow
=
1
)
