from django.db import models
from users.models import User


class OnlineCourse(models.Model):
    course_title = models.CharField(max_length=100)
    course_description = models.TextField()
    course_duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE)
    certification_date = models.DateTimeField(auto_now_add=True)
