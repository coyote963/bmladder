# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-24 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='image',
            field=models.ImageField(blank=True, upload_to='clans'),
        ),
        migrations.AlterField(
            model_name='clan',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]