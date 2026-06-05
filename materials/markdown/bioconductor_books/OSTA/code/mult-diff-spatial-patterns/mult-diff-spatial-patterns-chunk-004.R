plotCoords
(
spe
, 


    annotate
=
"Banksy_smooth"
, 


    in_tissue
=
NULL
,


    x_coord
=
"sdimx"
, 


    y_coord
=
"sdimy"
, 


    y_reverse
=
FALSE
,


    sample_id
=
"sample_id"
)
 
+
 


    
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
 
+
 


    
scale_color_manual
(
values
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
