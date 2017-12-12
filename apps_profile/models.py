from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    npm = models.CharField(max_length=10, unique=True)
    flag_nilai=  models.BooleanField(default=False)
    name = models.CharField(max_length=27, default='Kosong')
    expertise = models.ManyToManyField('Expertise',default='Kosong')
    email = models.EmailField(default='Kosong')
    linkedin_profile = models.URLField(default='Kosong')


LEVEL_CHOICES = (
    ('1', 'Beginner'),
    ('2', 'Intermediate'),
    ('3', 'Advanced'),
    ('4', 'Expert')
)

class Expertise(models.Model):
    expertise = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='1')

    def __str__(self):
        return str(self.expertise)
