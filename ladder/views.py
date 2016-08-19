from django.shortcuts import render, render_to_response
from ladder.forms import TournamentForm
from django.template import RequestContext
from ladder.models import Tournament,Participant
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime
from django.shortcuts import redirect
class index(ListView):
	model = Tournament
	template_name = 'ladder/index.html'

class detail(DetailView):
	def post(self, request, *args, **kwargs):
		object = super(detail, self).get_object()
		new_participant = Participant(user = request.user,latest_activity = datetime.now(), ranking = object.participants.count()+1)
		new_participant.save()
		object.participants.add(new_participant)
		return redirect('detail', object.pk)

	model = Tournament
	template_name = 'ladder/tournamentpage.html'
	def get_context_data(self, **kwargs):
		context = super(detail, self).get_context_data(**kwargs)
		object = super(detail, self).get_object()
		rankinglist = object.participants.all().order_by('ranking')
		context['players_ranked'] = rankinglist
		if self.request.user.is_anonymous():
			context['is_logged_in'] = False
			context['in_tournament'] = False
		else:
			if object.participants.all().filter(user = self.request.user).exists():
				context['in_tournament'] = True
				context['is_logged_in'] = True
			else:
				context['in_tournament'] = False
				context['is_logged_in'] = True
		return context

# Create your views here.
def createtournament(request):
	context = RequestContext(request)
	if request.method == 'POST':
		print 'POST'
		tournament_form = TournamentForm(data=request.POST)
		if tournament_form.is_valid():
			tournament = tournament_form.save()
			tournament.save()
			return redirect('index')
		else:
			print tournament_form.errors
	else:
		tournament_form = TournamentForm()
	return render_to_response(
		'ladder/createtournament.html',
		{'tournament_form':tournament_form},
		context
		)

