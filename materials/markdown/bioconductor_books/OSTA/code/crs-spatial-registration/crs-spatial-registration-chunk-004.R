res
 
<-
 
7
 
# target resolution


px
 
<-
 
0.2125
 
# px size (um)


sf
 
<-
 
px
*
(
2
^
(
res
-
1
)
)
 
# scale factor


img
 
<-
 
RBioFormats
::
read.image
(


    
"morphology_mip.ome.tif"
, 


    resolution
=
res
)
