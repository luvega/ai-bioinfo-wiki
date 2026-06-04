i
 
<-
 
c
(
"SingleCell"
, 
"Spatial"
)


j
 
<-
 
c
(


    
"BatchEffect"
, 
"Normalization"
, 
"QualityControl"
, 
"Visualization"
, 
# WorkflowStep


    
"Clustering"
, 
"DimensionReduction"
, 
"FeatureExtraction"
, 
# StatisticalMethod


    
"DifferentialExpression"
, 
"GeneSetEnrichment"
)
 
# BiologicalQuestion


names
(
i
)
 
<-
 
i
; 
names
(
j
)
 
<-
 
j


# count packages for each pair of terms


gg
 
<-
 
mapply
(


    i
=
i
, j
=
rep
(
j
, each
=
2
)
, 


    SIMPLIFY
=
FALSE
, \
(
i
, 
j
)
 
{


        
n
 
<-
 
sum
(
.f
(
c
(
i
, 
j
)
)
)


        
data.frame
(
i
, 
j
, 
n
)


    
}
)
 
|>
 
do.call
(
what
=
rbind
)


# order x-axis by total


xo
 
<-
 
gg
 
|>


    
group_by
(
j
)
 
|>


    
summarise_at
(
"n"
, 
sum
)
 
|>


    
arrange
(
n
)
 
|>


    
pull
(
j
)


ggplot
(
gg
, 
aes
(
j
, 
n
, fill
=
i
)
)
 
+
 


    
scale_x_discrete
(
limits
=
xo
)
 
+


    
geom_col
(
position
=
"dodge"
, alpha
=
2
/
3
)
 
+


    
labs
(
x
=
NULL
, y
=
"# packages"
, fill
=
"biocViews"
)
 
+


    
theme_bw
(
)
 
+
 
theme
(


        aspect.ratio
=
1
, 


        panel.grid.minor
=
element_blank
(
)
,


        axis.text.x
=
element_text
(
angle
=
45
, hjust
=
1
)
)
