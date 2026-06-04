top.markers <-
 
rownames
(marker.set)[marker.set
$
Top 
<=
 
10
]


plotHeatmap
(sce.zeisel, 
features=
top.markers, 
order_columns_by=
"label"
)
