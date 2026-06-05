# tabulate # and % of cells discarded 


# due to few counts/detected features


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
