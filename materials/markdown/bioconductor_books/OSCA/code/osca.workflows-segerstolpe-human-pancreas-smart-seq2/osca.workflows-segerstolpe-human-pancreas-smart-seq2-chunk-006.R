colData
(unfiltered) <-
 
cbind
(
colData
(unfiltered), stats)


unfiltered
$
discard <-
 
qc
$
discard




gridExtra
::
grid.arrange
(


    
plotColData
(unfiltered, 
x=
"Donor"
, 
y=
"sum"
, 
colour_by=
"discard"
) 
+


        
scale_y_log10
() 
+
 
ggtitle
(
"Total count"
) 
+


        
theme
(
axis.text.x =
 
element_text
(
angle =
 
90
)),


    
plotColData
(unfiltered, 
x=
"Donor"
, 
y=
"detected"
, 
colour_by=
"discard"
) 
+


        
scale_y_log10
() 
+
 
ggtitle
(
"Detected features"
) 
+


        
theme
(
axis.text.x =
 
element_text
(
angle =
 
90
)),


    
plotColData
(unfiltered, 
x=
"Donor"
, 
y=
"altexps_ERCC_percent"
,


        
colour_by=
"discard"
) 
+
 
ggtitle
(
"ERCC percent"
) 
+


        
theme
(
axis.text.x =
 
element_text
(
angle =
 
90
)),


    
ncol=
2


)
