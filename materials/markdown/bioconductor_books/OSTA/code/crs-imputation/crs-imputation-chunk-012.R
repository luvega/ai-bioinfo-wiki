cd
 
<-
 
intersect
(
names
(
colData
(
spe
)
)
, 
names
(
colData
(
sce
)
)
)


obj
 
<-
 
lapply
(
list
(
spe
, 
sce
)
, \
(
x
)
 
{


    
y
 
<-
 
logcounts
(
x
 
<-
 
x
[
gs
, 
]
)


    
y
 
<-
 
as
(
y
, 
"dgCMatrix"
)


    
SingleCellExperiment
(


        assays
=
list
(
logcounts
=
y
)
,


        colData
=
colData
(
x
)
[
cd
]
)


}
)
 
|>
 
do.call
(
what
=
cbind
)


# add single-cell annotations


lab
 
<-
 
match
(
colnames
(
obj
)
, 
colnames
(
sce
)
)


obj
$
Annotation
 
<-
 
sce
$
Annotation
[
lab
]
