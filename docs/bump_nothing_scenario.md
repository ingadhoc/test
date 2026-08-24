# Bump with nothing to bump

Fixture for the mergebot version bump. The pull request that carries this file
touches no module at all: only this file and the repository README.

Merged with `bump`, the bot finds no manifest to bump. That is a failure, and it
has to say so on the pull request instead of reporting a successful bump.
