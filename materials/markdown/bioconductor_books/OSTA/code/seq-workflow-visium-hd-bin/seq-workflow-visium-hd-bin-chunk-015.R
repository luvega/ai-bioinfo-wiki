# helper for subsetting


.sub
 
<-
 
function
(
spe
, 
rng
, 
roi
=
"box"
)
 
{


    
xs
 
<-
 
rng
[[
roi
]
]
[
c
(
1
, 
2
)
]


    
ys
 
<-
 
nrow
(
imgRaster
(
spe
)
)
 
-
 
rng
[[
roi
]
]
[
c
(
3
,
4
)
]


    
xy
 
<-
 
spatialCoords
(
spe
)
*
scaleFactors
(
spe
)


    
spe
[
, 
xy
[
, 
1
]
 
>
 
xs
[
1
]
 
&
 
xy
[
, 
1
]
 
<
 
xs
[
2
]
 
&
 


          
xy
[
, 
2
]
 
>
 
ys
[
1
]
 
&
 
xy
[
, 
2
]
 
<
 
ys
[
2
]
 
]


}
