# Applying cell type labels for downstream interpretation.


library
(SingleR)


training <-
 
sce.muraro[,
!
is.na
(sce.muraro
$
label)]


assignments <-
 
SingleR
(sce.grun, training, 
labels=
training
$
label)


sce.grun
$
label <-
 
assignments
$
labels


sce.grun
