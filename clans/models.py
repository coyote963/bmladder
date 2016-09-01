from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Clan(models.Model):
	title = models.CharField(max_length= 30)
	clantag = models.CharField(max_length = 4)
	image = models.ImageField(upload_to='clans',blank = True)
	description = models.TextField()
	slug = models.SlugField(unique='True')
	password = models.CharField(max_length = 15)

	def __unicode__(self):
		return self.slug
class Comment(models.Model):
	author = models.ForeignKey(User,blank = True)
	content = models.TextField()
	clan = models.ForeignKey(Clan, blank = True)
	date = models.DateTimeField(default=datetime.now)
	class Meta:
		ordering = ['-date']