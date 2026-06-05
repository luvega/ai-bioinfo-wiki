i
 
<-
 
match
(
vhd8
$
DeconLabel1
, 
sce
$
Level2
)


j
 
<-
 
match
(
vhd8
$
DeconLabel2
, 
sce
$
Level2
)


vhd8
$
.DeconLabel1
 
<-
 
sce
$
Level1
[
i
]


vhd8
$
.DeconLabel2
 
<-
 
sce
$
Level1
[
j
]


vhd8
 
<-
 
vhd8
[
, 
!
is.na
(
vhd8
$
.DeconLabel1
)
]


table
(
vhd8
$
.DeconLabel1
)
