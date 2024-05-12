import json
import subprocess
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        subprocess.run(["python3", "manage.py", "loaddata", "static/catalog_data.json"])
