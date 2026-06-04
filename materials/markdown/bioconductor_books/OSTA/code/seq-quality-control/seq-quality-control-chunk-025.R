# spot plot of log-transformed library size


p1
 
<-
 
plotCoords
(
spe
, 


    annotate
=
"sum_log"
)
 
+
 


    
ggtitle
(
"log2(Library Size)"
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
, in_tissue
=
"in_tissue"
, 


    annotate
=
"sum_outliers"
, point_size
=
0.2
)
 
+
 


    
ggtitle
(
"Local Outliers (Library Size)"
)




# spot plot of log-transformed detected genes


p3
 
<-
 
plotCoords
(
spe
, 


    annotate
=
"detected_log"
)
 
+
 


    
ggtitle
(
"log2(Detected)"
)




p4
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"spot"
, in_tissue
=
"in_tissue"
, 


    annotate
=
"detected_outliers"
, point_size
=
0.2
)
 
+
 


    
ggtitle
(
"Local Outliers (Detected)"
)




# spot plot of mitochondrial proportion


p5
 
<-
 
plotCoords
(
spe
, 


    annotate
=
"subsets_mito_percent"
)
 
+
 


    
ggtitle
(
"Mito Proportion"
)




p6
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"spot"
, in_tissue
=
"in_tissue"
, 


    annotate
=
"subsets_mito_percent_outliers"
, point_size
=
0.2
)
 
+
 


    
ggtitle
(
"Local Outliers (Mito Prop)"
)




# plot using patchwork


(
p1
 
/
 
p2
)
 
|
 
(
p3
 
/
 
p4
)
 
|
 
(
p5
 
/
 
p6
)
