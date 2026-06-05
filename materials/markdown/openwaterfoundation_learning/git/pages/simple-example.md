---
type: source-page
source: git
title: "Git Simple Examples"
original_url: "https://learn.openwaterfoundation.org/owf-learn-git/simple-example.html"
repo_url: "https://github.com/OpenWaterFoundation/owf-learn-git"
commit_sha: 42a393fb0e2daff55ae973f940ca946ae8d05acf
source_path: "mkdocs-project/docs/simple-example.md"
source_blob: "https://github.com/OpenWaterFoundation/owf-learn-git/blob/42a393fb0e2daff55ae973f940ca946ae8d05acf/mkdocs-project/docs/simple-example.md"
license: license_needs_review
ingested_at: 2026-06-04T02:06:47+00:00
status: source_ingested
tags: [git, github, version-control, week-02, week-03, week-17]
---

# Git Simple Examples

Git training sites provide simple examples.
The following illustrates common tasks.

**TODO smalers 2016-11-28 need to figure out whether repository should be used or are contrived examples below OK**

This documentation contains the following sections:

* [GitHub Repository Direct Edit for Single Developer](#github-repository-direct-edit-for-single-developer)
* [Other Examples](#other-examples)

## GitHub Repository Direct Edit for Single Developer

Some repositories are maintained by one people, with no edit conflicts.
The following illustrates the basic workflow in such cases, where direct edits of repository master branch occur.

The repository is created in GitHub by an account administrator.
Assume that the repository name is `org-product-name`.

Clone the repository to a local development space:

```
# Create the folders if necessary
$ cd ~/org-dev/MyProject/git-repos
# Clone using the URL that is provided on GitHub (or Bitbucket)
$ git clone https:/pathToRepo/org-product-name.git
```

This will result in a local folder `org-product-name`.
All repository files will be exist in a hidden `.git` folder.
All working files will exist under the `org-product-name` folder and can be edited as needed.

Check the status of the repository, can be run at any time:

```
$ git status
```

Try creating files with a text editor, making changes to existing files, etc.

The above will list files that have been added, modified, and deleted.
If a new folder has been added, it is listed without showing all the new files in the folder.

To actually add changes in the working files to the repository, it is necessary to use the [`git add`](https://git-scm.com/docs/git-add) command,
Specific files can be added by name, or the following can be used to add all files.
The following step is called "adding to index" or "adding to staging area".


```
# The following could also use --all
$ git add -A
$ git status
```

Once files are added, they are committed using the following:

```
$ git commit -m 'Commit message text`
```

The above only commits changes to the local repository files in the `.git` folder.
To push the edits to the cloud repository, use the following:

```
$ git push
# Enter account information for GitHub or Bitbucket
```

The above assumes that the remote repository has been configured, which generally is the case if the repository was cloned.

## Other Examples

**TODO smalers 2016-11-28 need to add more simple exampels**
