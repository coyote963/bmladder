from django.shortcuts import render
from django import forms
from ladder.models import Tournament, Comment
# Create your views here.
class TournamentForm(forms.ModelForm):
	class Meta:
		model = Tournament
		fields = ('capacity','rules','title','date_starting','date_ending')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
