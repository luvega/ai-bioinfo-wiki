es
 
<-
 
t
(
as.matrix
(
logcounts
(
sub
)
)
)


df
 
<-
 
data.frame
(
colData
(
sub
)
, 
es
)


ggplot
(
df
, 
aes
(
CXCL12
, 
s.CXCL12.CXCR4
)
)
 
+
 


ggplot
(
df
, 
aes
(
CXCR4
, 
r.CXCL12.CXCR4
)
)
 
+
 


    
plot_layout
(
nrow
=
1
)
 
&


    
geom_point
(
shape
=
16
, stroke
=
0
, size
=
1
, alpha
=
0.2
)
 
&


    
geom_abline
(
intercept
=
0
, slope
=
1
, linewidth
=
0.4
, col
=
"red"
)
 
&


    
coord_equal
(
)
 
&
 
theme_bw
(
)
 
&
 
theme
(
panel.grid.minor
=
element_blank
(
)
)
