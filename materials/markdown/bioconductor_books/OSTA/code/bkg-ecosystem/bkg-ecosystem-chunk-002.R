# retrieve current package record


df
 
<-
 
biocPkgList
(
)


# helper function to get indices of packages


# that contain 'biocViews' specified by 'x'


.f
 
<-
 \
(
x
, 
y
=
df
)
 
vapply
(
y
$
biocViews
, \
(
.
)
 
all
(
x
 
%in%
 
.
)
, 
logical
(
1
)
)


# view "Spatial" packages


df
$
Package
[
.f
(
"Spatial"
)
]
