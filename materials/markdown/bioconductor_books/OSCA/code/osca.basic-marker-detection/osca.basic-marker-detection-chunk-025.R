marker.info <-
 
scoreMarkers
(sce.pbmc, 
colLabels
(sce.pbmc), 
full.stats=
TRUE
)


chosen <-
 
marker.info[[
"12"
]]


chosen
$
full.AUC
