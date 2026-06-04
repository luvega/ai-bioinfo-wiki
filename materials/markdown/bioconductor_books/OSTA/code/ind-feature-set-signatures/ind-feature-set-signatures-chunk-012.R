cm
 
<-
 
cor
(
t
(
assay
(
auc
)
)
, method
=
"spearman"
)


pheatmap
(
cm
, 


    breaks
=
seq
(
-
1
, 
1
, 
0.1
)
, 


    color
=
pals
::
coolwarm
(
20
)
, 


    cellwidth
=
10
, cellheight
=
10
)
