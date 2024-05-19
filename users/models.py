from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement_name = models.CharField(max_length=100)
    achievement_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
