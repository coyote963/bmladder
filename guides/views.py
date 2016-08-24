from django.shortcuts import render
from guides.forms import GuideForm
from guides.models import Guide
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
def guidecreate(request):
	context = RequestContext(request)
	if request.method == 'POST':
		
		current_user = request.user
		
		guide_form = GuideForm(data=request.POST)
		if guide_form.is_valid():
			guide = guide_form.save(commit=False)
			guide.user = request.user
			guide.date = datetime.now()
			
			if 'banner' in request.FILES:
				guide.banner = request.FILES['banner']
			guide.save()
		else:
			print guide_form.errors
			return redirect('guidelist')
		url = reverse('guidelist')
		return HttpResponseRedirect(url)
	else:
		guide_form = GuideForm()
	return render(request,
			'guides/create.html',
			{'guide_form':guide_form,}, 
			context
		)
class guidelist(ListView):
	model = Guide
class guidedetail(DetailView):
	model = Guide

