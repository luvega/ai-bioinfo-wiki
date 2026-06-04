colData
(sce
.416
b) <-
 
cbind
(
colData
(sce
.416
b), df)


sce
.416
b
$
block <-
 
factor
(sce
.416
b
$
block)


sce
.416
b
$
phenotype <-
 
ifelse
(
grepl
(
"induced"
, sce
.416
b
$
phenotype),


    
"induced"
, 
"wild type"
)


sce
.416
b
$
discard <-
 
reasons
$
discard




library
(scater)


gridExtra
::
grid.arrange
(


    
plotColData
(sce
.416
b, 
x=
"block"
, 
y=
"sum"
, 
colour_by=
"discard"
,


        
other_fields=
"phenotype"
) 
+
 
facet_wrap
(
~
phenotype) 
+
 


        
scale_y_log10
() 
+
 
ggtitle
(
"Total count"
),


    
plotColData
(sce
.416
b, 
x=
"block"
, 
y=
"detected"
, 
colour_by=
"discard"
, 


        
other_fields=
"phenotype"
) 
+
 
facet_wrap
(
~
phenotype) 
+
 


        
scale_y_log10
() 
+
 
ggtitle
(
"Detected features"
),


    
plotColData
(sce
.416
b, 
x=
"block"
, 
y=
"subsets_Mito_percent"
, 


        
colour_by=
"discard"
, 
other_fields=
"phenotype"
) 
+
 


        
facet_wrap
(
~
phenotype) 
+
 
ggtitle
(
"Mito percent"
),


    
plotColData
(sce
.416
b, 
x=
"block"
, 
y=
"altexps_ERCC_percent"
, 


        
colour_by=
"discard"
, 
other_fields=
"phenotype"
) 
+
 


        
facet_wrap
(
~
phenotype) 
+
 
ggtitle
(
"ERCC percent"
),


    
ncol=
1


)
