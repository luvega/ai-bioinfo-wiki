proxy.ambient <-
 
aggregateAcrossCells
(summed.tal1,


    
ids=
summed.tal1
$
sample)




# Using 'proxy.ambient' instead of the estimaed 'ambient'.


max.ambient.proxy <-
 
ambientContribMaximum
(
counts
(summed.neural), 


    
counts
(proxy.ambient), 
mode=
"proportion"
)


head
(max.ambient.proxy)
