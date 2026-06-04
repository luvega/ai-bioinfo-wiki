markers <-
 
findMarkers
(sce.zeisel, 
direction=
"up"
)


marker.set <-
 
markers[[
"1"
]]


head
(marker.set[,
1
:
8
], 
10
) 
# only first 8 columns, for brevity
