from django import forms
from guides.models import Guide
from tinymce.widgets import TinyMCE
class GuideForm(forms.ModelForm):
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	class Meta:
		model = Guide
		fields = ('title','content','banner','teaser')
	class Media:
		js = ('/site_media/static/tiny_mce/tinymce.min.js',)
