# subset data to features being considered


ss
 
<-
 
strsplit
(
db
$
receptor
, 
"_"
)


rs
 
<-
 
sapply
(
ss
, 
.subset
, 
1
)


sub
 
<-
 
spe
[
unique
(
c
(
db
$
ligand
, 
rs
)
)
, 
]




# assign spatial coordinates to 'spatial' 


# reduced dimension slot (required by 'COMMOT')


xy
 
<-
 
spatialCoords
(
sub
)


reducedDim
(
sub
, 
"spatial"
)
 
<-
 
xy




# get indices of cells that fall


# into a (2mm) x (2mm) window


cs
 
<-


    
xy
[
, 
1
]
 
>=
 
1500
 
&
 
xy
[
, 
1
]
 
<=
 
3500
 
&


    
xy
[
, 
2
]
 
>=
 
2000
 
&
 
xy
[
, 
2
]
 
<=
 
4000




# print number of genes x cells left


dim
(
sub
 
<-
 
sub
[
, 
cs
]
)
