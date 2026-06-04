# compute standard scRNA-seq QC metrics for the Xenium dataset (e.g.,


# total counts & unique features, for RNA targets & negative probes)


xen
 
<-
 
addPerCellQCMetrics
(
xen
, use.altexps
=
TRUE
)
