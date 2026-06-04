---
type: source-page
source: git
title: "Git Messages ##"
original_url: "https://learn.openwaterfoundation.org/owf-learn-git/output-messages.html"
repo_url: "https://github.com/OpenWaterFoundation/owf-learn-git"
commit_sha: 42a393fb0e2daff55ae973f940ca946ae8d05acf
source_path: "mkdocs-project/docs/output-messages.md"
source_blob: "https://github.com/OpenWaterFoundation/owf-learn-git/blob/42a393fb0e2daff55ae973f940ca946ae8d05acf/mkdocs-project/docs/output-messages.md"
license: license_needs_review
ingested_at: 2026-06-04T02:06:47+00:00
status: source_ingested
tags: [git, github, version-control, week-02, week-03, week-17]
---

# Git Messages ##

The following is a list of Git messages and explanation of how to respond.

* [Deletion of directory ... failed](#deletion-of-directory-failed)
* [warning:  CRLF will be replaced by LF...](#warning-crlf-will-be-replaced-by-lf)
* [warning:  LF will be replaced by CRLF...](#warning-lf-will-be-replaced-by-crlf)

--------------

## Deletion of directory ... failed ##

The following message may be displayed when trying to checkout a branch, such as the `master` branch:

```sh
$ git checkout master
Deletion of directory 'CDSS-test/web-display/build-util' failed. Should I try again? (y/n) n
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
```

The above is indicative of git trying to delete a folder in the working files that is not part of
the branch being checked out, but which is still active in a window.

If `n` is selected, Git will checkout the branch but the indicated directory may erroneously remain because it
was open in a window.  In this case, checkout the branch where the directory existed,
close the window (or change directories/folders so the directory/folder in question is not active),
and then checkout the desired branch (master in the above example).

Otherwise, take action to close the directory/folder in question, and then select `y` to retry the checkout.
This should properly checkout the branch without the message.

## warning:  CRLF will be replaced by LF... ##

The following message may be displayed when adding files to the index (staging area), prior to committing changes:

```sh
$ git add -A
warning: CRLF will be replaced by LF in mkdocs-project/docs/datasets/water-rights-assets/example-sql.TSTool.
The file will have its original line endings in your working directory.

```

The warning is actually stating that upon checkout the next time, the local file with `CRLF` endings will have `LF`
because the environment that is running `git` is Linux or Mac and is configured to use `LF` for working area text files.
The warning may be shown when a `.gitattributes` file with `* text=auto` is used.
The end of line in the original file can be verified by using an editor to show the end of line characters.
For example running `vim -b filename` in Git Bash will display the following (note `^M` characters at end,
a condition that indicates `CRLF` line endings):

```text
Some text ^M
Some text ^M
Some text ^M
```

## warning:  LF will be replaced by CRLF... ##

The following message may be displayed when adding files to the index (staging area), prior to committing changes:

```sh
$ git add -A
warning: LF will be replaced by CRLF in src/file-with-CRLF-LF.txt.
The file will have its original line endings in your working directory.
warning: LF will be replaced by CRLF in src/file-with-LF-CRLF.txt.
The file will have its original line endings in your working directory.
warning: LF will be replaced by CRLF in src/file-with-LF.txt.
The file will have its original line endings in your working directory.
```

The warning is actually stating that upon checkout the next time, the local file with `LF` endings will have `CRLF`
because the environment that is running `git` is Windows and is configured to use `CRLF` for working area text files.
The warning may be shown when a `.gitattributes` file with `* text=auto` is used.
The end of line in the file can be verified by using an editor to show the end of line characters.
For example `vim -b filename` will display the following (note NO `^M` characters at end,
a condition that indicates `LF` line endings):

```txt
Some text
Some text
Some text
```
