# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-14 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_images', '0004_add_sharpened_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbnailgroup',
            name='hd_sharpened_inverted',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='thumbnailgroup',
            name='regular_sharpened_inverted',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
