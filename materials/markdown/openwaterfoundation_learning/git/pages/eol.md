---
type: source-page
source: git
title: "Git End-of-Line Issues"
original_url: "https://learn.openwaterfoundation.org/owf-learn-git/eol.html"
repo_url: "https://github.com/OpenWaterFoundation/owf-learn-git"
commit_sha: 42a393fb0e2daff55ae973f940ca946ae8d05acf
source_path: "mkdocs-project/docs/eol.md"
source_blob: "https://github.com/OpenWaterFoundation/owf-learn-git/blob/42a393fb0e2daff55ae973f940ca946ae8d05acf/mkdocs-project/docs/eol.md"
license: license_needs_review
ingested_at: 2026-06-04T02:06:47+00:00
status: source_ingested
tags: [git, github, version-control, week-02, week-03, week-17]
---

# Git End-of-Line Issues

**Note that end of line issues discussed below may not be much of an issue for some Git tool installs.
For example [Git for Windows](install/git.md#install-git-on-windows) installs with defaults appropriate for Windows.**

This documentation contains the following sections:

* [Background](#background)
* [Use `.gitattributes` File to Control Line Endings](#use-gitattributes-file-to-control-line-endings)
* [Additional Git Configuration](#additional-git-configuration)
	+ [Global property:  `core.eol`](#global-property-coreeol)
	+ [Global property:  `core.autocrlf`](#global-property-coreautocrlf)
* [Avoiding Issues by Using Consistent Developer Environment](#avoiding-issues-by-using-consistent-developer-environment)

----------------

## Background

End of line characters for text files are different based on the operating system.
Linux/Cygwin/Mac use line feed (`LF` indicated by the following character in code: `\n`)
whereas Windows uses carriage return followed by line feed (`CRLF`, indicated by the following characters in code: `\r\n`).
If not handled properly, developers working on the same repository but doing work on different operating systems
will introduce conflicting end of line characters, which will potentially result in every line of a file being different.

Git will, with default configuration, store end end of line as found in the file (the "native" end of line).
However, conventions have been established to ensure that:

* The repository only stores `LF` for end of line for text files
* The working files use the end of line character appropriate for the operating system

Background and a recommended solution is listed here:

* [Mind the End of Your Line](http://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/) - very good explanation
* [GitHub - Dealing with line endings](https://help.github.com/articles/dealing-with-line-endings/) - recommendations for each operating system

The bottom line is that the following should be configured as a best practice:

* Always store text files in the repository using linefeed only (Linux style `LF`).
* Text files in working files will have native operating system end of line.
* Using a `.gitattributes` file with each repository is the preferred way to ensure that the above happens.
* Can also set Git configuration variables to ensure that the above happens (although `.gitattributes` should suffice).

The following discuss how to properly handle end of line issues.

## Use `.gitattributes` File to Control Line Endings

Note that the `.gitattributes` file is available for Git 1.7.2 and above.

It is possible to use Git configuration settings (see next section) to control how line endings are handled.
However, this assumes that all developers consistently define their settings.
Instead, it is best to define how end of line is handled by using the per-repository `.gitattributes` file,
which is the "new way" of handling end of line configuration, and will supersede other settings.

The `.gitattributes` file is committed to the repository and will therefore be used consistently for all users,
assuming that client software recognizes the attributes.
The following is the recommended setting in the `.gitattributes` file:

```
# Set the default behavior, in case people don't have core.autocrlf set.
* text=auto

# Also can define which files are text and binary, to help Git make the right decision
*.md   text

*.png  binary
```

The person that sets up a repository initially should include an appropriate `.gitattributes` file in the root folder of the working files.

## Additional Git Configuration

The following additional configuration can be set to ensure proper handling of end of line,
although use of `.gitattributes` should handle.

### Global property:  `core.eol`

* `core.eol = native` is the default, which means that when Git writes files to the working directory
(such as with `git checkout`, `git clone`, and `git reset`),
it will use the native operating system end of line, `LF` for Linux/Cygwin/Mac and
`CRLF` for Windows.  Since this is the default, there is no need to change the setting if it is not set.

### Global property:  `core.autocrlf`

The following setting help ensure that the repository only contains text files with `LF` end of line characters.
They can be set if the `.gitattributes` approach does not seem to be working
(for example when git client software is not properly handling `.gitattributes`):

* Linux/Mac/Cygwin: `core.autocrlf = input` - this will ensure that operations that write text files to the
object database in `.git` convert `CRLF` to `LF` when writing, but reading will always return `LF`.

```
git config --global core.autocrlf input
```

* Windows:  `core.autocrlf = true` - this will ensure that operations that write text files to the
object database in `.git` convert `CRLF` to `LF` when writing, and to `CRLF` when reading.

```
git config --global core.autocrlf true
```

The default for `core.autocrlf` is false, meaning that Git will not adjust the end of line,
which could lead to `CRLF` files ending up in the repository (bad).
Therefore, it is generally best to set the above configuration for Linux and Windows to ensure that
the repository will only contain files with `LF`.

## Avoiding Issues by Using Consistent Developer Environment

One way to avoid issues is to encourage use of a consistent development environment for the development team.
This may not be possible, but can reduce issues.
For example, if the target installed environment is Windows, then everyone should use Windows for development.
If Linux is the target environment, then Linux/Cygwin/Mac can be used to ensure consistent end of line for files. 

A complication is if a Cygwin/Windows environment is used, for example, Eclipse on Windows and Cygwin command-line Git.
This case should be treated as if developing on two different operating systems.
Some warnings may be generated because files with `CRLF`are committed in Cygwin.
