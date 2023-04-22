class LegacyDbRouter:
    legacy_db_tables = ('department', 'employee')

    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.legacy_db_tables:
            return "legacy"

        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table in self.legacy_db_tables:
            return "legacy"

        return None

    def allow_relation(self, obj1, obj2, **hints):
        belong_to_legacy = obj1._meta.db_table in self.legacy_db_tables \
                           or obj2._meta.db_table in self.legacy_db_tables

        return True if belong_to_legacy else None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
