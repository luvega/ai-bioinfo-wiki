f
 
<-
 
Area
^
(
1
/
4
)
 
~
 
patient_stage
 
+
 
(
1
|
patient_id
)
 
+
 
(
1
|
image_name
)


summary
(
mod
 
<-
 
lmer
(
formula
=
f
, data
=
allIslets
)
)
