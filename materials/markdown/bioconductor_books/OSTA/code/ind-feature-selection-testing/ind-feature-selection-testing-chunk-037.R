# get top SVGs from each method


gs
 
<-
 
list
(


    HVGs
=
top_HVGs
, 


    DEGs
=
top_DEGs
, 


    DESpace
=
top_DESpace
)


# get gene symbols from ensembl identifiers


idx
 
<-
 
match
(
unlist
(
gs
)
, 
rowData
(
spe
)
$
gene_id
)


.gs
 
<-
 
rowData
(
spe
)
$
gene_name
[
idx
]


# expression plots for each top gene


ps
 
<-
 
lapply
(
seq_along
(
.gs
)
, \
(
.
)
 
{


    
plotCoords
(
spe
, 


        point_size
=
0
,


        annotate
=
.gs
[
.
]
, 


        assay_name
=
"logcounts"
, 


        feature_names
=
"gene_name"
)
 
+
 


        
if
 
(
.
 
%%
 
6
 
==
 
1
)
 
list
(


            
ylab
(
names
(
gs
)
[
ceiling
(
.
/
6
)
]
)
, 


            
theme
(
axis.title.y
=
element_text
(
)
)
)


}
)
 


wrap_plots
(
ps
, nrow
=
3
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
 
pals
::
parula
(
)
)
