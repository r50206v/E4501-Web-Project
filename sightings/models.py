from django.db import models

# Create your models here.
class Sighting(models.Model):

    auto_increment_id = models.AutoField(
        primary_key=True
    )

    latitude = models.FloatField(max_length=30)
    longitude = models.FloatField(max_length=30)
    
    unique_squirrel_id = models.CharField(
        max_length=20,
    )

    hectare = models.CharField(
        max_length=30,
        blank=True
    )

    shift = models.CharField(
        max_length=2,
        default="AM",
        choices=(("AM", "AM"), ("PM", "PM"))
    )

    date = models.DateField(
        auto_now=False        
    )

    hectare_squirrel_number = models.IntegerField(
        null=True
    )

    age = models.CharField(
        max_length=15,
        default='Adult',
        choices=(("Adult", "Adult"), ("Juvenile", "Juvenile"))
    )

    primary_fur_color = models.CharField(
        max_length=15,
        default='Gray',
        choices=(("Gray", "Gray"), ("Cinnamon", "Cinnamon"), ("Black", "Black"), ("White", "White"))
    )

    highlight_fur_color = models.CharField(
        max_length=15,
        blank=True,
        choices=(("Gray", "Gray"), ("Cinnamon", "Cinnamon"), ("Black", "Black"), ("White", "White"))
    )

    combination_of_primary_and_highlight_color = models.TextField(
        max_length=128,
        blank=True
    )

    color_notes = models.TextField(
        max_length=300,
        blank=True
    )

    location = models.CharField(
        max_length=30,
        default='Ground Plane',
        choices=(("Ground Plane", "Ground Plane"), ("Above Ground", "Above Ground"))
    )

    above_ground_sighter_measurement = models.TextField(
        max_length=30,
        blank=True
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

    other_activities = models.TextField(
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
    other_interactions = models.TextField(
        max_length=128,
        blank=True
    )

    lat_long = models.TextField(
        max_length=300,
        blank=True
    )