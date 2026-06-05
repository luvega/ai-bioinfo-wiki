gg
 
<-
 
lapply
(
i
, \
(
i
)
 
{


    
lapply
(
seq_along
(
j
)
, \
(
n
)
 
{


        
js
 
<-
 
combn
(
j
, 
n
, simplify
=
FALSE
)


        
lapply
(
js
, \
(
j
)
 
{


            
n
 
<-
 
sum
(
.f
(
c
(
i
, 
j
)
)
)


            
j
 
<-
 
gsub
(
"[a-z]"
, 
""
, 
j
)


            
j
 
<-
 
paste
(
j
, collapse
=
"+"
)


            
data.frame
(
i
, 
j
, 
n
)


        
}
)
 
|>
 
do.call
(
what
=
rbind
)


    
}
)
 
|>
 
do.call
(
what
=
rbind
)


}
)
 
|>
 
do.call
(
what
=
rbind
)
 
|>


    
group_by
(
j
)
 
|>


    
summarize_at
(
"n"
, 
sum
)
 
|>


    
slice_max
(
n
, n
=
30
)


yo
 
<-
 
gg
$
j
[
order
(
gg
$
n
)
]


ggplot
(
gg
, 
aes
(
n
, 
j
)
)
 
+
 


    
geom_col
(
alpha
=
1
/
3
, fill
=
"blue"
)
 
+


    
labs
(
y
=
NULL
, x
=
"# packages"
)
 
+


    
scale_y_discrete
(
limits
=
yo
)
 
+


    
theme_bw
(
)
 
+
 
theme
(


        aspect.ratio
=
1
, 


        panel.grid.minor
=
element_blank
(
)
,


        axis.text.x
=
element_text
(
angle
=
45
, hjust
=
1
)
)
