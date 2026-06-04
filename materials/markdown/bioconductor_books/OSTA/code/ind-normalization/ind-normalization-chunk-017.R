(
p1
 
+
 
p2
)
 
&


    
geom_boxplot
(


        
aes
(
Label
, 
EPCAM
, fill
=
Label
)
, 


        outlier.shape
=
16
, outlier.stroke
=
0
)
 
&


    
scale_fill_manual
(
values
=
unname
(
pals
::
tableau20
(
)
)
)
 
&


    
labs
(
x
=
"Cell type"
, y
=
"EPCAM expression"
)
 
&


    
theme_bw
(
)
 
&
 
theme
(


        aspect.ratio
=
1
,


        legend.position
=
"none"
,


        panel.grid.minor
=
element_blank
(
)
,


        plot.title
=
element_text
(
hjust
=
0.5
)
,


        axis.text.x
=
element_text
(
angle
=
45
, hjust
=
1
)
)
