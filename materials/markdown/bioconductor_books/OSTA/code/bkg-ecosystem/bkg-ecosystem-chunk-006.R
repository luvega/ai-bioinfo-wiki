# dependencies


library
(
dplyr
)


library
(
ggplot2
)


# specify 'biocViews' of interest


names
(
ids
)
 
<-
 
ids
 
<-
 
c
(
"SingleCell"
, 
"Spatial"
)


now
 
<-
 
as.Date
(
format
(
Sys.Date
(
)
, 
"%Y-%m-%d"
)
)


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


    
# get metadata & simplify naming


    
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
 
getPkgYearsInBioc
(
nm
)
 
|>


        
mutate
(
first
=
first_version_release_date
)
 
|>


        
mutate
(
last
=
last_version_release_date
)
 
|>


        
mutate
(
last
=
case_when
(
is.na
(
last
)
~
now
, 
TRUE
~
last
)
)
 
|>


        
filter
(
!
is.na
(
first
)
)


    
# complete months between first/last dates


    
ys
 
<-
 
lapply
(
split
(
ys
, 
ys
$
package
)
, \
(
.
)
 
{


        
data.frame
(


            package
=
.
$
package
, 


            date
=
seq
(
.
$
first
, 
.
$
last
)
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
 


    
# get cumulative number of packages available each month


    
ys
 
|>
 
group_by
(
date
)
 
|>
 
count
(
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
