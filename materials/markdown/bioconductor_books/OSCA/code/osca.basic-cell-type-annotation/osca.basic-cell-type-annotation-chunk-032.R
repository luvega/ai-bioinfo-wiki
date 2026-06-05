markers.mam <-
 
scoreMarkers
(sce.mam, 
lfc=
1
)




chosen <-
 "2"


cur.markers <-
 
markers.mam[[chosen]]


is.de <-
 
order
(cur.markers
$
median.logFC.cohen, 
decreasing=
TRUE
)[
1
:
100
]


cur.markers[is.de,
1
:
4
]
