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




library
(scater)


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
"sample"
, 
colour_by=
"discard"
, 


        
other_fields=
"protocol"
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


        
facet_wrap
(
~
protocol),


    
plotColData
(unfiltered, 
y=
"detected"
, 
x=
"sample"
, 
colour_by=
"discard"
,


        
other_fields=
"protocol"
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
 
facet_wrap
(
~
protocol),


    
ncol=
1


)
