from django.db import models

# Create your models here.
class Sighting(models.Model):

    latitude = models.FloatField(max_length=30)
    longitude = models.FloatField(max_length=30)
    
    unique_squirrel_id = models.CharField(
        max_length=20,
        primary_key=True,
        unique=True
    )

    shift = models.CharField(
        max_length=2,
        default='AM'
    )

    date = models.DateField(
        auto_now=False        
    )

    age = models.CharField(
        max_length=15,
        default='Adult'
    )

    primary_fur_color = models.CharField(
        max_length=15,
        default='Gray'
    )

    highlight_fur_color = models.CharField(
        max_length=15,
        blank=True
    )

    location = models.CharField(
        max_length=30,
        default='Ground Plane'
    )

    specific_location = models.TextField(
        max_length=128,
        blank=True
    )

    running = models.BooleanField(
        default=False
    )

    chasing = models.BooleanField(
        default=False        
    )

    climbing = models.BooleanField(
        default=False        
    )

    eating = models.BooleanField(
        default=False        
    )

    foraging = models.BooleanField(
        default=False        
    )

    other_activity = models.TextField(
        max_length=128,
        blank=True
    )

    kuks = models.BooleanField(
        default=False
    )
    quaas = models.BooleanField(
        default=False
    )
    moans = models.BooleanField(
        default=False
    )
    tail_flags = models.BooleanField(
        default=False
    )
    tail_twitches = models.BooleanField(
        default=False
    )
    approaches = models.BooleanField(
        default=False
    )
    indifferent = models.BooleanField(
        default=False
    )
    runs_from = models.BooleanField(
        default=False
    )
    other_interaction = models.TextField(
        max_length=128,
        blank=True
    )