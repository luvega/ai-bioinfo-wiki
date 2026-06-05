# Making a copy and pretending it's a different sample,


# for demonstration purposes.


# 
TODO
: actually get a different sample.


target <-
 
paste0
(fpath, 
'-2'
)


unlink
(target)




if
 (.Platform
$
OS.type
==
"windows"
) {


    
file.copy
(fpath, target)


} 
else
 {


    
file.symlink
(fpath, target)


}
