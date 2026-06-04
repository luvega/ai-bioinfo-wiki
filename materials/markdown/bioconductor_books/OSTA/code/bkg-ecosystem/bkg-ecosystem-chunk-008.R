# fit linear model where x = 'date', y = # packages


# (starting at 'date' where at least 5 packages exist)


dy
 
<-
 
round
(
as.integer
(
diff
(
slice_min
(
group_by
(
.gg
, 
biocViews
)
, 
date
)
$
date
)
)
/
365
, 
2
)


(
bs
 
<-
 
.gg
 
|>


    
group_by
(
biocViews
)
 
|>


    
group_split
(
)
 
|>


    
# return coefficients = # packages 


    
# added each month (on average)


    
sapply
(
\
(
.
)
 
coef
(
lm
(
n
~
date
, 
.
)
)
[[
2
]
]
)
 
|>


    
setNames
(
sort
(
unique
(
gg
$
biocViews
)
)
)
)
