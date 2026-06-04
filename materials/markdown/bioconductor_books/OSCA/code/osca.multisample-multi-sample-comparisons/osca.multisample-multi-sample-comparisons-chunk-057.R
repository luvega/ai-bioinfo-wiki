summed.sub <-
 
summed[,summed
$
celltype.mapped 
%in%
 
c
(
"Neural crest"
, 
"Notochord"
)]




# Using a dummy value for the label to allow us to include multiple cell types


# in the fitted model; otherwise, each cell type will be processed separately.


between.res <-
 
pseudoBulkDGE
(summed.sub,


    
label=
rep
(
"dummy"
, 
ncol
(summed.sub)),


    
design=
~
factor
(sample) 
+
 
celltype.mapped,


    
coef=
"celltype.mappedNotochord"
)[[
1
]]




table
(
Sig=
between.res
$
FDR 
<=
 
0.05
, 
Sign=
sign
(between.res
$
logFC))
