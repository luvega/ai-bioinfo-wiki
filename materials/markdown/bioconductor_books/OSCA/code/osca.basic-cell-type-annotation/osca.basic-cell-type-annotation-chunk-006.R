library
(SingleR)


pred <-
 
SingleR
(
test=
sce.pbmc, 
ref=
ref, 
labels=
ref
$
label.main)


table
(pred
$
labels)
