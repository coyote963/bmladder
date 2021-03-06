from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
	body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	class Meta:
		model = Post
		fields = ('title', 'body')
	class Media:
		js = ('/site_media/static/tiny_mce/tinymce.min.js',)

# from django import forms
# from django.contrib.flatpages.models import FlatPage
# from tinymce.widgets import TinyMCE

# class PostForm(forms.ModelForm):

#     blogbody = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
 

#     class Meta:
#         model = FlatPage
#         fields = ['blogbody']
