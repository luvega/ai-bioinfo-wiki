lyz.high <-
 
c
(
"7"
, 
"8"
, 
"10"
, 
"12"
, 
"15"
, 
"18"
) 
# based on inspection of the previous Figure.


subset <-
 
chosen
$
full.AUC[,
colnames
(chosen
$
full.AUC) 
%in%
 
lyz.high]


to.show <-
 
subset[
computeMinRank
(subset) 
<=
 
10
,]


to.show
