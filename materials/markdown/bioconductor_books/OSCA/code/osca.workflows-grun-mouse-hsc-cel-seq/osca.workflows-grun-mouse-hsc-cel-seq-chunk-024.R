chosen <-
 
markers[[
'6'
]]


best <-
 
chosen[chosen
$
Top 
<=
 
10
,]


aucs <-
 
getMarkerEffects
(best, 
prefix=
"AUC"
)


rownames
(aucs) <-
 
best
$
SYMBOL




library
(pheatmap)


pheatmap
(aucs, 
color=
viridis
::
plasma
(
100
))
