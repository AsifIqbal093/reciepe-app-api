"""
Django command to wait for the Database to be availabale
"""


import time
from psycopg2 import OperationalError as Psycopg2opError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for Database...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2opError, OperationalError):
                self.stdout.write('Database unavailable, witing 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is availabale!'))
