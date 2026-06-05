names
(
bin
)
 
<-
 
bin
 
<-
 
c
(
"square_008um"
, 
"square_016um"
)


ncs
 
<-
 
lapply
(
bin
, \
(
um
)
 
{


    
ns
 
<-
 
lapply
(
spe
$
map
, \
(
df
)
 
unique
(
df
[[
um
]
]
)
)


    
as.vector
(
table
(
unlist
(
ns
)
)
)


}
)


sapply
(
ncs
, 
summary
)
