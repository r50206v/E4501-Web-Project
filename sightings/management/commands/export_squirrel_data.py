from sightings.models import Sighting
from django.core.management.base import BaseCommand
import numpy as np
import pandas as pd

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **options):

        data = pd.DataFrame(list(Sighting.objects.all().values()))
        data.replace('nan', np.nan, inplace=True)
        data.to_csv(options['file_path'], index=False)