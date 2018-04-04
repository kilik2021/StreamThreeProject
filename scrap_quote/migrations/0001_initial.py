# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('type_of_boat', models.CharField(choices=[(None, 'Please select the type of boat'), ('Sailing Dinghy', 'Sailing Dinghy'), ('Motor Boat', 'Motor Boat'), ('Yacht', 'Yacht'), ('Narrowboat', 'Narrowboat')], max_length=20)),
                ('keel_type', models.CharField(choices=[('N/A', 'Not Applicable'), ('Fin Keel', 'Fin Keel'), ('Bilge Keel', 'Keel'), ('Other', 'Other')], max_length=10)),
                ('boat_length', models.PositiveSmallIntegerField()),
                ('boat_weight', models.PositiveSmallIntegerField()),
                ('hull_material', models.CharField(max_length=20)),
                ('hazardous_mats', models.CharField(blank=True, max_length=100)),
                ('engine_removed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't Know", "Don't Know")], max_length=10)),
                ('type_of_engine', models.CharField(blank=True, choices=[(None, 'Please select the type of engine.'), ('Outboard', 'Outboard'), ('Inboard', 'Inboard'), ('Twin Outboard', 'Twin Outboard'), ('Twin Inboard', 'Twin Inboard'), ('Other', 'Other')], max_length=15)),
                ('engine_make', models.CharField(blank=True, max_length=50)),
                ('engine_cylinders', models.PositiveSmallIntegerField(blank=True)),
                ('engine_hours', models.PositiveSmallIntegerField(blank=True)),
                ('engine_still_run', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't Know", "Don't Know")], max_length=10)),
                ('deliver_boat', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't Know", "Don't Know")], max_length=10)),
                ('scrap_where_located', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't Know", "Don't Know")], max_length=10)),
                ('boat_in_water', models.CharField(blank=True, choices=[(None, 'Please select if your boat is in the water.'), ('No', 'No'), ('Yes, along side and ready to be lifted', 'Yes, along side and ready to be lifted'), ('Yes, needs moving and lifting out', 'Yes, needs moving and lifting out')], max_length=40)),
                ('has_trailer', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't Know", "Don't Know")], max_length=10)),
                ('trailer_road_legal', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't Know", "Don't Know")], max_length=10)),
                ('travel_distance', models.PositiveSmallIntegerField(blank=True)),
                ('additional_info', tinymce.models.HTMLField()),
                ('my_consent', models.BooleanField(default=False)),
                ('date_approved', models.DateTimeField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]