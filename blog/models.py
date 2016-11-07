from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

	class Meta:
		app_label = 'blog'
	
