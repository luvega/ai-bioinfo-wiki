okay.genes <-
 
names
(ctrl.non.ambient)[
which
(ctrl.non.ambient)]


tab.neural4 <-
 
tab.neural[
rownames
(tab.neural) 
%in%
 
okay.genes,]


head
(tab.neural4)
