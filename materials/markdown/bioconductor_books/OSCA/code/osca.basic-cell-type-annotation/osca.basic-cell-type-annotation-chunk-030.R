muraro.mat <-
 
counts
(sce.muraro)


rownames
(muraro.mat) <-
 
rowData
(sce.muraro)
$
symbol


# Explicitly coerce count matrix to a dense matrix to avoid issues with 


# support for sparse matrices in AUCell.


muraro.rankings <-
 
AUCell_buildRankings
(
as.matrix
(muraro.mat),


    
plotStats=
FALSE
, 
verbose=
FALSE
)




# Applying MsigDB to the Muraro dataset, because it's human:


scsig.aucs <-
 
AUCell_calcAUC
(scsigs, muraro.rankings)


scsig.results <-
 
t
(
assay
(scsig.aucs))


full.labels <-
 
colnames
(scsig.results)[
max.col
(scsig.results)]


tab <-
 
table
(full.labels, sce.muraro
$
label)


fullheat <-
 
pheatmap
(
log10
(tab
+
10
), 
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




# Restricting to the subset of Muraro-derived gene sets:


scsigs.sub <-
 
scsigs[
grep
(
"Pancreas"
, 
names
(scsigs))]


sub.aucs <-
 
AUCell_calcAUC
(scsigs.sub, muraro.rankings)


sub.results <-
 
t
(
assay
(sub.aucs))


sub.labels <-
 
colnames
(sub.results)[
max.col
(sub.results)]


tab <-
 
table
(sub.labels, sce.muraro
$
label)


subheat <-
 
pheatmap
(
log10
(tab
+
10
), 
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
(fullheat[[
4
]], subheat[[
4
]])
