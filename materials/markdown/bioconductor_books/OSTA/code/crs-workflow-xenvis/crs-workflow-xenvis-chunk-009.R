# stash original coordinates


old
 
<-
 
spatialCoords
(
xen
)


colData
(
xen
)
[
c
(
".x"
, 
".y"
)
]
 
<-
 
old


# apply affine transformation


new
 
<-
 
old
 
%*%
 
t
(
mtx
[
, 
-
3
]
)
 
# scale/rotate &


new
 
<-
 
sweep
(
new
, 
2
, 
mtx
[
, 
3
]
, 
`+`
)
 
# offset


spatialCoords
(
xen
)
 
<-
 
new
