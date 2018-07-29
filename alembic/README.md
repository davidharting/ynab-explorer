# Alembic

This directory contains database migrations.
It was created with

```bash
alembic init alembic
```

To run migrations up:

```bash
PYTHONPATH=. alembic upgrade head
```

To revert the last migration:

```bash
PYTHONPATH=. alembic downgrade -1
```

Note that the dependency on psycopg2 is due to connecting to a Postgres database (see `env.py`). I do not directly import that anywhere, and alembic does not directly depend on it itself.
