from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventMedia(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

