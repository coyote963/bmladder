# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-24 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0004_auto_20160824_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='slug',
            field=models.SlugField(unique='True'),
        ),
    ]
