from django.db import models
from users.models import User


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
