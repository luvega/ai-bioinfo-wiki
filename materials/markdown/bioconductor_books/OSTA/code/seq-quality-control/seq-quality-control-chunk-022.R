# check spatial pattern of discarded spots if threshold is too high


spe
$
qc_lib_size_2000
 
<-
 
spe
$
sum
 
<
 
2000




# plot the spots flagged with the high threshold


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
"qc_lib_size_2000"
)
 
+
 


    
ggtitle
(
"Library size (< 2000 UMI)"
)




# plot manually annotated reference layers


p2
 
<-
 
plotCoords
(
spe
, 


    annotate
=
"ground_truth"
, pal
=
"libd_layer_colors"
)
 
+
 


    
ggtitle
(
"Manually annotated layers"
)




# plot library size by manual annotation


p3
 
<-
 
plotColData
(
spe
, 


    x
=
"ground_truth"
, y
=
"sum"
, colour_by
=
"ground_truth"
)
 
+
 


    
theme
(
axis.text.x
=
element_text
(
angle
=
45
, hjust
=
1
)
)
 
+


    
ggtitle
(
"Library size by layer"
)
 
+
 
xlab
(
""
)


  


p1
 
|
 
p2
 
|
 
p3
