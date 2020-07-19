import os

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User, Group

import django

django.setup()


class Command(BaseCommand):
    help = 'Create admin user .'

    def handle(self, *args, **kwargs):
        print('Starting Create Admin ...')
        self.create_admin_superuser()
        print('Completed Create Admin ...')

    def create_admin_superuser(self):
        # create user
        user = User(username='admin')
        user.first_name = "super user"
        user.last_name = "admin"
        user.set_password('password')
        user.is_superuser = True
        user.is_staff = True
        user.save()
