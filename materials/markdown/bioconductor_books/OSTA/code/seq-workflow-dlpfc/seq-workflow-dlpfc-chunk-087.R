# if we had spots with no counts, we would remove them


if
 
(
any
(
spe
$
sum_umi
 
==
 
0
)
)
 
{


    
spots_no_counts
 
<-
 
which
(
spe
$
sum_umi
 
==
 
0
)


    
# number of spots with no counts


    
print
(
length
(
spots_no_counts
)
)


    
# percent of spots with no counts


    
print
(
length
(
spots_no_counts
)
 
/
 
ncol
(
spe
)
 
*
 
100
)


    
spe
 
<-
 
spe
[
, 
-
spots_no_counts
, drop
=
FALSE
]


}
