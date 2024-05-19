from django.db import models
from aidrequests.models import AidRequest


class AidDelivery(models.Model):
    aid_request = models.ForeignKey(AidRequest, on_delete=models.CASCADE)
    description = models.TextField()
    delivery_status = models.CharField(max_length=50)
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
