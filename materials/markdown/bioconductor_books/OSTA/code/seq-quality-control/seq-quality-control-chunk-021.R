# check spatial pattern of discarded spots


p1
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"spot"
, annotate
=
"qc_lib_size"
)
 
+
 


    
ggtitle
(
"Library size (< 600 UMI)"
)




p2
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"spot"
, annotate
=
"qc_detected"
)
 
+
 


    
ggtitle
(
"Detected genes (< 400 genes)"
)




p3
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"spot"
, annotate
=
"qc_mito_prop"
)
 
+
 


    
ggtitle
(
"Mito proportion (> 30%)"
)




p1
 
|
 
p2
 
|
 
p3
