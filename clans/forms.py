from django import forms
from django.forms.widgets import PasswordInput
from tinymce.widgets import TinyMCE
from clans.models import Clan, Comment
from django.shortcuts import RequestContext
class ClanForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	class Meta:
		model = Clan
		fields = ('title','password','clantag','image', 'description','slug')
class EntryForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput)
class CommentForm(forms.ModelForm):
	class Meta:
		help_texts = {
            'content': 'Type your message here and click submit to put it on the clan wall',
        }
		model = Comment
		fields = ('content',)
		widgets = {
          'content': forms.Textarea(attrs={'rows':1, 'cols':60}),
        }