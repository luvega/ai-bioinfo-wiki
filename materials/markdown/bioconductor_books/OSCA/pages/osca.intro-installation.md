---
source: OSCA
title: "Introduction to Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.intro/installation.html
ingested_at: 2026-06-04T01:52:38+00:00
status: source_ingested
---

# [Introduction to Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.intro/)

# Chapter 1 Installation

## 1.1 Overview

So, you want to be the very best, like no one ever wa– oh wait, wrong tutorial.
So, you want to learn how to do single-cell RNA-seq data analyses with Bioconductor?
This chapter will describe the very first step in this process: getting up and running with a R/Bioconductor installation on your local computer.
If you already know how to do this, or are using a centrally-managed installation (e.g., on a institutional server), feel free to skip ahead to the next chapter.

What is R, anyway?
R is a [high-level programming language](https://www.r-project.org/about.html) that provides an integrated environment for analyzing all kinds of data.
One of its key advantages is the ease with which it can be extended via *packages*.
For example, some of these packages implement statistical/computational methods (e.g., *[lme4](https://CRAN.R-project.org/package=lme4)* for mixed effect modelling),
while other packages provide programming utilities for general use (e.g., *[ggplot2](https://CRAN.R-project.org/package=ggplot2)* for visualization).
The diverse package ecosystem provides R with the capabilities needed to develop useful applications and answer important scientific questions across many fields of study.

Within this ecosystem, the Bioconductor project provides tools for the analysis and comprehension of high-throughput genomics data.
The scope of the project covers microarray data, various forms of sequencing (RNA-seq, ChIP-seq, bisulfite, genotyping, etc.), proteomics, flow cytometry and more.
One of Bioconductor’s main selling points is the use of common data structures to promote interoperability between packages,
allowing code written by different people (from different organizations, in different countries) to work together seamlessly in complex analyses.
By extending R to genomics, Bioconductor serves as a powerful addition to the computational biologist’s toolkit.

## 1.2 Installing software

Our first task is to get R installed on our computer by following the instructions at <https://www.r-project.org>.
In brief: we select a local mirror from <https://cran.r-project.org/mirrors.html> and then we choose the appropriate link in *“Download R for…”* for our operating system.
This will download installers for Mac OS X and Windows, which can be opened and run in the usual way.
For Linux, the link provides distribution-specific instructions that uses the relevant package manager - for example:

```
sudo apt-get install r-base # Debian/Ubuntu
sudo dnf install R # Fedora/CentOS/RHEL
sudo yum install R # older Fedora/CentOS/RHEL
```

Users of Homebrew can also do:

```
brew install R
```

We suggest installing the latest version of R to ensure that you have access to the most up-to-date functionality and bugfixes.
For example, this book’s contents were generated using R 4.6,
which is the version that should be installed if you want to reproduce the results shown in later chapters.

For most users, we also recommend installing a graphical user interface such as [RStudio](http://www.rstudio.com/download).
This features many helpful tools such as code completion and an interactive data viewer.
Starting an R session becomes as simple as opening up RStudio and typing commands into the console.
Of course, this is not essential and more advanced users may prefer to work with R directly from the command line. (This author does.)

## 1.3 Installing packages

Once R is installed, we can install packages that extend R’s capabilities.
The default repository is the [Comprehensive R Archive Network](https://cran.r-project.org/mirrors.html) (CRAN), which is home to over 13,000 different R packages.
We can easily install packages from CRAN - say, the popular *[ggplot2](https://CRAN.R-project.org/package=ggplot2)* package for data visualization - by opening up R and typing in:

```
install.packages("ggplot2")
```

In our case, we want to install Bioconductor packages.
These packages are located in a separate repository (see comments below) so we first install the *[BiocManager](https://CRAN.R-project.org/package=BiocManager)* package to easily connect to the Bioconductor servers.

```
install.packages("BiocManager")
```

After that, we can use *[BiocManager](https://CRAN.R-project.org/package=BiocManager)*’s `install()` function to install any package from Bioconductor.
For example, the code chunk below uses this approach to install the *[SingleCellExperiment](https://bioconductor.org/packages/3.23/SingleCellExperiment)* package.
(The same command also works for any CRAN package; `install()` will automatically call `install.packages()` for us, as a matter of convenience.)

```
## The command below is a one-line shortcut for:
## library(BiocManager)
## install("SingleCellExperiment")
BiocManager::install("SingleCellExperiment")
```

Should we forget, the same instructions are present on the landing page of any Bioconductor package.
For example, looking at the [`scater`](https://bioconductor.org/packages/release/bioc/html/scater.html) package page on Bioconductor, we can see the following copy-pasteable instructions:

```
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("scater")
```

In fact, each Bioconductor book is itself a package that can be installed via *[BiocManager](https://CRAN.R-project.org/package=BiocManager)*.
This will automatically install all of the individual packages that are used in the book.
We illustrate below with *[OSCA.intro](https://bioconductor.org/packages/3.23/OSCA.intro)*, which is the package corresponding to this particular book.

```
BiocManager::install("OSCA.intro")
```

Packages only need to be installed once, and then they are available for all subsequent uses of a particular R installation.
There is no need to repeat the installation every time we start R.

## 1.4 Comments on Bioconductor versioning

Unlike CRAN, Bioconductor releases its packages as a cohort on a half-yearly cycle.
This comes with the guarantee that different packages will work together smoothly if they belong to the same cohort - as mentioned above, this is one of Bioconductor’s main selling points.
For a particular installation, the version of the cohort release can be easily obtained from *[BiocManager](https://bioconductor.org/packages/3.23/BiocManager)*:

```
BiocManager::version()
```

```
## [1] '3.23'
```

Each Bioconductor release relies on the latest release version of R, which in turn has yearly updates.
For example, Bioconductor 3.11 and 3.12 would use R 4.0, while Bioconductor 3.13 and 3.14 will use R 4.1, and so on.
Thus, getting the latest Bioconductor release usually requires us to install the latest release version of R; `BiocManager::install()` will then take care of the rest.

The interoperability guarantee mentioned above only extends to packages from the same version of Bioconductor.
Packages from different Bioconductor releases may not necessarily work together, e.g., due to updates in the data structures or function arguments.
Normally, `BiocManager::install()` will prevent us from installing versions from different versions, but if it does happen, we can fix incompatibilities with:

```
BiocManager::valid()
```

## 1.5 Finding relevant packages

To find relevant Bioconductor packages, one useful resource is the [BiocViews](https://bioconductor.org/packages/release/BiocViews.html) page.
This provides a hierarchically organized view of annotations associated with each Bioconductor package.
For example, under the [“Software”](https://bioconductor.org/packages/release/BiocViews.html#___Software) label, we might be interested in a particular [“Technology”](https://bioconductor.org/packages/release/BiocViews.html#___Technology) such as… say, [“SingleCell”](https://bioconductor.org/packages/release/BiocViews.html#___SingleCell).
This gives us a listing of all Bioconductor packages that might be useful for our single-cell data analyses.
CRAN uses the similar concept of [“Task views”](https://cran.r-project.org/web/views/), though this is understandably more general than genomics.
For example, the [Cluster task view page](https://cran.r-project.org/web/views/Cluster.html) lists an assortment of packages that are relevant to cluster analyses.

## 1.6 Staying up to date

Updating all R/Bioconductor packages is as simple as running `BiocManager::install()` without any arguments.
This will check for more recent versions of each package (within a Bioconductor release) and prompt the user to update if any are available.

```
BiocManager::install()
```

If we want to update to a more recent Bioconductor release, we can use the `version=` argument to explicitly state the version number.
This assumes that we have a version of R that is capable of handling the requested Bioconductor release.

```
BiocManager::install(version='3.23')
```

It is a good idea to make sure that you are using the latest versions of all packages, at least at the start of any analysis project.
This ensures that you have the most recent functionality and bugfixes.
The only exception is if there is a need to recover historical results, in which case we might prefer to use older versions of all packages:

```
# Installing CRAN packages as of 29th April, 2020;
# see https://packagemanager.rstudio.com/client/#/repos/1/overview for available dates.
options(repos = c(CRAN = "https://packagemanager.rstudio.com/all/277"))

# Using packages from Bioconductor version 3.10, see below. 
BiocManager::install(version="3.10")
```

More advanced users may consider using *[packrat](https://CRAN.R-project.org/package=packrat)*, Conda or Docker to create separate R environments for different analysis projects.
These approaches ensure that package updates for one project do not affect the reproducibility of results in other projects;
they also make it easier to share environments between users.
