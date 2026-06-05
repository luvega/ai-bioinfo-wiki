# realize delayed matrices, as CARD does 


# not yet support delayed matrix handling


counts
(
sce
)
 
<-
 
as
(
counts
(
sce
)
, 
"sparseMatrix"
)


counts
(
vis
)
 
<-
 
as
(
counts
(
vis
)
, 
"sparseMatrix"
)


colnames
(
spatialCoords
(
vis
)
)
 
<-
 
c
(
"x"
, 
"y"
)
