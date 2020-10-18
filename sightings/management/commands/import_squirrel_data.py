from sightings.models import Sighting
from django.core.management.base import BaseCommand
import pandas as pd

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **options):
        data = pd.read_csv(options['file_path'])
        
        data.columns = [
            c.lower().replace(' ', '_').replace('/', '_') 
            for c in data.columns
        ]
        data.rename(columns={
            "x": "latitude",
            "y": "longitude"
        }, inplace=True)
        data['date'] = pd.to_datetime(
            data['date'].astype(str),
            format='%m%d%Y'
        )
        sightList = data.to_dict(orient='records')
        

        sightList = [Sighting(**s) for s in sightList]
        Sighting.objects.all().delete()
        Sighting.objects.bulk_create(sightList)