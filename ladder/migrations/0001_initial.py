# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 02:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_loss', models.DateTimeField()),
                ('latest_activity', models.DateTimeField()),
                ('ranking', models.IntegerField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('rules', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_starting', models.DateTimeField()),
                ('date_ending', models.DateTimeField()),
                ('is_open', models.BooleanField()),
                ('participants', models.ManyToManyField(to='ladder.Participant')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
