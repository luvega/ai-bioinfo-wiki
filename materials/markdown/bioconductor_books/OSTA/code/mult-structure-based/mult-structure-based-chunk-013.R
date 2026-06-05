# wrangling


df
 
<-
 
allIslets
 
|>
 


    
st_drop_geometry
(
)
 
|>
 


    
select
(
patient_stage
, 
patient_id
, 
rownames
(
isletMetrics
)
)
 
|>
 


    
pivot_longer
(
-
c
(
patient_stage
, 
patient_id
)
)
 
|>
 


    
filter
(
name
 
%in%
 
c
(
"Area"
)
)


# visualization


ggplot
(
df
, 
aes
(
patient_id
, 
value
^
(
1
/
4
)
, fill
=
patient_stage
)
)
 
+
 


    
geom_violin
(
)
 
+
 
geom_boxplot
(
fill
=
NA
, width
=
0.3
)
 
+
 


    
scale_fill_manual
(
values
=
unname
(
pals
::
tol
(
n
=
3
)
)
)
 
+


    
facet_wrap
(
~
patient_stage
, scales
=
"free_x"
)
 
+
 


    
geom_jitter
(
size
=
0.5
)
 
+
 
ylab
(
"Area"
)
 
+


    
guides
(
fill
=
"none"
)
 
+
 
theme_bw
(
)
