# load dataset as SPE & convert to SFE


spe
 
<-
 
Janesick_breastCancer_Xenium_rep1
(
)


sfe
 
<-
 
toSpatialFeatureExperiment
(
spe
)




# load the official 10X annotations 


fnm
 
<-
 
"https://cdn.10xgenomics.com/raw/upload/v1695234604/Xenium%20Preview%20Data/Cell_Barcode_Type_Matrices.xlsx"


labels
 
<-
 
read.xlsx
(
fnm
, sheet
=
4
)


labels
$
cell_id
 
<-
 
(
labels
$
Barcode
)




# add the cell type labels to the spe


cd
 
<-
 
as.data.frame
(
colData
(
sfe
)
)


cd
 
<-
 
left_join
(
cd
, 


    
as.data.frame
(
labels
)
, 


    by
=
join_by
(
"cell_id"
)
)


colData
(
sfe
)
 
<-
 
DataFrame
(
cd
)




# exclude 0-count cells &


# cells without annotation


sfe
 
<-
 
sfe
[
, 
colSums
(
counts
(
sfe
)
)
 
>
 
0
]


sfe
 
<-
 
sfe
[
, 
!
is.na
(
sfe
$
Cluster
)
]




# log-library size normalization


sfe
 
<-
 
logNormCounts
(
sfe
)




# basic theme for spatial plots


xy
 
<-
 
spatialCoords
(
sfe
)


theme_xy
 
<-
 
list
(


    
coord_equal
(
expand
=
FALSE
)
, 


    
theme_void
(
)
, 
theme
(


        plot.margin
=
margin
(
l
=
5
)
,


        legend.key
=
element_blank
(
)
,


        panel.background
=
element_rect
(
fill
=
"black"
)
)
)
