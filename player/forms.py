from django import forms
from django.contrib.auth.models import User
from player.models import Profile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('email','username','password')

class PlayerForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('ingamename','avatar')