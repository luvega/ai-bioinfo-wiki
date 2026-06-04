# subset to only Invasive tumor cells 


ppSub
 
<-
 
subset
(
pp
, 
marks
 
%in%
 
"Invasive_Tumor"
)


# restrict to a smaller window for computational reasons


Window
(
ppSub
)
 
<-
 
owin
(
c
(
3500
, 
7524.087
)
, 
c
(
1200
, 
5475.691
)
)


# plot the point pattern


plot
(
ppSub
)
