aggregated <-
 
sumCountsAcrossFeatures
(sce.mam, by.go,


    
exprs_values=
"logcounts"
, 
average=
TRUE
)


dim
(aggregated) 
# rows are gene sets, columns are cells
