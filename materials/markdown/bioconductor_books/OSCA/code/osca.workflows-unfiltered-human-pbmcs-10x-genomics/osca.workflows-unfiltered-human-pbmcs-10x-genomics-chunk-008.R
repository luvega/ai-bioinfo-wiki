colData
(unfiltered) <-
 
cbind
(
colData
(unfiltered), stats)


unfiltered
$
discard <-
 
high.mito




gridExtra
::
grid.arrange
(


    
plotColData
(unfiltered, 
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
