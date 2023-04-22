# Integrate Django Admin into a legacy database

This is an example for integrating Django Admin into a legacy database:
- Legacy database & Django Admin are in the different databases
- Sqlite is used for demonstrating purpose (**admin_db.sqlite3; legacy_db.sqlite3)**
- The files to be checked are
  - settings.py (DATABASES & DATABASE_ROUTERS config)
  - db_routers.py
  - admin.py
  - models.py

Refer to the django documentation for more info:
- https://docs.djangoproject.com/en/4.2/topics/db/multi-db/
- https://docs.djangoproject.com/en/4.2/howto/legacy-databases/
