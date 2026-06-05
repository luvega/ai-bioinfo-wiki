# z-transformed library size and outliers


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
"sum_z"
, 


    annotate
=
"sum_outliers"
, point_size
=
0.5
)
 
+
 


    
xlab
(
"sum_outliers"
)




# z-transformed detected genes and outliers


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
"detected_z"
, 


    annotate
=
"detected_outliers"
, point_size
=
0.5
)
 
+
 


    
xlab
(
"detected_outliers"
)




# z-transformed mito percent and outliers


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
"subsets_mito_percent_z"
, 


    annotate
=
"subsets_mito_percent_outliers"
, point_size
=
0.5
)
 
+
 


    
xlab
(
"mito_outliers"
)




p1
 
|
 
p2
 
|
 
p3
