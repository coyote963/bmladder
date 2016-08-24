from django.shortcuts import render, render_to_response
from ladder.forms import TournamentForm, CommentForm
from django.template import RequestContext
from ladder.models import Tournament,Participant
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime
from django.shortcuts import redirect, get_object_or_404

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

		if object.participants.all().filter(user = self.request.user).exists():
			context['in_tournament'] = True
		else:
			context['in_tournament'] = False
		context['self.request'] = self.request
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
	return render(request,
		'ladder/createtournament.html',
		{'tournament_form':tournament_form},
		)
def add_comment_to_post(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.tournament = tournament
            new_comment.save()
            return redirect('detail', pk)
    else:
        form = CommentForm()
    return render(request, 
    	'ladder/add_comment_to_post.html',
    	{'form': form},
    	)