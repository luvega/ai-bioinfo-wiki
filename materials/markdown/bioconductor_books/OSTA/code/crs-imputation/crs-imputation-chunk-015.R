# helper to perform PCR 


# xs = 'colData' to use as predictor(s)


# dr = 'reducedDim' slot to use as response


.pcr
 
<-
 \
(
obj
, 
xs
, 
dr
)
 
{


    
pcs
 
<-
 
reducedDim
(
obj
, 
dr
)


    
lapply
(
xs
, \
(
x
)
 
{


        
fit
 
<-
 
summary
(
lm
(
pcs
 
~
 
obj
[[
x
]
]
)
)


        
r2
 
<-
 
sapply
(
fit
, \
(
.
)
 
.
$
adj.r.squared
)


        
data.frame
(
x
, pc
=
seq_along
(
r2
)
, 
r2
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




# analysis


xs
 
<-
 
c
(
"sample_id"
, 
"Annotation"
)


pcs
 
<-
 
list
(
before
=
".PCA"
, after
=
"PCA"
)


pcr
 
<-
 
lapply
(
pcs
, \
(
dr
)
 
.pcr
(
obj
, 
xs
, 
dr
)
)




# wrangling


df
 
<-
 
bind_rows
(
pcr
, .id
=
"id"
)


df
$
id
 
<-
 
factor
(
df
$
id
, 
names
(
pcs
)
)


rownames
(
df
)
 
<-
 
NULL


head
(
df
)
