colData
(unfiltered) <-
 
cbind
(
colData
(unfiltered), stats)


unfiltered
$
discard <-
 
qc2
$
discard


unfiltered
$
Plate_ID <-
 
factor
(unfiltered
$
Plate_ID)




gridExtra
::
grid.arrange
(


    
plotColData
(unfiltered, 
y=
"sum"
, 
x=
"Plate_ID"
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
),


    
plotColData
(unfiltered, 
y=
"detected"
, 
x=
"Plate_ID"
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
),


    
ncol=
1


)
