import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django commands to pause exec until database operational."""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db access...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('DB Unavailable...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("I'm in!"))
