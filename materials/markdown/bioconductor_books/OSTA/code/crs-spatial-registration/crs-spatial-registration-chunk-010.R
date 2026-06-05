img
 
<-
 
imgRaster
(
xen
)


xy
 
<-
 
spatialCoords
(
xen
)


xy
 
<-
 
xy
*
scaleFactors
(
xen
)


xy
[
, 
2
]
 
<-
 
nrow
(
img
)
 
-
 
xy
[
, 
2
]


xy_reg
 
<-
 
t
(
mtx
 
%*%
 
rbind
(
t
(
xy
)
, 
1
)
)


xy_reg
 
<-
 
xy_reg
[
, 
-
3
]


colnames
(
xy_reg
)
 
<-
 
colnames
(
spatialCoords
(
xen
)
)


# create a dataset copy with new coordinates


reg
 
<-
 
xen


imgData
(
reg
)
 
<-
 
NULL


spatialCoords
(
reg
)
 
<-
 
xy_reg
