from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from clans.forms  import ClanForm,EntryForm,CommentForm
from clans.models import Clan, Comment
from player.models import Profile
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
@login_required
def clancreate(request):
	context = RequestContext(request)
	if request.method == 'POST':
		clan_form = ClanForm(data = request.POST)
		if clan_form.is_valid():
			new_clan = clan_form.save()
			if 'image' in request.FILES:
				new_clan.image = request.FILES['image']
			new_clan.save()
			return redirect('clandetail',slug = new_clan.slug)
		else:
			print clan_form.errors
	else:
		clan_form = ClanForm()
	return render(request,
		'clans/clancreate.html',
		{'clan_form':clan_form},
		context)
@login_required
def clandetail(request, slug):
	clan = get_object_or_404(Clan, slug = slug)
	members = Player.objects.filter(clan = clan)
	comments = Comment.objects.filter(clan = clan)
	if request.method == 'POST':
		comment_form = CommentForm(data = request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.author = request.user
			comment.clan = clan
			comment.save()
		else:
			print comment_form.errors
	else:
		comment_form=CommentForm()
	return render(request,
		'clans/clandetail.html',
		{'clan':clan, 'members':members, 'comment_form':comment_form, 'comments':comments})
@login_required
def clanenter(request, slug):
	clan = get_object_or_404(Clan, slug = slug)
	error_message = ""
	if request.method =='POST':
		form = EntryForm(data = request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			if clan.password == cd.get('password'):
				request.user.player.clan = clan
				request.user.player.save()
				return redirect('clandetail', slug)
			else:
				error_message = "Wrong Password!"
		else:
			print form.errors
	else:
		form = EntryForm()
	return render(request,
		'clans/clanenter.html',
		{'form':form,'clan':clan,'error_message':error_message}
		)
class ClanList(ListView):
	model = Clan
	template_name_suffix = '_list'
class ClanUpdate(PermissionRequiredMixin,UpdateView):
	permission_required = 'clan.can_change_clan'
	model = Clan
	template_name_suffix = '_update_form'
	fields = ['title','image','description','clantag']
	def get_success_url(self):
		return reverse('clandetail', kwargs={'slug':self.object.slug})
