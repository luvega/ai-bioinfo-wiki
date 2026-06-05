library
(cluster)


clust.col <-
 
scater
:::
.get_palette
(
"tableau10medium"
) 
# hidden scater colours


sil <-
 
silhouette
(my.clusters, 
dist =
 my.dist)


sil.cols <-
 
clust.col[
ifelse
(sil[,
3
] 
>
 
0
, sil[,
1
], sil[,
2
])]


sil.cols <-
 
sil.cols[
order
(
-
sil[,
1
], sil[,
3
])]


plot
(sil, 
main =
 
paste
(
length
(
unique
(my.clusters)), 
"clusters"
),


    
border=
sil.cols, 
col=
sil.cols, 
do.col.sort=
FALSE
)
