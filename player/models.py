from django.contrib.auth.models import User
from django.db import models
from clans.models import Clan

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)
	ingamename = models.CharField(max_length=25)
	avatar = models.ImageField(upload_to='profile_images', blank=True)
	clan = models.ForeignKey(Clan, blank=True, null=True)
	steamid = models.IntegerField(blank=True, null=True)
	steamimage = models.CharField(max_length=75, blank = True, null = True)
	def __unicode__(self):
		return self.user.username
