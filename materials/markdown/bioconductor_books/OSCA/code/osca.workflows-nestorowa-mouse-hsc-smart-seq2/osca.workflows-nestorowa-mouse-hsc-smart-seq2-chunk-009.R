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
"altexps_ERCC_percent"
,


        
colour_by=
"discard"
) 
+
 
ggtitle
(
"ERCC percent"
),


    
ncol=
2


)
