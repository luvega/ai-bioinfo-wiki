# get local mito ratio variance of a normal sample


spe
 
<-
 
localVariance
(
spe
, 


    n_neighbors
=
36
, 


    metric
=
"subsets_mito_percent"
, 


    name
=
"local_mito_variance_k36"
)




# plot distribution of local variance in mitochondrial percentage


hangnail_sample
 
<-
 
data.frame
(
x
=
spe.hangnail
$
local_mito_variance_k36
)


normal_sample
 
<-
 
data.frame
(
x
=
spe
$
local_mito_variance_k36
)




p1
 
<-
 
ggplot
(
hangnail_sample
, 
aes
(
x
)
)
 
+
 
ggtitle
(
"Hangnail Sample"
)


p2
 
<-
 
ggplot
(
normal_sample
, 
aes
(
x
)
)
 
+
 
ggtitle
(
"Normal Sample"
)




(
p1
 
|
 
p2
)
 
&
 


    
geom_density
(
fill
=
"gray"
, alpha
=
0.5
)
 
&


    
xlab
(
"local mitochondrial variance"
)
