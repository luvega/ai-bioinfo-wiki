.ids
 
<-
 
levels
(
spe
$
sample_id
)


lapply
(
seq_along
(
.ids
)
, \
(
.
)
 
{


    
.spe
 
<-
 
spe
[
, 
spe
$
sample_id
 
==
 
.ids
[
.
]
]


    
p
 
<-
 
FeaturePlot
(
.spe
, 


        feature
=
top_dsp
,


        platform
=
"Stereo-seq"
,


        coordinates
=
c
(
"sdimx"
, 
"sdimy"
)
,


        cluster_col
=
"Banksy_smooth"
, cluster
=
"2"
,


        diverging
=
TRUE
, low
=
"gray95"
, high
=
"blue"
)


    
# ignore alignment


    
free
(
p
[[
1
]
]
 
+
 
ggtitle
(
.ids
[
.
]
)
)
 


}
)
 
|>
 
wrap_plots
(
ncol
=
3
)
