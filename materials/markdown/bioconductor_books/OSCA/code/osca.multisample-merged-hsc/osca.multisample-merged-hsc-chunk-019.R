common.pseudo <-
 
averagePseudotime
(pseudo.out
$
ordering)


plotUMAP
(merged, 
colour_by=
I
(common.pseudo), 


        
text_by=
"label"
, 
text_colour=
"red"
) 
+


    
geom_line
(
data=
pseudo.out
$
connected
$
UMAP, 


        
mapping=
aes
(
x=
UMAP1, 
y=
UMAP2, 
group=
edge))
