tif
 
<-
 
"GSM7780153_Post-Xenium_HE_Rep1.ome.tif"


img
 
<-
 
RBioFormats
::
read.image
(
tif
, resolution
=
7
)


png
 
<-
 
"Xenium_H&E_res7.png"


EBImage
::
writeImage
(
tif
, files
=
png
, type
=
"png"
)
