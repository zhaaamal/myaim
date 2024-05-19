from django.db import models
from users.models import User
from events.models import Event


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    date = models.DateTimeField()
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

