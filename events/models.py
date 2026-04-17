from django.db import models
from django.conf import settings  # If organizer is linked to a User or a custom model

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=255)
    building_location = models.CharField(max_length=255)


    def __str__(self):
        return self.venue_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)


    org = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.CASCADE,
        related_name='events',
        null=True,
        blank=True
    )

    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        related_name='events',
        null=True,
        blank=True
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title