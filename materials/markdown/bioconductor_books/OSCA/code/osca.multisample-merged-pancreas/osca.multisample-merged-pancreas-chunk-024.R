donors.per.batch <-
 
split
(combined
$
donor, combined
$
batch)


donors.per.batch <-
 
lapply
(donors.per.batch, unique)


donors.per.batch
