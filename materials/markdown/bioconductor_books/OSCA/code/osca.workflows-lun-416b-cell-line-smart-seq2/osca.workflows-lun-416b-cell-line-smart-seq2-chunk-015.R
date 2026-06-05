library
(limma)


assay
(sce
.416
b, 
"corrected"
) <-
 
removeBatchEffect
(
logcounts
(sce
.416
b), 


    
design=
model.matrix
(
~
sce
.416
b
$
phenotype), 
batch=
sce
.416
b
$
block)
