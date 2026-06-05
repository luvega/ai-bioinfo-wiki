# set random seed for number generation


# in order to make results reproducible


set.seed
(
123
)


# sample 100 spots to decrease runtime in this demo


# (note: skip this step in full analysis)


n
 
<-
 
100


sub
 
<-
 
spe
[
, 
sample
(
ncol
(
spe
)
, 
100
)
]


# filter lowly expressed genes using stringent


# criteria to decrease runtime in this demo


# (note: use default criteria in full analysis)


sub
 
<-
 
filter_genes
(
sub
,     
# filter for genes with...


    filter_genes_ncounts
=
10
, 
# at least 10 counts in


    filter_genes_pcspots
=
3
)
  
# at least 3% of spots


# re-normalize counts post-filtering


sub
 
<-
 
logNormCounts
(
sub
)
