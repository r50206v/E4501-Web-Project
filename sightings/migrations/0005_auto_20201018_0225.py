# Generated by Django 3.1.2 on 2020-10-18 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0004_auto_20201018_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='auto_increment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
