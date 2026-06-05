# check for availability of 'Statial';


# disable coming chunks if unavailable


run
 
<-
 
require
(
"Statial"
, quietly
=
TRUE
)


if
 
(
!
run
)
 
knitr
::
opts_chunk
$
set
(
eval
=
FALSE
)
