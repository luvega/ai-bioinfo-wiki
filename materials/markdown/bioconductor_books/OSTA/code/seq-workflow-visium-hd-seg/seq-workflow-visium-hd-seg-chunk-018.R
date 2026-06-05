# specify bounding box


box
 
<-
 
c
(


    xmin
=
56e3
, xmax
=
58e3
, 


    ymin
=
15e3
, ymax
=
16e3
)


# plot exemplary cell masks


geo
 
<-
 
colGeometry
(
crop
(
sfe
, 
box
)
)


plot
(
st_geometry
(
geo
)
, col
=
rep
(
colors
(
)
, 
2
)
)
