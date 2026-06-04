n8
 
<-
 
table
(
.vhd8
$
.DeconLabel1
)


n16
 
<-
 
table
(
.vhd16
$
.DeconLabel1
)


df
 
<-
 
data.frame
(
x
=
as.numeric
(
n8
/
n16
)
)


ggplot
(
df
, 
aes
(
x
)
)
 
+
 
geom_density
(
)
 
+
 


    
xlab
(
"Cell type frequency ratio"
)
 
+
 


    
ggtitle
(
"distribution of cell type frequency\nratio between 8 vs. 16 µm bins"
)
 
+
 


    
scale_x_continuous
(
breaks
=
seq
(
0
, 
max
(
df
$
x
)
, by
=
2
)
)
 
+
 


    
theme_classic
(
)
 
+
 
theme
(
plot.title
=
element_text
(
hjust
=
0.5
)
)
