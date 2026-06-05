# average across cluster-level sender/receiver 


# averages to obtain i(nteraction) scores


ks
 
<-
 
expand.grid
(
ks
 
<-
 
colnames
(
mu
)
, 
ks
)


cs
 
<-
 
split
(
colnames
(
sce
)
, 
sce
$
Leiden
)


lr
 
<-
 
grepl
(
"-"
, 
rownames
(
sce
)
)


lr
 
<-
 
lr
 
&
 
!
grepl
(
"total"
, 
rownames
(
sce
)
)


ss
 
<-
 
strsplit
(
rownames
(
sce
)
, 
"-"
)


l
 
<-
 
sapply
(
ss
, 
.subset
, 
1
)


r
 
<-
 
sapply
(
ss
, 
.subset
, 
2
)


df
 
<-
 
mapply
(


    i
=
ks
[
, 
1
]
, j
=
ks
[
, 
2
]
,


    SIMPLIFY
=
FALSE
, \
(
i
, 
j
)
 
{


        
source
 
<-
 
sce
[
lr
, 
cs
[[
i
]
]
]


        
target
 
<-
 
sce
[
lr
, 
cs
[[
j
]
]
]


        
sr
 
<-
 
cbind
(


            
rowMeans
(
assay
(
source
, 
"s"
)
)
,


            
rowMeans
(
assay
(
target
, 
"r"
)
)
)


        
data.frame
(


            source
=
paste
(
i
)
, target
=
paste
(
j
)
,


            ligand
=
l
[
lr
]
, receptor
=
r
[
lr
]
,


            score
=
rowMeans
(
sr
)
)


    
}
)
 
|>
 
do.call
(
what
=
rbind
)


rownames
(
df
)
 
<-
 
NULL


head
(
df
)
