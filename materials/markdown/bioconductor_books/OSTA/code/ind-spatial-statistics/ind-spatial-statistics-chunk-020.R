df
 
<-
 
.speToDf
(
sfe
)


pp
 
<-
 
.dfToppp
(
df
, marks
=
"Cluster"
)


plot
(
density
(
x
=
pp
, sigma
=
bw.diggle
)
)
