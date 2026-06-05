k.stats <-
 
khclust.info
$
objects
$
first


tree.pbmc <-
 
khclust.info
$
objects
$
second
$
hclust




m <-
 
match
(
as.integer
(tree.pbmc
$
labels), k.stats
$
cluster)


final.clusters <-
 
khclust.info
$
clusters[m]




# 
TODO
: expose scater color palette for easier re-use,


# given that the default colors start getting recycled.


dend <-
 
as.dendrogram
(tree.pbmc, 
hang=
0.1
)


labels_colors
(dend) <-
 
as.integer
(final.clusters)[
order.dendrogram
(dend)]




plot
(dend)
