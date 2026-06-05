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
rownames
(
isletMetrics
)
)
 
|>
 


    
pivot_longer
(
-
patient_stage
)
 
|>
 


    
filter
(
name
 
%in%
 
c
(
"Area"
, 
"Compactness"
, 
"Curl"
)
)


# visualization


ggplot
(
df
, 
aes
(
patient_stage
, 
value
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
aes
(
fill
=
NULL
)
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


    
scale_x_discrete
(
guide
=
guide_axis
(
n.dodge
=
2
)
)
 
+
 


    
facet_wrap
(
~
name
, scales
=
"free"
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
