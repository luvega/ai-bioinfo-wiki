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
"islet unos id"
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
"islet unos id"
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
"islet unos id"
, 
y=
"subsets_Mito_percent"
,


        
colour_by=
"discard"
) 
+
 
ggtitle
(
"Mito percent"
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
