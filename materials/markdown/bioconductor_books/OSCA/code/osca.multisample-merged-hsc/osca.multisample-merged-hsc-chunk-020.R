pseudo.out2 <-
 
quickPseudotime
(merged, 
use.dimred=
"corrected"
, 


    
dist.method=
"mnn"
, 
outgroup=
TRUE
)




common.pseudo2 <-
 
averagePseudotime
(pseudo.out2
$
ordering)


plotUMAP
(merged, 
colour_by=
I
(common.pseudo2), 


        
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
pseudo.out2
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
