plotGroupedHeatmap
(sce.pbmc[,
colLabels
(sce.pbmc) 
%in%
 
lyz.high],


    
features=
rownames
(to.show), 
group=
"label"
, 
center=
TRUE
, 
zlim=
c
(
-
3
, 
3
))
