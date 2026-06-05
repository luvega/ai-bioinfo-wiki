library
(scater)


top <-
 
rownames
(vars)[
order
(vars
$
adjusted, 
decreasing=
TRUE
)[
1
]]


gridExtra
::
grid.arrange
(


    
plotExpression
(pbmc3k, 
x=
"label"
, 
features=
top) 
+
 
ggtitle
(
"3k"
),


    
plotExpression
(pbmc4k, 
x=
"label"
, 
features=
top) 
+
 
ggtitle
(
"4k"
),


    
ncol=
2


)
