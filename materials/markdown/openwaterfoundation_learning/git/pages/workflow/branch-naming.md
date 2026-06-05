---
type: source-page
source: git
title: "Git Workflow / Branch Naming"
original_url: "https://learn.openwaterfoundation.org/owf-learn-git/workflow/branch-naming.html"
repo_url: "https://github.com/OpenWaterFoundation/owf-learn-git"
commit_sha: 42a393fb0e2daff55ae973f940ca946ae8d05acf
source_path: "mkdocs-project/docs/workflow/branch-naming.md"
source_blob: "https://github.com/OpenWaterFoundation/owf-learn-git/blob/42a393fb0e2daff55ae973f940ca946ae8d05acf/mkdocs-project/docs/workflow/branch-naming.md"
license: license_needs_review
ingested_at: 2026-06-04T02:06:47+00:00
status: source_ingested
tags: [git, github, version-control, week-02, week-03, week-17]
---

# Git Workflow / Branch Naming

Branching naming conventions are important to ensure communication within a software project.
General naming conventions will be imposed by the Git software (e.g., "master") and the Git workflow
that is selected by the core software development team (e.g., "stable" branch might be used for software releases).

Branches that will generally not be public will have less of a chance to cause issues during collaboration,
especially if the branches are never pushed to a cloud repository.
However, the branch name will often show up in commit messages,
such as a merge commit and pull request, and therefore it is helpful to adopt a minimal naming convention.

Assume that issues (requests and bug reports) are tracked in an issue tracker such as GitHub's issue tracker.
Each issue will then have an issue number.
Including the issue number in the branch name will ensure that a connection can be made between the branch
and various issue artifacts.

The following are properties that might be added to a branch name, with some discussion of pros and cons.
The development team and workflow for a project will determine what works best.

* use dashes between branch name parts
	+ See [Stack Overflow: Using slash character in Git branch name](http://stackoverflow.com/questions/2527355/using-the-slash-character-in-git-branch-name/2527452#2527452) - there
	are some known issues with using `/` so be safe and use a dash
* issue type
	+ using an issue type such as `feature`, `bug`, `hotfix`, `test`, `refactor`, etc. may be helpful
	+ however, an issue may evolve from bug to feature so assigning a type as a primary part of the identifier
	may be confusing over the lifetime of the issue (but this may not be an issue for simple items)
	+ can include an issue type keyword in the subject below rather than requiring
* issue number
	+ need this at a minimum to link to the issue tracker, consistent with GitHub, Bitbucket, etc. features
	+ using issue number alone can cause Git commands problems since git may not know whether the number is a branch name
	or SHA-1 hash number corresponding to a commit (so recommend including a subject)
* developer ID
	+ not recommended because it can be found in the issue tracker, more than one person may work on the issue,
	and the assignment of a developer may change over time
* subject
	+ it may be helpful to include a short subject (topic) to help quickly understand the focus of the issue and not get lost in issue numbers

Examples of suitable branch names when using an issue tracker are:

* `1234-add-save-to-main-menu`
* `bug-1234-crash-at-start`
* `1234-bug-crash-at-start`

The remote branch name should be consistent if possible, for example:

```text
origin/1234-add-save-to-main-menu
```

If an issue tracker is not used, then the issue type and subject are more important for context.
Again, the approach adopted should be determined based on what works for the team.
