# factor levels for 'patient_stage'


lv
 
<-
 
c
(
"Non-diabetic"
, 
"Onset"
, 
"Long-duration"
)


# cell metadata columns to keep


colsKeep
 
<-
 
c
(


    
"sample_id"
, 
"image_name"
,


    
"patient_disease_duration"
, 


    
"patient_id"
, 
"patient_stage"
, 


    
"patient_age"
, 
"patient_gender"
,


    
"tissue_slide"
, 
"tissue_region"
)
 


patientData
 
<-
 
colData
(
spe
)
 
|>
 


    
as_tibble
(
)
 
|>
 


    
# keep selected columns


    
select
(
all_of
(
colsKeep
)
)
 
|>
 


    
# refactor patient IDs & stages


    
group_by
(
image_name
)
 
|>
 


    
mutate_at
(
"patient_id"
, 
factor
)
 
|>


    
mutate_at
(
"patient_stage"
, 
factor
, 
lv
)
 
|>


    
# keep only unique combinations


    
unique
(
)
 


# join with results from reconstruction


allIslets
 
<-
 
left_join
(
allIslets
, 
patientData
, by
=
"image_name"
)
