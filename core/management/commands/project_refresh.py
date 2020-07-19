from django.core.management import call_command
from django.core.management.base import BaseCommand
import django

django.setup()


class Command(BaseCommand):
    help = 'like project_reset but migrate migrations again'

    def handle(self, *args, **kwargs):
        print('Start Project Refresh...')
        call_command('project_reset')
        call_command('makemigrations')
        call_command('migrate')
        print('Completed Project Refresh...')
