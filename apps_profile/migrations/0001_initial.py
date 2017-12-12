# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('npm', models.CharField(max_length=10, unique=True)),
                ('flag_nilai', models.BooleanField(default=False)),
                ('name', models.CharField(default='Kosong', max_length=27)),
                ('email', models.EmailField(default='Kosong', max_length=254)),
                ('linkedin_profile', models.URLField(default='Kosong')),
                ('expertise', models.ManyToManyField(default='Kosong', to='apps_profile.Expertise')),
            ],
        ),
    ]
