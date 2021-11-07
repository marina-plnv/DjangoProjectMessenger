from django.contrib.auth.models import User
from django.db import models

class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=100)