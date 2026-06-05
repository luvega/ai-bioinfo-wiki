# plot spatial distributions of discarded spots


p1
 
<-
 
plotObsQC
(
spe
, 


    plot_type
=
"spot"
, 


    annotate
=
"qc_lib_size"
)
 
+
 


    
ggtitle
(
"Library size (< threshold)"
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
, 


    annotate
=
"qc_detected"
)
 
+


    
ggtitle
(
"Detected genes (< threshold)"
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
, 


    annotate
=
"qc_mito"
)
 
+
 


    
ggtitle
(
"Mito proportion (> threshold)"
)




wrap_plots
(
p1
, 
p2
, 
p3
, nrow
=
1
, guides
=
"collect"
)
 
&
 
labs
(
col
=
"discard"
)
