chosen <-
 
marker.info[[
"5"
]]


ordered <-
 
chosen[
order
(chosen
$
mean.AUC, 
decreasing=
TRUE
),]


head
(ordered[,
1
:
4
]) 
# showing basic stats only, for brevity.
