# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap_quote', '0024_auto_20180414_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date_declined',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='is_declined',
            field=models.BooleanField(default=False),
        ),
    ]