# set up environment using 'basilisk'


env
 
<-
 
BasiliskEnvironment
(


    pkgname
=
"base"
, 


    envname
=
"basilisk"
, 


    pip
=
"numpy==2.4.0"
,


    packages
=
"python=3.12"
)


# activate virtual environment


use_virtualenv
(
obtainEnvironmentPath
(
env
)
)
