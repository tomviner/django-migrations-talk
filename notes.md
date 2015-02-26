# Django DB Migrations

- History
- Django Migrations
-- New commands
-- Interesting internals


## Pre-history

Originally there were many libraries:

- dmigrations
- south
- django-evolution

Quite funny watching the DjangoCon 2008: [Schema Evolution Panel](https://www.youtube.com/watch?v=VSq8m00p1FM)
they keep talking about branching and svn merges.


## A winner

2009: South become most popular


## Kickstarter in 2013

- [Schema Migrations for Django by Andrew Godwin](https://www.kickstarter.com/projects/andrewgodwin/schema-migrations-for-django)
- massively over funded
- open source works


## DB Migrations

- "South 2" built into Django 1.7
- but not just moving South into Django: 95% new code

Note: - cancelled backport for Django 1.4 to 1.6
- then https://github.com/andrewgodwin/south2


## New features

- Improved migration format
- Rebasing
- Improved autodetection
- Better merge detection


Note: - compact; introspectable without execution
- recreate squashed initial migrations (not whole history every time)
- improved field API
- merging branches now easier


## User interface changes


### New commands

- `makemigrations`: create new migrations (replaces `schemamigration`)
- `migrate`: apply, unapply, list migrations


#### Also

- `showmigrations`: list migrations, marking which were applied
- `showmigrations --plan`: list migrations in planned order
- `sqlmigrate`: SQL statements for a migration
- `squashmigrations`: reduce several migrations into one
- `makemigrations --merge`: "apps with more than one leaf migration"


### More changes

- syncdb is going away!
-- no more initial data
-- no more fake initial
--- except in django 1.8:
---- `migrate --fake-initial`
- migration numbers no longer matter

Note: - syncdb [deleted](https://github.com/django/django/commit/f6463bb38) in latest dev branch!

### New migration format

- No more frozen ORM
- Virtual model of your models

## Implementation

parts

Dependancy
Squash

## Converting from South to Migrations

## For third party package authors

- Final version of South 1.0
-- checks `south_migrations/` first to avoid clash

My ticket

Indexes DEP

18:34
32:33
42:30
