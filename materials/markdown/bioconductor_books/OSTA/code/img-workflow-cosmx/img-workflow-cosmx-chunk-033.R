jc
 
<-
 
joincount.multi
(
sfe
$
SingleR_label
, 
colGraph
(
sfe
, 
"poly2nb"
)
, zero.policy
=
TRUE
)


head
(
jc
[
order
(
abs
(
jc
[
, 
"z-value"
]
)
, decreasing
=
TRUE
)
, 
]
)
