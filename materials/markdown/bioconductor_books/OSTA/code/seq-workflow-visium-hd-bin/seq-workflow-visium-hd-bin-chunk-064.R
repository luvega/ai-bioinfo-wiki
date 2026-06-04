dbl
 
<-
 
vhd8
$
DeconClass
 
==
 
"doublet_certain"


lab
 
<-
 
c
(
".DeconLabel1"
, 
".DeconLabel2"
)


df
 
<-
 
data.frame
(
colData
(
vhd8
)
[
dbl
, 
lab
]
)


# sort as to ignore order


df
 
<-
 
apply
(
df
, 
1
, 
sort
)


df
 
<-
 
do.call
(
rbind
, 
df
)


names
(
df
)
 
<-
 
lab


# count unique pairs


ij
 
<-
 
paste
(
df
[
, 
1
]
, 
df
[
, 
2
]
, sep
=
";"
)


head
(
sort
(
table
(
ij
)
, decreasing
=
TRUE
)
, 
5
)
