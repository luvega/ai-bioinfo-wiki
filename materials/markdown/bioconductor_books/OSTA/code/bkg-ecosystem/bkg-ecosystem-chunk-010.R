gg
 
<-
 
lapply
(
ids
, \
(
id
)
 
{


    
nm
 
<-
 
df
$
Package
[
.f
(
id
)
]


    
ys
 
<-
 
BiocPkgTools
:::
getPkgYearsInBioc
(
nm
)


}
)
 
|>
 
bind_rows
(
.id
=
"biocViews"
)
 
|>


    
mutate
(
years
=
approx_years_in
)
 
|>


    
filter
(
!
is.na
(
years
)
)


mu
 
<-
 
gg
 
|>


    
group_by
(
biocViews
)
 
|>


    
summarise_at
(
"years"
, 
mean
)


# print


cat
(
"years in Bioconductor:\n"
)


summary
(
gg
$
approx_years_in
)


# plot


ggplot
(
gg
, 
aes
(
years
, fill
=
biocViews
)
)
 
+
 


    
geom_histogram
(
alpha
=
1
/
3
, binwidth
=
0.5
)
 
+


    
geom_vline
(


        linewidth
=
1
, data
=
mu
,


        
aes
(
xintercept
=
years
, col
=
biocViews
)
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
100
, 
2
)
)
 
+


    
labs
(
x
=
"lifetime (years)"
, y
=
"# packages"
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
