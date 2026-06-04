de.specific <-
 
pseudoBulkSpecific
(summed.filt,


    
label=
summed.filt
$
celltype.mapped,


    
design=
~
factor
(pool) 
+
 
tomato,


    
coef=
"tomatoTRUE"
,


    
condition=
summed.filt
$
tomato


)




cur.specific <-
 
de.specific[[
"Allantois"
]]


cur.specific <-
 
cur.specific[
order
(cur.specific
$
PValue),]


cur.specific
