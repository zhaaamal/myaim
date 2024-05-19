from django.db import models
from users.models import User
from events.models import Event


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    availability_status = models.CharField(max_length=50)
    skills = models.TextField()
    joined_at = models.DateTimeField(auto_now_add=True)


class VolunteerAssignment(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
