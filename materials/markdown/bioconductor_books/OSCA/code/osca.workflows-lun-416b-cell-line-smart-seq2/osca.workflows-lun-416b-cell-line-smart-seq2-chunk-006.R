gridExtra
::
grid.arrange
(


    
plotColData
(unfiltered, 
x=
"sum"
, 
y=
"subsets_Mt_percent"
, 


        
colour_by=
"discard"
) 
+
 
scale_x_log10
(),


    
plotColData
(unfiltered, 
x=
"altexps_ERCC_percent"
, 
y=
"subsets_Mt_percent"
,


        
colour_by=
"discard"
),


    
ncol=
2


)
