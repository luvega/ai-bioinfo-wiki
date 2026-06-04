library
(pheatmap)




# Using a large pseudo-count for a smoother color transition


# between 0 and 1 cell in each 'tab'.


tab <-
 
table
(
paste
(
"Infomap"
, clust.infomap), 


    
paste
(
"Walktrap"
, clust.walktrap))


ivw <-
 
pheatmap
(
log10
(tab
+
10
), 
main=
"Infomap vs Walktrap"
,


    
color=
viridis
::
viridis
(
100
), 
silent=
TRUE
)




tab <-
 
table
(
paste
(
"Fast"
, clust.fast), 


    
paste
(
"Walktrap"
, clust.walktrap))


fvw <-
 
pheatmap
(
log10
(tab
+
10
), 
main=
"Fast-greedy vs Walktrap"
,


    
color=
viridis
::
viridis
(
100
), 
silent=
TRUE
)




gridExtra
::
grid.arrange
(ivw[[
4
]], fvw[[
4
]])
