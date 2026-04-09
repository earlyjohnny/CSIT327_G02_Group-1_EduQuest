from django.db import models
from django.conf import settings  # If organizer is linked to a User or a custom model

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=255)
    building_location = models.CharField(max_length=255)
    max_occupancy = models.PositiveIntegerField()  # Use PositiveIntegerField instead of IntegerField

    def __str__(self):
        return self.venue_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)

    # Link to organizer (replace with actual model if you have an Organizer model)
    # Example: settings.AUTH_USER_MODEL if it's a user
    org = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='events'
    )

    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        related_name='events'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title