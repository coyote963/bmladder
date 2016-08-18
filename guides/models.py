from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Guide(models.Model):
	title = models.CharField(max_length= 140)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField()
	content = models.TextField()
	banner = models.ImageField(upload_to='guides',blank = True)
	teaser = models.TextField()
	def __str__(self):
		return self.title

	class Meta:
		app_label = 'guides' 