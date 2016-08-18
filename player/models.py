from django.contrib.auth.models import User
from django.db import models

class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ingamename = models.CharField(max_length=25)
	avatar = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username