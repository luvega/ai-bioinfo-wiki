# select top-3 markers for each cluster & get gene symbols


gs
 
<-
 
unique
(
unlist
(
lapply
(
mgs
, \
(
df
)
 
head
(
rownames
(
df
)
, 
3
)
)
)
)


gs
 
<-
 
rowData
(
spe
)
$
gene_name
[
match
(
gs
, 
rownames
(
spe
)
)
]


# gene-wise spatial plots


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
 
4
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
