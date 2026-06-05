# extract co-localization metrics


cd
 
<-
 
colData
(
.spe
)
 
|>


    
as.data.frame
(
)
 
|>
 


    
distinct
(
patient_id
, 
patient_stage
, 
image_name
)
 
|>


    
dplyr
::
rename
(
imageID
=
image_name
)


bind
(
spicyTest
)
 
|>
 


    
# merge with metadata


    
merge
(
cd
, by
=
"imageID"
, all
=
FALSE
)
 
|>


    
# select columns of interest


    
select
(
c
(
imageID
, 
Tc__beta
, 
patient_id
, 
patient_stage
)
)
 
|>


    
filter
(
imageID
 
%in%
 
c
(
"L29"
, 
"O02"
, 
"E17"
, 
"G17"
)
)
