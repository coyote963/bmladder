from django.shortcuts import render
from django import forms
from ladder.models import Tournament
# Create your views here.
class TournamentForm(forms.ModelForm):
	class Meta:
		model = Tournament
		fields = ('capacity','rules','title','date_starting','date_ending')