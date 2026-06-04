plotVisium
(
.vhd16
, 


    annotate
=
"cluster"
, zoom
=
TRUE
, 


    point_shape
=
22
, point_size
=
1.6
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
 


plot_spacer
(
)
 
+


plotVisium
(
.vhd16
, 


    annotate
=
"Banksy"
, zoom
=
TRUE
, 


    point_shape
=
22
, point_size
=
1.6
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
 


plot_spacer
(
)
 
+


plotVisium
(
.vhd16
, 


    annotate
=
".DeconLabel1"
, zoom
=
TRUE
, 


    point_shape
=
22
, point_size
=
1.6
, 


    pal
=
unname
(
pals
::
trubetskoy
(
)
)
)
 
+


plot_layout
(
nrow
=
1
, widths
=
c
(
1
, 
0.05
, 
1
, 
0.05
, 
1
)
)
 
&
 


    
facet_null
(
)
 
&
 
theme
(
legend.key.size
=
unit
(
0
, 
"lines"
)
)
