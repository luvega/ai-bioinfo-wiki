# keep only annotated bins


vhd8
 
<-
 
vhd8
[
, 
rownames
(
df
)
]


names
(
df
)
 
<-
 
c
(
"DeconClass"
, 
"DeconLabel1"
, 
"DeconLabel2"
)


colData
(
vhd8
)
[
names
(
df
)
]
 
<-
 
df
