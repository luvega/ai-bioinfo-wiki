drop <-
 
sce.chimera
$
celltype.mapped 
%in%
 
c
(
"stripped"
, 
"Doublet"
)


sce.chimera <-
 
sce.chimera[,
!
drop]
