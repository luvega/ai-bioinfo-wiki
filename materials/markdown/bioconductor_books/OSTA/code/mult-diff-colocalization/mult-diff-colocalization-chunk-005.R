# filter out some larger 'cell_type's


# (for runtime reasons in this demo)


ids
 
<-
 
setdiff
(


    
levels
(
spe
$
cell_type
)
, 
c
(
"endothelial"
,


    
"alpha"
, 
"acinar"
, 
"ductal"
, 
"unknown"
)
)


.spe
 
<-
 
spe
[
, 
spe
$
cell_type
 
%in%
 
ids
]




# perform spatial tests


spicyTestPair
 
<-
 
spicy
(


    cells
=
.spe
, 


    condition
=
"patient_stage"
, 


    imageID
=
"image_name"
, 


    cellType
=
"cell_type"
,


    window
=
"square"
, 


    cores
=
4
)




# extract most significant pairs


head
(
topPairs
(
spicyTestPair
)
)
