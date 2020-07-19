import os
from django.conf import settings
from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'delete all migration files in project .'
    project_path = settings.BASE_DIR

    def handle(self, *args, **kwargs):
        print('Starting Clear Migrations  ...')
        self.delete_migrations()
        print('Completed Clear Migrations  ...')

    def get_project_app(self) -> list:
        app_labels = settings.LOCAL_APPS
        return [apps.get_app_config(app_label).path for app_label in app_labels]

    def delete_migrations(self):
        app_paths = self.get_project_app()
        paths = app_paths
        for path in paths:
            migration_path = os.path.join(path, 'migrations')
            if os.path.exists(migration_path):
                self.delete_migration_files(migration_path)

    def delete_migration_files(self, migration_path):
        for filename in os.listdir(migration_path):
            delete_path = os.path.join(migration_path, filename)
            if os.path.isfile(delete_path) and filename != "__init__.py":

                try:
                    os.remove(delete_path)
                    print("{} was deleted.".format(delete_path))
                except FileNotFoundError as e:
                    print("{}".format(e))
