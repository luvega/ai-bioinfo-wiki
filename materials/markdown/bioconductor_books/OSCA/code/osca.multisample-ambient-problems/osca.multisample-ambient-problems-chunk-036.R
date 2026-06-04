scaled.ambient <-
 
controlAmbience
(
counts
(summed.neural), ambient,


    
features=
is.hbb,  
mode=
"profile"
)


subtracted <-
 
counts
(summed.neural) 
-
 
scaled.ambient


subtracted <-
 
round
(subtracted)


subtracted[subtracted 
<
 
0
] <-
 
0


subtracted[is.hbb,]
