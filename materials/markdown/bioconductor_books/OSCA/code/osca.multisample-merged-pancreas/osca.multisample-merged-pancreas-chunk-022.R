donors <-
 
c
(


    normed.pancreas
$
Grun
$
donor, 


    normed.pancreas
$
Muraro
$
donor,


    normed.pancreas
$
Lawlor
$
`
islet unos id
`
, 


    normed.pancreas
$
Seger
$
Donor


)




seger.donors <-
 
donors


seger.donors[mnn.pancreas
$
batch
!=
"Seger"
] <-
 
NA


plotTSNE
(mnn.pancreas, 
colour_by=
I
(seger.donors))
