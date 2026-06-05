qcplots <-
 
list
()


for
 (n 
in
 
names
(all.sce)) {


    current <-
 
unfiltered[[n]]


    
colData
(current) <-
 
cbind
(
colData
(current), stats[[n]])


    current
$
discard <-
 
high.mito[[n]]


    qcplots[[n]] <-
 
plotColData
(current, 
x=
"sum"
, 
y=
"subsets_Mito_percent"
,


        
colour_by=
"discard"
) 
+
 
scale_x_log10
()


}


do.call
(gridExtra
::
grid.arrange, 
c
(qcplots, 
ncol=
3
))
