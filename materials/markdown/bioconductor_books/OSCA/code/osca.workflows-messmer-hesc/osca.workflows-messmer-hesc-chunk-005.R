gridExtra
::
grid.arrange
(


    
plotColData
(original, 
x=
"experiment batch"
, 
y=
"sum"
,


        
colour_by=
I
(filtered
$
discard), 
other_field=
"phenotype"
) 
+


        
facet_wrap
(
~
phenotype) 
+
 
scale_y_log10
(),


    
plotColData
(original, 
x=
"experiment batch"
, 
y=
"detected"
,


        
colour_by=
I
(filtered
$
discard), 
other_field=
"phenotype"
) 
+


        
facet_wrap
(
~
phenotype) 
+
 
scale_y_log10
(),


    
plotColData
(original, 
x=
"experiment batch"
, 
y=
"subsets_Mito_percent"
,


        
colour_by=
I
(filtered
$
discard), 
other_field=
"phenotype"
) 
+


        
facet_wrap
(
~
phenotype),


    
plotColData
(original, 
x=
"experiment batch"
, 
y=
"altexps_ERCC_percent"
,


        
colour_by=
I
(filtered
$
discard), 
other_field=
"phenotype"
) 
+


        
facet_wrap
(
~
phenotype),


    
ncol=
1


)
