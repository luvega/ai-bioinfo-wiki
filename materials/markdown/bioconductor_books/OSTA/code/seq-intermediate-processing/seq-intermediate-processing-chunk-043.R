# gene-wise spatial plots


gs
 
<-
 
c
(
"MBP"
, 
"PLP1"
, 
"NRGN"
, 
"SNAP25"
, 
"NEFL"
, 
"HPCAL1"
)


ps
 
<-
 
lapply
(
gs
, \
(
.
)
 
{


    
plotCoords
(
spe
, 


        annotate 
=
 
.
, 


        feature_names 
=
 
"gene_name"
, 


        assay_name 
=
 
"logcounts"
)
 
}
)


# figure arrangement


wrap_plots
(
ps
, nrow 
=
 
2
)
 
&
 


  
theme
(
legend.key.width 
=
 
unit
(
0.4
, 
"lines"
)
, 


        legend.key.height 
=
 
unit
(
0.8
, 
"lines"
)
)
 
&
 


  
scale_color_gradientn
(
colors 
=
 
rev
(
hcl.colors
(
9
, 
"Rocket"
)
)
)
