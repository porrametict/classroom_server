from django.core.management import call_command
from django.core.management.base import BaseCommand
import django

django.setup()


class Command(BaseCommand):
    help = 'clear migrations , media folder and delete db.sqlite .'

    def handle(self, *args, **kwargs):
        print('Start Project Reset...')
        call_command('clear_migration_files')
        call_command('delete_db_sqlite')
        print('Completed Project Reset...')
