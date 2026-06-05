lapply
(
c
(
"Leiden"
, 
"Level0"
, 
"Level1"
)
, \
(
.
)
 
{


    
pal
 
<-
 
if
 
(
.
 
==
 
"Level0"
)
 
{


        
c
(
"gold"
, 
"cyan"
, 
"magenta"
, 
"black"
)


    
}
 
else
 
{


        
hcl.colors
(
nlevels
(
sub
[[
.
]
]
)
, 
"Spectral"
)


    
}


    
.plt_xy
(
sub
, 
.
)
 
+
 
scale_color_manual
(
values
=
pal
)
 


}
)
 
|>
 
wrap_plots
(
)
