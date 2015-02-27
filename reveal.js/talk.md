## Django Migrations - Tom Viner

A (pizza and) techie talk by [Tom Viner](http://tomviner.co.uk) /
[@tomviner](http://twitter.com/tomviner)


## Coming up:

- History
- Django Migrations
    - New commands
    - Interesting internals
    - Converting from South to Migrations

---

## Pre-history

In the beginning there was `syncdb`


## History

- dmigrations
- south
- django-evolution

Note: Quite funny watching the DjangoCon 2008: [Schema Evolution Panel](https://www.youtube.com/watch?v=VSq8m00p1FM)
they keep talking about branching and svn merges.


## A winner

2009: South become most popular


## Kickstarter in 2013

- [Schema Migrations for Django by Andrew Godwin](https://www.kickstarter.com/projects/andrewgodwin/schema-migrations-for-django)
- massively over funded
- open source works

---

## DB Migrations

- "South 2" built into Django 1.7
    - but 95% new code!
- `django.db.migrations`

Note: - cancelled backport for Django 1.4 to 1.6
- then https://github.com/andrewgodwin/south2


## New features

- Improved migration format
- Rebasing
- Improved autodetection
- Better merge detection

Note: - compact; introspectable without execution
- recreate squashed initial migrations (not whole history every time)
- improved field API, cross app dependencies
- merging branches now easier

---

## User interface changes


### New commands, part I

- `makemigrations`
- `migrate`

Note: - create new migrations
    - replaces `schemamigration`
- apply, unapply, list migrations


### New commands, part II

- `showmigrations`
- `showmigrations --plan`
- `sqlmigrate`
- `squashmigrations`
- `makemigrations --merge`

Note: - list migrations, marking which were applied
- list migrations in planned order
- SQL statements for a migration
- reduce several migrations into one
- "apps with more than one leaf migration"


### More changes

- syncdb is going away!
    - no more initial data
    - no more fake initial
        - except, returning  in django 1.8:
           - `migrate --fake-initial`
- migration numbers no longer matter

Note: - syncdb [deleted](https://github.com/django/django/commit/f6463bb38) in latest dev branch!


### New migration format

- No more frozen ORM
- Virtual model of your models


<!-- --- data-background="css/mformat.png" -->

Note: - Bye bye frozen models!
- Hello in memory simulation
- Also: no ability to introspect


# Demo time!

---

## Implementation

- Schema Editor
- Migrations machinary

---

## Schema Editor

- Like the ORM but for changing tables and columns
    - even Oracle support


<!-- --- data-background="css/sc_ed.png" -->


<!-- --- data-background="css/schema_editor.png" -->


## Migrations machinary

- Autodetector
- Operations
- Loader / Graph
- State
- Executor
- Optimiser


## Operations


<!-- --- data-background="css/load_fix.png" -->


## Squashing


## Merging


---

## Converting from South to Migrations

- fully migrate all DBs
<!-- -- class="fragment" -->
- Remove south from INSTALLED_APPS
<!-- -- class="fragment" -->
- Delete migration files
<!-- -- class="fragment" -->
- Run python manage.py makemigrations
<!-- -- class="fragment" -->
- Run python manage.py migrate --fake-initial
<!-- -- class="fragment" -->


## For third party package authors

- Final version of South 1.0
    - checks `south_migrations/` first to avoid clash

---

# Questions?