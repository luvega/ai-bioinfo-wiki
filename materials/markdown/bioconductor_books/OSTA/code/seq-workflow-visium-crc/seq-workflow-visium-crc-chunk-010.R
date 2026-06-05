# add results as cell metadata


colData
(
spe
)
[
names
(
ol
)
]
 
<-
 
ol
 


# tabulate # and % of cells that'd 


# be discarded for different reasons


data.frame
(


    check.names
=
FALSE
,


    `#`
=
apply
(
ol
, 
2
, 
sum
)
, 


    `%`
=
round
(
100
*
apply
(
ol
, 
2
, 
mean
)
, 
2
)
)
