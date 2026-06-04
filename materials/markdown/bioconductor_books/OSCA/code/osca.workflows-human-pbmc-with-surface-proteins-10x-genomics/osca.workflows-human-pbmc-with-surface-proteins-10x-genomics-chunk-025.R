data.frame
(


    
Cluster=
names
(subclusters),


    
Ncells=
vapply
(subclusters, ncol, 0L),


    
Nsub=
vapply
(subclusters, 
function
(x) 
length
(
unique
(x
$
subcluster)), 0L)


)
