ks
 
<-
 
c
(
"Label"
, 
"Leiden"
, 
"Banksy"
)
#, "CellCharter")


lapply
(
ks
, \
(
.
)
 
{


    
plt
 
<-
 
plotCoords
(
spe
, annotate
=
.
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


}
)
 
|>


    
wrap_plots
(
nrow
=
2
)
 
&


    
scale_color_manual
(
values
=
unname
(
pals
::
trubetskoy
(
)
)
)
 
&


    
theme
(
legend.key.size
=
unit
(
0
, 
"lines"
)
, legend.justification
=
"left"
)
