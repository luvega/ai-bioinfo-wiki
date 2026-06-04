chosen <-
 
marker.info[[
"12"
]] 
# using another cluster, for some variety.


ordered <-
 
chosen[
order
(chosen
$
median.logFC.cohen,
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
