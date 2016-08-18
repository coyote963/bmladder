from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'body',)

# from django import forms
# from django.contrib.flatpages.models import FlatPage
# from tinymce.widgets import TinyMCE

# class PostForm(forms.ModelForm):

#     blogbody = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
 

#     class Meta:
#         model = FlatPage
#         fields = ['blogbody']