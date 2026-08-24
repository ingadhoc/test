# Paging samples

Filler files for the mergebot version bump fixture. The pull request that adds
them touches more files inside `mail_ux` than one page of the GitHub pull
request files listing holds, so any module sorting after `mail_ux` only shows up
on the second page.

They are never loaded: nothing imports this directory and no manifest lists it.
