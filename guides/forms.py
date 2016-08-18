from django import forms
from guides.models import Guide

class GuideForm(forms.ModelForm):
	class Meta:
		model = Guide
		fields = ('title','content','banner','teaser')
