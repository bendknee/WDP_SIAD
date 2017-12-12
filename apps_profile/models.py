from django.db import models
from django.contrib.postgres.fields import ArrayField
#from apps_status.models import Status
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    npm = models.CharField(max_length=10, unique=True)
    flag_nilai=  models.BooleanField(default=False)
    name = models.CharField(max_length=27, default='Kosong')
    expertise = models.ManyToManyField('Expertise',default='Kosong')
    status = models.ForeignKey('apps_status.Status',default='Kosong')
    email = models.EmailField(default='Kosong')
    linkedin_profile = models.URLField(default='Kosong')

class Expertise(models.Model):
    expertise = models.CharField(max_length=20)
