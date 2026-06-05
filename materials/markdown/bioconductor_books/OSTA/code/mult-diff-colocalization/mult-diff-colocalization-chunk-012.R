# relevel to have non-diabetic as the reference category


spe
$
patient_stage
 
<-
 
relevel
(
factor
(
spe
$
patient_stage
)
, 
"Non-diabetic"
)




# run the spatial statistics inference


resLs
 
<-
 
crossSpatialInference
(


    
spe
, 


    selection
=
c
(
"alpha"
, 
"Tc"
, 
"Th"
)
,


    fun
=
"Gcross"
, 


    marks
=
"cell_type"
,


    rSeq
=
seq
(
0
, 
50
, l
=
50
)
, 


    correction
=
"rs"
,


    transformation
=
"Fisher"
,


    eps
=
1e-3
,


    delta
=
"minNnDist"
,


    family
=
mgcv
::
scat
(
link
=
"log"
)
,


    sample_id
=
"patient_id"
,


    image_id
=
"image_name"
, 


    condition
=
"patient_stage"
,


    algorithm
=
"bam"
,


    verbose
=
FALSE
)
