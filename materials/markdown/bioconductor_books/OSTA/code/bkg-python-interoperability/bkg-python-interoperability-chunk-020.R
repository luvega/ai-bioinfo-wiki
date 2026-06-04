# get image metadata


imgdata
 
<-
 
imgData
(
spe
)




# get image


img
 
<-
 
imgRaster
(
spe
)


img
 
<-
 
apply
(
img
, 
c
(
1
, 
2
)
, \
(
x
)
 
col2rgb
(
x
)
)


img
 
<-
 
aperm
(
img
, perm
=
c
(
2
, 
3
, 
1
)
)


img
 
<-
 
img
 
/
 
255




# create uns


uns
 
<-
 
list
(
images
=
list
(
lowres
=
img
)
, scalefactors
=
sfs
)


uns
 
<-
 
list
(
spatial
=
setNames
(
list
(
uns
)
, 
imgdata
$
sample_id
)
)
