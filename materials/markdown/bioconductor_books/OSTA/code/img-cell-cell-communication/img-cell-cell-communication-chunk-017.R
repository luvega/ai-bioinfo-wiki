# construct SCE from CCC results;


# assays = s(ender) & r(eceiver)


as
 
<-
 
lapply
(
ccc
, \
(
.
)
 
{


    
names
(
.
)
 
<-
 
gsub
(
"^(s|r)-"
, 
""
, 
names
(
.
)
)


    
as
(
t
(
as.matrix
(
.
)
)
, 
"dgCMatrix"
)


}
)


(
sce
 
<-
 
SingleCellExperiment
(
as
, colData
=
colData
(
sub
)
)
)
