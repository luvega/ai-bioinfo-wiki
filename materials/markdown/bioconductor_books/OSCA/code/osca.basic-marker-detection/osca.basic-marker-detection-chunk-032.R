marker.info.lfc <-
 
scoreMarkers
(sce.pbmc, 
colLabels
(sce.pbmc), 
lfc=
2
)


chosen2 <-
 
marker.info.lfc[[
"4"
]] 
# another cluster for some variety.


chosen2 <-
 
chosen2[
order
(chosen2
$
mean.AUC, 
decreasing=
TRUE
),]


chosen2[,
c
(
"self.average"
, 
"other.average"
, 
"mean.AUC"
)]
