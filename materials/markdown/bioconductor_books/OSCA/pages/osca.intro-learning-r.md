---
source: OSCA
title: "Introduction to Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.intro/learning-r.html
ingested_at: 2026-06-04T01:52:47+00:00
status: source_ingested
---

# [Introduction to Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.intro/)

# Chapter 2 Learning R

## 2.1 Links to R tutorials

There are many, many online resources available for learning how to use R.
To name a few:

* The [R for data science book](https://r4ds.had.co.nz/), which is a fairly enjoyable read
  though it focuses heavily on a specific dialect of the R language.
* A [free course from Codecademy](https://www.codecademy.com/learn/learn-r),
  which uses a web-based console; this allows people to start learning without actually installing R on their own computers.
* A [free course from EdX](https://www.edx.org/course/statistics-and-r),
  which focuses on the use of R’s statistical functionality.
* [An Introduction to R](https://cran.r-project.org/doc/manuals/R-intro.pdf),
  a definitive description of R that is best read after some basic familiarity has been established.

We will not attempt to repeat the contents of these resources here, as they already do a good job of explaining themselves.

## 2.2 Code formatting

This book contains code chunks interspersed with results, plots and explanatory text.
Code chunks contain R code that is to be evaluated, and interested readers can copy-paste these lines into the R console to try it out themselves.
Each code chunk looks like this:

```
a <- 2 * 5
print(a)
```

Terms are colored differently depending on their category - this is mostly aesthetic and can be ignored for the time being.
If a code chunk produces any visible output, it is shown in another chunk like so:

```
## [1] 10
```

Alternatively, as a figure:

```
plot(1:10, 1:10, pch=16, main="I am a figure")
```

![](../../../../raw/bioconductor_books/assets/OSCA/osca.intro-learning-r/unnamed-chunk-3-1.png)

Any text after a `#` is considered a comment and is ignored when running the code.
The content of output chunks is always prefixed with `#` so that users can just copy-paste sections of code without having to explicitly remove the lines containing the results.

In some chapters, chunks may also be hidden in collapsible boxes.
This usually contains code to set up objects for later steps but is otherwise not particularly interesting (e.g., downloading files, formatting data),
and so is hidden to avoid distracting the reader.

Click me!

```
message <- "I am hidden!"
```

All chapters will finish with a printout of the session information.
This describes the system on which the chapter was compiled and the versions of all packages that were used,
which is useful for reproducing old results and diagnosing changes due to package updates.

## 2.3 Getting help

If you have a question about how a function works, it can often be answered by the function’s documentation.
This is accessible by prepending the function name with `?`.

More general questions on how to use a package may be answered by the package’s vignette, if it is available.
(One aspect of Bioconductor software that distinguishes it from CRAN packages is the required documentation of packages and workflows.)

```
vignette(package='SingleCellExperiment') # list all available vignettes
vignette(package='SingleCellExperiment', topic='intro') # open specific vignette
```

Beyond the R console, there are myriad online resources to get help.
The R for Data Science book has a great section dedicated to looking for help [outside of R](https://r4ds.had.co.nz/introduction.html#getting-help-and-learning-more).
For example, [Stack Overflow’s R tag](https://stackoverflow.com/questions/tagged/r) is a helpful resource for asking and exploring general R programming questions.

For Bioconductor specifically, the [support site](https://support.bioconductor.org/) contains a question and answer-style support site that is actively updated by both users and package developers.
This should generally be the first port of call for questions that are not answered by any existing documentation.

Users can also connect to the Bioconductor community through [our Slack group](https://bioc-community.herokuapp.com), which hosts various channels dedicated to packages and workflows.
The Bioc-community Slack is a great way to stay in the loop on the latest developments happening across Bioconductor, and we recommend exploring the “Channels” section to find topics of interest.

## 2.4 Beyond the basics

Once comfortable with the basic concepts of the language, we take things to the next level:

* [Advanced R](https://adv-r.hadley.nz/), as its name suggests, goes through some of the more advanced concepts in the language.
* The aptly named [What They Forgot to Teach You About R](https://rstats.wtf/) discusses topics such as file naming, maintaining an R installation, and reproducible analysis habits.
* The [R Inferno](https://www.burns-stat.com/pages/Tutor/R_inferno.pdf) dives into many of the unique quirks of R and some of the common user mistakes.
* [Happy Git and Github for the useR](https://happygitwithr.com/), which describes how to use the Git version control system with R.

Over time, you may accumulate a collection of your own functions that you might want to re-use across projects or even share with other people.
This can be done easily by creating your own R package.
The [R Packages book](http://r-pkgs.had.co.nz/) provides a user-friendly guide for doing so;
more experienced developers will consult [Writing R extensions](https://cran.r-project.org/doc/manuals/r-release/R-exts.html), the definitive documentation for the R packaging system.
Bioconductor itself also provides [some educational resources](https://www.bioconductor.org/developers/) for package development within the Bioconductor context.

## Session Info

View session info

```
R version 4.6.0 RC (2026-04-17 r89917)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /home/biocbuild/bbs-3.23-bioc/R/lib/libRblas.so 
LAPACK: /usr/lib/x86_64-linux-gnu/lapack/liblapack.so.3.12.0  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_GB              LC_COLLATE=C              
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: America/New_York
tzcode source: system (glibc)

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base     

other attached packages:
[1] BiocStyle_2.40.0 rebook_1.22.0   

loaded via a namespace (and not attached):
 [1] cli_3.6.6           knitr_1.51          rlang_1.2.0        
 [4] xfun_0.57           otel_0.2.0          generics_0.1.4     
 [7] CodeDepends_0.6.7   jsonlite_2.0.0      dir.expiry_1.20.0  
[10] htmltools_0.5.9     XML_3.99-0.23       graph_1.90.0       
[13] sass_0.4.10         stats4_4.6.0        rmarkdown_2.31     
[16] filelock_1.0.3      evaluate_1.0.5      jquerylib_0.1.4    
[19] fastmap_1.2.0       yaml_2.3.12         lifecycle_1.0.5    
[22] bookdown_0.46       BiocManager_1.30.27 compiler_4.6.0     
[25] codetools_0.2-20    digest_0.6.39       R6_2.6.1           
[28] bslib_0.10.0        tools_4.6.0         BiocGenerics_0.58.0
[31] cachem_1.1.0
```
