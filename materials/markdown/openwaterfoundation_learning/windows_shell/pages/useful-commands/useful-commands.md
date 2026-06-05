---
type: source-page
source: windows_shell
title: "Windows Shell / Useful Command Examples #"
original_url: "https://learn.openwaterfoundation.org/owf-learn-windows-shell/useful-commands/useful-commands.html"
repo_url: "https://github.com/OpenWaterFoundation/owf-learn-windows-shell"
commit_sha: 3d459b386751e1d799f13c63fa9a7dbcda1ac6d3
source_path: "mkdocs-project/docs/useful-commands/useful-commands.md"
source_blob: "https://github.com/OpenWaterFoundation/owf-learn-windows-shell/blob/3d459b386751e1d799f13c63fa9a7dbcda1ac6d3/mkdocs-project/docs/useful-commands/useful-commands.md"
license: license_needs_review
ingested_at: 2026-06-04T02:06:47+00:00
status: source_ingested
tags: [windows-shell, batch, reproducibility, week-02, week-03, week-17]
---

# Windows Shell / Useful Command Examples #

This page provides examples of useful Windows commands.
The commands can be run from the command line or used in a batch files.
See also [Useful Batch File Examples](../useful-batch-files/useful-batch-files.md).

* [Find the Locations of a Program](#find-the-locations-of-a-program)

--------------

## Find the Locations of a Program ##

It is useful to confirm which program is being run,
especially when multiple versions exist.
Use the [`where`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/where_1)
program to search the `PATH` environment variable for all occurences of the program.
This is similar to the Linux [`which`](https://linux.die.net/man/1/which) command.
The name of the program to be found can be any executable program, with or without file extension.

```
> where cmd
C:\Windows\System32\cmd.exe
```
