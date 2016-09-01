from django.shortcuts import render
from django import forms
from ladder.models import Tournament, Comment
from tinymce.widgets import TinyMCE
# Create your views here.
class TournamentForm(forms.ModelForm):
	rules = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	class Meta:
		model = Tournament
		fields = ('capacity','rules','title','date_starting','date_ending')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

