# plot selected clusters in order of frequency,


# highlighting cells assigned to cluster 'k'


lapply
(
tail
(
names
(
sort
(
table
(
spe
$
Banksy
)
)
)
, 
12
)
, \
(
k
)
 
{


    
spe
$
foo
 
<-
 
spe
$
Banksy
 
==
 
k


    
spe
 
<-
 
spe
[
, 
order
(
spe
$
foo
)
]


    
plt
 
<-
 
plotCoords
(
spe
, annotate
=
"foo"
)


    
plt
$
layers
[[
1
]
]
$
aes_params
$
stroke
 
<-
 
0


    
plt
$
layers
[[
1
]
]
$
aes_params
$
size
 
<-
 
0.2


    
plt
 
+
 
ggtitle
(
k
)


}
)
 
|>


    
wrap_plots
(
nrow
=
3
)
 
&


    
scale_color_manual
(
values
=
c
(
"lavender"
, 
"purple"
)
)
 
&


    
theme
(
plot.title
=
element_text
(
hjust
=
0.5
)
, legend.position
=
"none"
)
