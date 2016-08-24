from django import forms
from django.forms.widgets import PasswordInput
from clans.models import Clan, Comment
from django.shortcuts import RequestContext
class ClanForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Clan
		fields = ('title','password','clantag','image', 'description','slug')
class EntryForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput)
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)