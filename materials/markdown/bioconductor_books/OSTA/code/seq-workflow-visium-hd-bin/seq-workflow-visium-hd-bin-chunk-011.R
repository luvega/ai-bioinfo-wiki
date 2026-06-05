p1
 
<-
 
plotVisium
(
vhd16
, 


    annotate
=
"libsize"
, point_shape
=
22
,


    zoom
=
TRUE
, show_axes
=
TRUE
, point_size
=
1.3
)
 
+
 


    
xlim
(
c
(
422
, 
442
)
)
 
+
 
ylim
(
c
(
318
, 
330
)
)
 
+
 


    
ggtitle
(
"16 µm - original"
)




vhd16
 
<-
 
vhd16
[
, 
vhd16
$
libsize
 
>
 
400
]




p2
 
<-
 
plotVisium
(
vhd16
, 


    annotate
=
"libsize"
, point_shape
=
22
,


    zoom
=
TRUE
, show_axes
=
TRUE
, point_size
=
1.3
)
 
+
 


    
xlim
(
c
(
422
, 
442
)
)
 
+
 
ylim
(
c
(
318
, 
330
)
)
 
+
 


    
ggtitle
(
"16 µm - post > 400 UMI QC"
)




p1
 
|
 
p2
