# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-10-01 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_auth', '0005_auto_20201001_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='profile_image',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
