import pandas as pd

from django.core.management.base import BaseCommand
from sightings.models import Sighting

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **options):

        data = pd.read_csv(options['file_path'])
        print(data.head(3))