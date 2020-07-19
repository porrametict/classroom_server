import os
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'delete db.sqlite3 if existed'
    project_path = settings.BASE_DIR

    def handle(self, *args, **kwargs):
        print('Start Delete DB...')

        file_name = "db.sqlite3"
        db_path = os.path.join(self.project_path, file_name)

        try:
            os.remove(db_path)
            print("{} was deleted.".format(db_path))
        except FileNotFoundError or PermissionError:
            print("Can not delete {} file.".format(db_path))
        print('Completed Delete DB...')
