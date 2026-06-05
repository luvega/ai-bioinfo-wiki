roi
 
<-
 
c
(
xmin
=
54e3
, xmax
=
58e3
, ymin
=
12e3
, ymax
=
16e3
)


spe
$
roi
 
<-
 
colnames
(
spe
)
 
%in%
 
colnames
(
.crop
(
spe
, 
roi
)
)


plotCoords
(
spe
, annotate
=
"roi"
, point_size
=
0
)
 
+
 
theme
(
legend.position
=
"none"
)
