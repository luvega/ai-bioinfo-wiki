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
),


    
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
),


    
plotColData
(unfiltered, 
x=
"Donor"
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
),


    
ncol=
2


)
