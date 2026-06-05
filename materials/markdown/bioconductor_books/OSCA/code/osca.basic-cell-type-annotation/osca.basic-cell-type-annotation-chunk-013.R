# Pruning out unknown or unclear labels.


sce.muraro <-
 
sce.muraro[,
!
is.na
(sce.muraro
$
label) 
&
 


    
sce.muraro
$
label
!=
"unclear"
]


table
(sce.muraro
$
label)
