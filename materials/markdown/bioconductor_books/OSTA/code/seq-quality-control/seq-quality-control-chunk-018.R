# plot library size vs. number of cells per spot


p1
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"scatter"
, 


    x_metric
=
"cell_count"
, 


    y_metric
=
"sum"
,


    y_threshold
=
600
)
 
+
 


    
ggtitle
(
"Library size vs. cells per spot"
)




# plot mito proportion vs. number of cells per spot


p2
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"scatter"
, 


    x_metric
=
"cell_count"
, 


    y_metric
=
"subsets_mito_percent"
, 


    y_threshold
=
30
)
 
+
 


    
ggtitle
(
"Mito proportion vs. cells per spot"
)




p1
 
|
 
p2
