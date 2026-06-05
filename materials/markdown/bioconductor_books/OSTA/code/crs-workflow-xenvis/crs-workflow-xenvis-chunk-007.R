# simplify spatial coordinate names


spatialCoordsNames
(
vis
)
 
<-
 
spatialCoordsNames
(
xen
)
 
<-
 
c
(
"x"
, 
"y"
)


# use gene symbols as feature names


rownames
(
vis
)
 
<-
 
make.unique
(
rowData
(
vis
)
$
Symbol
)


rownames
(
xen
)
 
<-
 
make.unique
(
rowData
(
xen
)
$
Symbol
)
