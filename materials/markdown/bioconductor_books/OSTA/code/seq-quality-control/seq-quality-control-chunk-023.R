# library size and outliers


p1
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"violin"
, x_metric
=
"sum"
, 


    annotate
=
"qc_lib_size"
, point_size
=
0.5
)
 
+
 


    
xlab
(
"Library size"
)




# detected genes and outliers


p2
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"violin"
, x_metric
=
"detected"
, 


    annotate
=
"qc_detected"
, point_size
=
0.5
)
 
+
 


    
xlab
(
"Detected genes"
)
 




# mito proportion and outliers


p3
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"violin"
, x_metric
=
"subsets_mito_percent"
, 


    annotate
=
"qc_mito_prop"
, point_size
=
0.5
)
 
+
 


    
xlab
(
"Mito proportion"
)




p1
 
|
 
p2
 
|
 
p3
