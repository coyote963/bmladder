from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
# Create your views here.
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)