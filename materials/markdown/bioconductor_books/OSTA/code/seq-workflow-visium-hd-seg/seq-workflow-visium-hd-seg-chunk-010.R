xy
 
<-
 
spatialCoords
(
spe
)


xs
 
<-
 
range
(
xy
[
, 
1
]
)


ys
 
<-
 
range
(
xy
[
, 
2
]
)


dx
 
<-
 
diff
(
xs
)
/
4


dy
 
<-
 
diff
(
ys
)
/
4


box
 
<-
 
list
(


    xmin
=
xs
[
1
]
+
dx
, xmax
=
xs
[
2
]
-
dx
,


    ymin
=
ys
[
1
]
+
dy
, ymax
=
ys
[
2
]
-
dy
)


sub
 
<-
 
.crop
(
spe
, 
box
)
