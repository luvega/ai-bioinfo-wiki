res.tal1 <-
 
pseudoBulkSpecific
(summed.tal1, 


    
label=
summed.tal1
$
label,


    
design=
~
factor
(block) 
+
 
tomato,


    
coef=
"tomatoTRUE"
,


    
condition=
summed.tal1
$
tomato)




# Inspecting our neural crest results again.


tab.neural.again <-
 
res.tal1[[
"Neural crest"
]]


head
(tab.neural.again[
order
(tab.neural.again
$
PValue),], 
10
)
