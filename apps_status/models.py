from django.db import models
from apps_profile.models import User

# Create your models here.

class Status(models.Model):
    user = models.ForeignKey(User, default="kosong")
    status = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)
