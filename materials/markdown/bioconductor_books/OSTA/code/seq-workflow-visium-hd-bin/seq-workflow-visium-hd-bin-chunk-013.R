(
plotCoords
(
vhd8
, 


    annotate
=
"cluster"
, point_size
=
0.05
, point_shape
=
15
,


    pal
=
unname
(
pals
::
kelly
(
)
)
)
 
+
 
ggtitle
(
"8 µm"
)
)
 
|


(
plotCoords
(
vhd16
[
, 
!
is.na
(
vhd16
$
cluster
)
]
, 


    annotate
=
"cluster"
, point_size
=
0.1
, point_shape
=
15
, 


    pal
=
unname
(
pals
::
kelly
(
)
)
)
 
+
 
ggtitle
(
"16 µm"
)
)
