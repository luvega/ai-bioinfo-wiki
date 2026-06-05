colData
(unfiltered) <-
 
cbind
(
colData
(unfiltered), stats)


unfiltered
$
block <-
 
factor
(unfiltered
$
block)


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
"block"
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
"block"
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
"block"
, 
y=
"subsets_Mt_percent"
, 


        
colour_by=
"discard"
) 
+
 
ggtitle
(
"Mito percent"
),


    
plotColData
(unfiltered, 
x=
"block"
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
),


    
nrow=
2
,


    
ncol=
2


)
