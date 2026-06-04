is.hbb <-
 
grep
(
"^Hb[ab]-"
, 
rownames
(summed.neural))


ctrl.ambient <-
 
ambientContribNegative
(
counts
(summed.neural), ambient,


    
features=
is.hbb,  
mode=
"proportion"
)


head
(ctrl.ambient)
