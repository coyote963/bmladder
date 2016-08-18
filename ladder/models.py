from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
class Participant(models.Model):
	user = models.ForeignKey(User)
	latest_loss = models.DateTimeField(blank = True, null = True)
	latest_activity = models.DateTimeField()
	ranking = models.IntegerField(unique=True)

# Create your models here.
class Tournament(models.Model):
	capacity = models.IntegerField()
	participants = models.ManyToManyField(Participant)
	rules = models.TextField()
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(default=datetime.now)
	date_starting = models.DateTimeField()
	date_ending = models.DateTimeField()
	
	class Meta:
		ordering=["-date_created"]
	def __str__(self):
		return self.title

