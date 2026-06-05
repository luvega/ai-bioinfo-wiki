# utility for cropping by bounding box


.crop
 
<-
 \
(
spe
, 
box
)
 
{


    
box
 
<-
 
as.list
(
box
)


    
xy
 
<-
 
spatialCoords
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
 
box
$
xmin
 
&
 
xy
[
,
1
]
 
<
 
box
$
xmax
 
&


        
xy
[
,
2
]
 
>
 
box
$
ymin
 
&
 
xy
[
,
2
]
 
<
 
box
$
ymax
 
]


}
