# Bump scenario

Fixture for testing the post-merge version bump of the mergebot.

The pull request that carries this file touches three modules and two paths that
are not modules. Merged with a merge commit and `bump`, the bot has to bump the
three modules and ignore the rest:

| Path | Expected |
|---|---|
| `mail_ux/models/res_users.py` | bumped |
| `maintenance_ux/views/maintenance_views.xml` | bumped |
| `portal_backend/models/res_users.py` | bumped |
| `README.md` (repository root) | ignored, not inside a module |
| `docs/bump_scenario.md` | ignored, `docs/` has no manifest |
