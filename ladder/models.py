from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone
class Participant(models.Model):
	user = models.ForeignKey(User)
	latest_loss = models.DateTimeField(blank = True, null = True)
	latest_activity = models.DateTimeField()
	ranking = models.IntegerField(unique=True)
	
	class Meta:
		ordering=["ranking"]
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
class Match(models.Model):
	tournament = models.ForeignKey(Tournament)
	winner = models.OneToOneField(Participant, related_name="match_winner", null=True)
	loser = models.OneToOneField(Participant, related_name="match_loser", null=True)
	date = models.DateTimeField(default=datetime.now)
	score_winner = models.IntegerField()
	score_loser = models.IntegerField()
	class Meta:
		ordering=["-date"]
class Comment(models.Model):
    tournament = models.ForeignKey('ladder.Tournament', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    def __str__(self):
    	return self.text
    def approve(self):
        self.approved_comment = True
        self.save()
    class Meta:
    	ordering=["-created_date"]
    def __str__(self):
        return self.text