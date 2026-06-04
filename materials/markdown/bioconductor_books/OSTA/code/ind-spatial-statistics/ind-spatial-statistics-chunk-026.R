# calculate LISA K curves


resLocal
 
<-
 
localK
(
ppSub
, verbose
=
FALSE
)
 




# code adapted from 


# https://robinsonlabuzh.github.io/


# pasta/01-imaging-univar-ppSOD.html


df
 
<-
 
resLocal
 
|>


    
as.data.frame
(
)
 
|>


    
pivot_longer
(


        
iso0001
:
iso1327
, 


        names_to
=
"curve"
)
 




sel
 
<-
 
df
 
|>


    
filter
(
r
 
>
 
700.5630
 
&
 
r
 
<
 
702.4388
)
 
|>


    
mutate
(
sel
=
value
)
 
|>
 


    
select
(
curve
, 
sel
)




df
 
<-
 
left_join
(
df
, 
sel
)




thm
 
<-
 
list
(


    
theme_light
(
)
,


    
theme
(
legend.position
=
"none"
)
,


    
scale_color_viridis_c
(
)
)




p
 
<-
 
ggplot
(
df
, 
aes
(
r
, 
value
, group
=
curve
, col
=
sel
)
)
 
+


    
geom_line
(
)
 
+


    
geom_line
(
aes
(
y
=
theo
)
, linetype
=
2
, col
=
"darkgray"
)
 
+


    
geom_vline
(
xintercept
=
700
)
 
+


    
thm




df
 
<-
 
data.frame
(


    x
=
ppSub
$
x
, y
=
ppSub
$
y
, 


    sel
=
unique
(
sel
)
$
sel
)




q
 
<-
 
ggplot
(
df
, 
aes
(
x
, 
y
, col
=
sel
)
)
 
+


    
coord_equal
(
expand
=
FALSE
)
 
+


    
geom_point
(
size
=
1
)
 
+
 


    
thm


 


p
 
|
 
q
